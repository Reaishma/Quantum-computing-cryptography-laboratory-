
from flask import Flask, jsonify, request, render_template_string
from quantum_interface import quantum_interface
import json

app = Flask(__name__)

# HTML template with Q# backend integration
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Q# Quantum Computing Laboratory</title>
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a3e 50%, #2d2d5f 100%);
            color: #ffffff;
            min-height: 100vh;
        }
        .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
        .header {
            text-align: center;
            margin-bottom: 40px;
            padding: 30px 0;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
        }
        .header h1 {
            font-size: 3rem;
            background: linear-gradient(45deg, #00d4ff, #ff00ff, #ffff00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .tabs {
            display: flex;
            margin-bottom: 30px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 10px;
        }
        .tab {
            flex: 1;
            padding: 15px 25px;
            background: transparent;
            border: none;
            color: #ffffff;
            cursor: pointer;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        .tab.active {
            background: linear-gradient(45deg, #00d4ff, #ff00ff);
        }
        .tab-content {
            display: none;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 30px;
        }
        .tab-content.active { display: block; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 20px; }
        .card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 25px;
            backdrop-filter: blur(10px);
        }
        .button {
            background: linear-gradient(45deg, #00d4ff, #ff00ff);
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            color: white;
            cursor: pointer;
            margin: 5px;
            transition: transform 0.2s;
        }
        .button:hover { transform: translateY(-2px); }
        .input {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.1);
            color: white;
        }
        .quantum-state {
            background: rgba(0, 212, 255, 0.1);
            border: 1px solid rgba(0, 212, 255, 0.3);
            border-radius: 8px;
            padding: 15px;
            margin: 15px 0;
            font-family: monospace;
        }
        .stats {
            display: flex;
            justify-content: space-around;
            margin: 20px 0;
        }
        .stat {
            text-align: center;
        }
        .stat-value {
            font-size: 2rem;
            font-weight: bold;
            color: #00d4ff;
        }
        .circuit-builder {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin: 15px 0;
        }
        .gate {
            background: rgba(255, 255, 255, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 10px 15px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .gate:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: scale(1.05);
        }
    </style>
</head>
<body>
    <div id="app">
        <div class="container">
            <div class="header">
                <h1>Q# Quantum Computing Laboratory</h1>
                <p>Powered by Microsoft Q# - Real quantum computing operations</p>
            </div>

            <div class="tabs">
                <button class="tab" :class="{active: activeTab === 'quantum'}" @click="activeTab = 'quantum'">
                    Q# Quantum Simulation
                </button>
                <button class="tab" :class="{active: activeTab === 'crypto'}" @click="activeTab = 'crypto'">
                    Q# Quantum Cryptography
                </button>
                <button class="tab" :class="{active: activeTab === 'materials'}" @click="activeTab = 'materials'">
                    Q# Material Simulation
                </button>
            </div>

            <!-- Quantum Simulation Tab -->
            <div class="tab-content" :class="{active: activeTab === 'quantum'}">
                <div class="grid">
                    <div class="card">
                        <h3>Q# Quantum Circuit Builder</h3>
                        <div class="circuit-builder">
                            <div class="gate" @click="addGate('H')">H</div>
                            <div class="gate" @click="addGate('X')">X</div>
                            <div class="gate" @click="addGate('Y')">Y</div>
                            <div class="gate" @click="addGate('Z')">Z</div>
                            <div class="gate" @click="addGate('CNOT')">CNOT</div>
                            <div class="gate" @click="addGate('RZ')">RZ(θ)</div>
                            <div class="gate" @click="addGate('RY')">RY(θ)</div>
                        </div>
                        <div class="quantum-state">
                            Circuit: {{quantumCircuit.join(' → ')}}
                        </div>
                        <button class="button" @click="executeCircuit">Execute Q# Circuit</button>
                        <button class="button" @click="resetCircuit">Reset</button>
                        <div class="quantum-state" v-if="circuitResults.length">
                            <strong>Q# Results:</strong> {{circuitResults.join(', ')}}
                        </div>
                    </div>

                    <div class="card">
                        <h3>Q# Bell State Generator</h3>
                        <button class="button" @click="createBellState">Create Bell State</button>
                        <div class="quantum-state" v-if="bellState.length">
                            <strong>Bell State Measurement:</strong><br>
                            Qubit 1: {{bellState[0]}}<br>
                            Qubit 2: {{bellState[1]}}<br>
                            <strong>Entangled:</strong> {{bellState[0] === bellState[1] ? 'Yes' : 'No'}}
                        </div>
                    </div>

                    <div class="card">
                        <h3>Q# Quantum State Analysis</h3>
                        <button class="button" @click="measureEntanglement">Measure Entanglement</button>
                        <button class="button" @click="calculateFidelity">Calculate Fidelity</button>
                        <div class="stats">
                            <div class="stat">
                                <div class="stat-value">{{entanglement.toFixed(3)}}</div>
                                <div class="stat-label">Entanglement</div>
                            </div>
                            <div class="stat">
                                <div class="stat-value">{{fidelity.toFixed(3)}}</div>
                                <div class="stat-label">Fidelity</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Quantum Cryptography Tab -->
            <div class="tab-content" :class="{active: activeTab === 'crypto'}">
                <div class="grid">
                    <div class="card">
                        <h3>Q# BB84 Quantum Key Distribution</h3>
                        <input class="input" v-model.number="qkd.keyLength" placeholder="Key Length">
                        <button class="button" @click="startQKD">Start Q# BB84</button>
                        <div class="quantum-state" v-if="qkd.sharedKey.length">
                            <strong>Q# Generated Key:</strong> {{qkd.sharedKey.slice(0, 20).join('')}}...<br>
                            <strong>Error Rate:</strong> {{qkd.errorRate.toFixed(2)}}%<br>
                            <strong>Key Length:</strong> {{qkd.sharedKey.length}} bits
                        </div>
                    </div>

                    <div class="card">
                        <h3>Q# Quantum Random Number Generator</h3>
                        <input class="input" v-model.number="qrng.bits" placeholder="Number of bits">
                        <button class="button" @click="generateQuantumRandom">Generate Q# Random</button>
                        <div class="quantum-state" v-if="qrng.result">
                            <strong>Binary:</strong> {{qrng.result.binary.slice(0, 32)}}...<br>
                            <strong>Decimal:</strong> {{qrng.result.decimal}}<br>
                            <strong>Hex:</strong> {{qrng.result.hex}}
                        </div>
                    </div>

                    <div class="card">
                        <h3>Q# Post-Quantum Cryptography</h3>
                        <select class="input" v-model="pqc.algorithm">
                            <option>CRYSTALS-Kyber</option>
                            <option>CRYSTALS-Dilithium</option>
                            <option>SPHINCS+</option>
                            <option>FALCON</option>
                        </select>
                        <input class="input" v-model="pqc.message" placeholder="Message to encrypt">
                        <button class="button" @click="pqcEncrypt">Q# Encrypt</button>
                        <div class="quantum-state" v-if="pqc.encrypted">
                            <strong>Q# Encrypted:</strong> {{pqc.encrypted.slice(0, 50)}}...
                        </div>
                    </div>

                    <div class="card">
                        <h3>Q# Quantum Digital Signature</h3>
                        <input class="input" v-model="qsign.document" placeholder="Document to sign">
                        <button class="button" @click="quantumSign">Q# Sign</button>
                        <div class="quantum-state" v-if="qsign.signature">
                            <strong>Q# Signature:</strong> {{qsign.signature}}<br>
                            <strong>Valid:</strong> {{qsign.valid ? 'Yes' : 'No'}}
                        </div>
                    </div>
                </div>
            </div>

            <!-- Materials Tab -->
            <div class="tab-content" :class="{active: activeTab === 'materials'}">
                <div class="grid">
                    <div class="card">
                        <h3>Q# Material Property Simulator</h3>
                        <input class="input" v-model="material.name" placeholder="Material Name">
                        <input class="input" v-model.number="material.temperature" placeholder="Temperature (K)">
                        <input class="input" v-model.number="material.pressure" placeholder="Pressure (atm)">
                        <button class="button" @click="simulateMaterial">Q# Simulate</button>
                        <div class="quantum-state" v-if="material.results">
                            <strong>Q# Simulation Results:</strong><br>
                            Conductivity: {{material.results.conductivity}}<br>
                            Band Gap: {{material.results.bandGap}} eV<br>
                            Magnetic Moment: {{material.results.magneticMoment}} μB
                        </div>
                    </div>

                    <div class="card">
                        <h3>Q# Molecular Simulation</h3>
                        <input class="input" v-model.number="molecule.numAtoms" placeholder="Number of atoms">
                        <input class="input" v-model.number="molecule.temperature" placeholder="Temperature (K)">
                        <button class="button" @click="simulateMolecule">Q# Molecular Sim</button>
                        <div class="quantum-state" v-if="molecule.results">
                            <strong>Q# Molecular Results:</strong><br>
                            Energy: {{molecule.results.energy.toFixed(2)}} eV<br>
                            Bond Strength: {{molecule.results.bondStrength.toFixed(3)}}<br>
                            Vibration Freq: {{molecule.results.vibrationFrequency.toFixed(1)}} cm⁻¹
                        </div>
                    </div>

                    <div class="card">
                        <h3>Q# Quantum Database</h3>
                        <input class="input" v-model="db.query" placeholder="Quantum query">
                        <input class="input" v-model.number="db.entries" placeholder="Number of entries">
                        <button class="button" @click="executeQuery">Q# Query</button>
                        <div class="quantum-state" v-if="db.result">
                            <strong>Q# Query Results:</strong><br>
                            Found: {{db.result.results.filter(x => x).length}} entries<br>
                            Coherence Time: {{db.result.coherenceTime}}ms<br>
                            Quantum Entries: {{db.result.quantumEntries}}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const { createApp } = Vue;

        createApp({
            data() {
                return {
                    activeTab: 'quantum',
                    
                    // Q# Quantum Circuit
                    quantumCircuit: [],
                    circuitResults: [],
                    bellState: [],
                    entanglement: 0,
                    fidelity: 0,
                    
                    // Q# Cryptography
                    qkd: {
                        keyLength: 256,
                        sharedKey: [],
                        errorRate: 0
                    },
                    qrng: {
                        bits: 128,
                        result: null
                    },
                    pqc: {
                        algorithm: 'CRYSTALS-Kyber',
                        message: '',
                        encrypted: ''
                    },
                    qsign: {
                        document: '',
                        signature: '',
                        valid: false
                    },
                    
                    // Q# Materials
                    material: {
                        name: '',
                        temperature: 300,
                        pressure: 1,
                        results: null
                    },
                    molecule: {
                        numAtoms: 4,
                        temperature: 300,
                        results: null
                    },
                    db: {
                        query: '',
                        entries: 16,
                        result: null
                    }
                }
            },

            methods: {
                async addGate(gate) {
                    this.quantumCircuit.push(gate);
                },

                async executeCircuit() {
                    try {
                        const response = await fetch('/api/execute_circuit', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ gates: this.quantumCircuit })
                        });
                        const result = await response.json();
                        this.circuitResults = result.results;
                    } catch (error) {
                        console.error('Q# Circuit execution error:', error);
                    }
                },

                resetCircuit() {
                    this.quantumCircuit = [];
                    this.circuitResults = [];
                },

                async createBellState() {
                    try {
                        const response = await fetch('/api/bell_state');
                        const result = await response.json();
                        this.bellState = result.results;
                    } catch (error) {
                        console.error('Q# Bell state error:', error);
                    }
                },

                async measureEntanglement() {
                    try {
                        const response = await fetch('/api/entanglement');
                        const result = await response.json();
                        this.entanglement = result.entanglement;
                    } catch (error) {
                        console.error('Q# Entanglement error:', error);
                    }
                },

                async calculateFidelity() {
                    try {
                        const response = await fetch('/api/fidelity');
                        const result = await response.json();
                        this.fidelity = result.fidelity;
                    } catch (error) {
                        console.error('Q# Fidelity error:', error);
                    }
                },

                async startQKD() {
                    try {
                        const response = await fetch('/api/bb84', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ keyLength: this.qkd.keyLength })
                        });
                        const result = await response.json();
                        this.qkd.sharedKey = result.sharedKey;
                        this.qkd.errorRate = result.errorRate;
                    } catch (error) {
                        console.error('Q# BB84 error:', error);
                    }
                },

                async generateQuantumRandom() {
                    try {
                        const response = await fetch('/api/qrng', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ bits: this.qrng.bits })
                        });
                        const result = await response.json();
                        this.qrng.result = result;
                    } catch (error) {
                        console.error('Q# QRNG error:', error);
                    }
                },

                async pqcEncrypt() {
                    try {
                        const response = await fetch('/api/pqc_encrypt', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ 
                                message: this.pqc.message,
                                algorithm: this.pqc.algorithm
                            })
                        });
                        const result = await response.json();
                        this.pqc.encrypted = result.encrypted;
                    } catch (error) {
                        console.error('Q# PQC error:', error);
                    }
                },

                async quantumSign() {
                    try {
                        const response = await fetch('/api/quantum_sign', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ document: this.qsign.document })
                        });
                        const result = await response.json();
                        this.qsign.signature = result.signature;
                        this.qsign.valid = true;
                    } catch (error) {
                        console.error('Q# Signature error:', error);
                    }
                },

                async simulateMaterial() {
                    try {
                        const response = await fetch('/api/material_sim', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({
                                name: this.material.name,
                                temperature: this.material.temperature,
                                pressure: this.material.pressure
                            })
                        });
                        const result = await response.json();
                        this.material.results = result;
                    } catch (error) {
                        console.error('Q# Material simulation error:', error);
                    }
                },

                async simulateMolecule() {
                    try {
                        const response = await fetch('/api/molecule_sim', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({
                                numAtoms: this.molecule.numAtoms,
                                temperature: this.molecule.temperature
                            })
                        });
                        const result = await response.json();
                        this.molecule.results = result;
                    } catch (error) {
                        console.error('Q# Molecular simulation error:', error);
                    }
                },

                async executeQuery() {
                    try {
                        const response = await fetch('/api/quantum_db', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({
                                query: this.db.query,
                                entries: this.db.entries
                            })
                        });
                        const result = await response.json();
                        this.db.result = result;
                    } catch (error) {
                        console.error('Q# Database query error:', error);
                    }
                }
            }
        }).mount('#app');
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/execute_circuit', methods=['POST'])
def execute_circuit():
    data = request.json
    gates = data.get('gates', [])
    results = quantum_interface.execute_circuit(gates)
    return jsonify({'results': results})

@app.route('/api/bell_state')
def bell_state():
    results = quantum_interface.create_bell_state()
    return jsonify({'results': list(results)})

@app.route('/api/entanglement')
def entanglement():
    entanglement = quantum_interface.measure_entanglement()
    return jsonify({'entanglement': entanglement})

@app.route('/api/fidelity')
def fidelity():
    fidelity = quantum_interface.calculate_fidelity()
    return jsonify({'fidelity': fidelity})

@app.route('/api/bb84', methods=['POST'])
def bb84():
    data = request.json
    key_length = data.get('keyLength', 256)
    shared_key, error_rate = quantum_interface.bb84_key_distribution(key_length)
    return jsonify({
        'sharedKey': shared_key,
        'errorRate': error_rate
    })

@app.route('/api/qrng', methods=['POST'])
def qrng():
    data = request.json
    bits = data.get('bits', 128)
    result = quantum_interface.quantum_random_generator(bits)
    return jsonify(result)

@app.route('/api/pqc_encrypt', methods=['POST'])
def pqc_encrypt():
    data = request.json
    message = data.get('message', '')
    algorithm = data.get('algorithm', 'CRYSTALS-Kyber')
    encrypted = quantum_interface.pqc_encryption(message, algorithm)
    return jsonify({'encrypted': encrypted})

@app.route('/api/quantum_sign', methods=['POST'])
def quantum_sign():
    data = request.json
    document = data.get('document', '')
    signature = quantum_interface.quantum_signature(document)
    return jsonify({'signature': signature})

@app.route('/api/material_sim', methods=['POST'])
def material_sim():
    data = request.json
    name = data.get('name', 'unknown')
    temperature = data.get('temperature', 300)
    pressure = data.get('pressure', 1)
    results = quantum_interface.simulate_material(name, temperature, pressure)
    return jsonify(results)

@app.route('/api/molecule_sim', methods=['POST'])
def molecule_sim():
    data = request.json
    num_atoms = data.get('numAtoms', 4)
    temperature = data.get('temperature', 300)
    results = quantum_interface.molecular_simulation(num_atoms, temperature)
    return jsonify(results)

@app.route('/api/quantum_db', methods=['POST'])
def quantum_db():
    data = request.json
    query = data.get('query', '')
    entries = data.get('entries', 16)
    results = quantum_interface.quantum_database_query(query, entries)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
