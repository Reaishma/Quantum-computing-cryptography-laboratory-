
<template>
  <div class="grid">
    <div class="card">
      <h3>Quantum Circuit Builder</h3>
      <input class="input" v-model="circuitName" placeholder="Circuit Name">
      <input class="input" v-model.number="qubits" placeholder="Number of Qubits">
      
      <div class="gate-buttons">
        <div class="gate" @click="addGate('H')">H</div>
        <div class="gate" @click="addGate('X')">X</div>
        <div class="gate" @click="addGate('Y')">Y</div>
        <div class="gate" @click="addGate('Z')">Z</div>
        <div class="gate" @click="addGate('CNOT')">CNOT</div>
        <div class="gate" @click="addGate('RZ')">RZ(θ)</div>
      </div>
      
      <div class="quantum-state">
        Circuit: {{ gates.join(' → ') }}
      </div>
      <div class="quantum-state">
        State: {{ quantumState }}
      </div>
      
      <button class="button" @click="executeCircuit">Execute Circuit</button>
      <button class="button" @click="saveCircuit">Save Circuit</button>
      <button class="button danger" @click="resetCircuit">Reset</button>
    </div>

    <div class="card">
      <h3>Molecular Simulation</h3>
      <select class="input" v-model="moleculeType">
        <option value="h2o">H2O - Water</option>
        <option value="co2">CO2 - Carbon Dioxide</option>
        <option value="nh3">NH3 - Ammonia</option>
        <option value="random">Random Molecule</option>
      </select>
      
      <div class="parameter-inputs">
        <input class="input" v-model.number="temperature" placeholder="Temperature (K)">
        <input class="input" v-model.number="pressure" placeholder="Pressure (atm)">
      </div>
      
      <button class="button" @click="generateMolecule">Generate Molecule</button>
      
      <div class="molecular-viewer" v-if="molecule">
        <h4>{{ molecule.name }}</h4>
        <svg width="400" height="300" class="molecule-svg">
          <circle 
            v-for="atom in molecule.atoms" 
            :key="atom.id"
            :cx="atom.x" 
            :cy="atom.y" 
            r="15" 
            :fill="atom.color"
          />
          <text 
            v-for="atom in molecule.atoms" 
            :key="'text-' + atom.id"
            :x="atom.x" 
            :y="atom.y + 5" 
            text-anchor="middle" 
            fill="white" 
            font-size="12"
          >
            {{ atom.symbol }}
          </text>
        </svg>
      </div>
    </div>

    <div class="card">
      <h3>Saved Circuits</h3>
      <div class="circuit-list">
        <div v-for="circuit in circuits" :key="circuit.id" class="circuit-item">
          <div class="circuit-info">
            <strong>{{ circuit.name }}</strong>
            <span>{{ circuit.qubits }} qubits</span>
            <span>Fidelity: {{ circuit.fidelity?.toFixed(3) }}</span>
          </div>
          <div class="circuit-actions">
            <button class="button small" @click="loadCircuit(circuit)">Load</button>
            <button class="button small danger" @click="deleteCircuit(circuit.id)">Delete</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { quantumAPI } from '../services/api'

export default {
  name: 'QuantumSimulation',
  data() {
    return {
      circuitName: '',
      qubits: 3,
      gates: [],
      quantumState: '|0⟩',
      circuits: [],
      moleculeType: 'h2o',
      molecule: null,
      temperature: 300,
      pressure: 1
    }
  },
  mounted() {
    this.loadCircuits()
  },
  methods: {
    addGate(gate) {
      this.gates.push(gate)
    },
    
    async executeCircuit() {
      if (this.circuits.length > 0) {
        try {
          const response = await quantumAPI.executeCircuit(this.circuits[0].id)
          this.quantumState = response.data.state
        } catch (error) {
          console.error('Error executing circuit:', error)
        }
      }
    },
    
    async saveCircuit() {
      if (!this.circuitName) {
        alert('Please enter a circuit name')
        return
      }
      
      try {
        const circuitData = {
          name: this.circuitName,
          gates: this.gates,
          state: this.quantumState,
          qubits: this.qubits
        }
        
        const response = await quantumAPI.createCircuit(circuitData)
        this.circuits.push(response.data)
        this.circuitName = ''
      } catch (error) {
        console.error('Error saving circuit:', error)
      }
    },
    
    resetCircuit() {
      this.gates = []
      this.quantumState = '|0⟩'
    },
    
    async loadCircuits() {
      try {
        const response = await quantumAPI.getCircuits()
        this.circuits = response.data
      } catch (error) {
        console.error('Error loading circuits:', error)
      }
    },
    
    loadCircuit(circuit) {
      this.circuitName = circuit.name
      this.gates = [...circuit.gates]
      this.quantumState = circuit.state
      this.qubits = circuit.qubits
    },
    
    async deleteCircuit(id) {
      try {
        await quantumAPI.deleteCircuit(id)
        this.circuits = this.circuits.filter(c => c.id !== id)
      } catch (error) {
        console.error('Error deleting circuit:', error)
      }
    },
    
    async generateMolecule() {
      try {
        const response = await quantumAPI.generateMolecule({
          type: this.moleculeType,
          temperature: this.temperature,
          pressure: this.pressure
        })
        this.molecule = response.data
      } catch (error) {
        console.error('Error generating molecule:', error)
      }
    }
  }
}
</script>
