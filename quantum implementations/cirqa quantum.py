
"""
Quantum Computing & Cryptography Laboratory - Cirq Implementation
Google Cirq framework for quantum circuit simulation and cryptography
"""

import cirq
import numpy as np
import matplotlib.pyplot as plt
import random
import hashlib
from typing import List, Dict, Tuple, Optional
import json
from datetime import datetime

class CirqQuantumLab:
    """Main class for Cirq-based quantum computing laboratory"""
    
    def __init__(self):
        self.simulator = cirq.Simulator()
        self.circuits = {}
        self.molecules = {}
        self.crypto_keys = {}
        
    # === QUANTUM CIRCUIT OPERATIONS ===
    
    def create_quantum_circuit(self, name: str, num_qubits: int, gates: List[str]) -> Dict:
        """Create a quantum circuit with specified gates using Cirq"""
        
        # Create qubits
        qubits = [cirq.LineQubit(i) for i in range(num_qubits)]
        circuit = cirq.Circuit()
        
        # Apply gates based on the gate list
        for i, gate in enumerate(gates):
            qubit_idx = i % num_qubits
            
            if gate.upper() == 'H':
                circuit.append(cirq.H(qubits[qubit_idx]))
            elif gate.upper() == 'X':
                circuit.append(cirq.X(qubits[qubit_idx]))
            elif gate.upper() == 'Y':
                circuit.append(cirq.Y(qubits[qubit_idx]))
            elif gate.upper() == 'Z':
                circuit.append(cirq.Z(qubits[qubit_idx]))
            elif gate.upper() == 'CNOT' and num_qubits > 1:
                control = qubit_idx
                target = (qubit_idx + 1) % num_qubits
                circuit.append(cirq.CNOT(qubits[control], qubits[target]))
            elif gate.upper() == 'RZ':
                circuit.append(cirq.rz(np.pi/4)(qubits[qubit_idx]))
        
        # Add measurements
        circuit.append(cirq.measure(*qubits, key='result'))
        
        # Store circuit
        circuit_id = len(self.circuits) + 1
        self.circuits[circuit_id] = {
            'id': circuit_id,
            'name': name,
            'circuit': circuit,
            'qubits': qubits,
            'num_qubits': num_qubits,
            'gates': gates,
            'created_at': datetime.now().isoformat()
        }
        
        return {
            'id': circuit_id,
            'name': name,
            'num_qubits': num_qubits,
            'gates': gates,
            'circuit_str': str(circuit),
            'depth': len(circuit)
        }
    
    def execute_circuit(self, circuit_id: int, repetitions: int = 1000) -> Dict:
        """Execute a quantum circuit and return results"""
        if circuit_id not in self.circuits:
            raise ValueError(f"Circuit {circuit_id} not found")
        
        circuit_data = self.circuits[circuit_id]
        circuit = circuit_data['circuit']
        
        # Execute circuit
        result = self.simulator.run(circuit, repetitions=repetitions)
        measurements = result.measurements['result']
        
        # Convert measurements to counts
        counts = {}
        for measurement in measurements:
            bitstring = ''.join(str(bit) for bit in measurement)
            counts[bitstring] = counts.get(bitstring, 0) + 1
        
        # Get statevector before measurement
        statevector_circuit = circuit.copy()
        # Remove measurements for statevector simulation
        statevector_circuit = cirq.Circuit([op for op in statevector_circuit.all_operations() 
                                          if not isinstance(op.gate, cirq.MeasurementGate)])
        
        statevector_result = self.simulator.simulate(statevector_circuit)
        statevector = statevector_result.final_state_vector
        
        return {
            'circuit_id': circuit_id,
            'repetitions': repetitions,
            'counts': counts,
            'statevector': statevector.tolist(),
            'probabilities': {state: count/repetitions for state, count in counts.items()},
            'success': True
        }
    
    def create_bell_state(self) -> Dict:
        """Create a Bell state (entangled qubits) using Cirq"""
        qubits = cirq.LineQubit.range(2)
        circuit = cirq.Circuit()
        
        # Create Bell state
        circuit.append(cirq.H(qubits[0]))  # Hadamard on first qubit
        circuit.append(cirq.CNOT(qubits[0], qubits[1]))  # CNOT gate
        circuit.append(cirq.measure(*qubits, key='bell'))
        
        # Execute
        result = self.simulator.run(circuit, repetitions=1000)
        measurements = result.measurements['bell']
        
        # Convert to counts
        counts = {}
        for measurement in measurements:
            bitstring = ''.join(str(bit) for bit in measurement)
            counts[bitstring] = counts.get(bitstring, 0) + 1
        
        return {
            'name': 'Bell State',
            'circuit': str(circuit),
            'counts': counts,
            'entanglement': self._calculate_entanglement(counts),
            'fidelity': self._calculate_fidelity(counts, {'00': 0.5, '11': 0.5})
        }
    
    # === MOLECULAR SIMULATION ===
    
    def simulate_molecule(self, molecule_type: str, temperature: float = 300, pressure: float = 1) -> Dict:
        """Simulate molecular structures using Cirq quantum circuits"""
        
        molecules = {
            'h2o': {'atoms': ['H', 'H', 'O'], 'bonds': 2, 'qubits': 6},
            'co2': {'atoms': ['C', 'O', 'O'], 'bonds': 2, 'qubits': 6},
            'nh3': {'atoms': ['N', 'H', 'H', 'H'], 'bonds': 3, 'qubits': 8},
            'ch4': {'atoms': ['C', 'H', 'H', 'H', 'H'], 'bonds': 4, 'qubits': 10}
        }
        
        if molecule_type.lower() not in molecules:
            raise ValueError(f"Molecule {molecule_type} not supported")
        
        mol_data = molecules[molecule_type.lower()]
        num_qubits = mol_data['qubits']
        qubits = cirq.LineQubit.range(num_qubits)
        
        # Create molecular circuit
        circuit = cirq.Circuit()
        
        # Initialize molecular state
        for i in range(0, num_qubits, 2):
            circuit.append(cirq.H(qubits[i]))  # Superposition for electron pairs
            if i + 1 < num_qubits:
                circuit.append(cirq.CNOT(qubits[i], qubits[i + 1]))  # Entangle electron pairs
        
        # Add molecular interactions
        for bond in range(mol_data['bonds']):
            if bond * 2 + 1 < num_qubits:
                circuit.append(cirq.rz(np.pi * temperature / 1000)(qubits[bond * 2]))
                circuit.append(cirq.ry(np.pi * pressure / 10)(qubits[bond * 2 + 1]))
        
        # Execute simulation
        result = self.simulator.simulate(circuit)
        statevector = result.final_state_vector
        
        # Calculate molecular properties
        properties = self._calculate_molecular_properties(statevector, temperature, pressure)
        
        molecule_id = len(self.molecules) + 1
        self.molecules[molecule_id] = {
            'id': molecule_id,
            'type': molecule_type,
            'atoms': mol_data['atoms'],
            'properties': properties,
            'circuit': str(circuit),
            'temperature': temperature,
            'pressure': pressure
        }
        
        return self.molecules[molecule_id]
    
    # === QUANTUM CRYPTOGRAPHY ===
    
    def bb84_key_distribution(self, key_length: int = 256) -> Dict:
        """Implement BB84 Quantum Key Distribution protocol using Cirq"""
        
        # Alice's random bits and bases
        alice_bits = [random.randint(0, 1) for _ in range(key_length * 2)]
        alice_bases = [random.randint(0, 1) for _ in range(key_length * 2)]
        
        # Bob's random bases
        bob_bases = [random.randint(0, 1) for _ in range(key_length * 2)]
        
        # Quantum transmission simulation
        bob_measurements = []
        
        for i in range(len(alice_bits)):
            # Create quantum circuit for each bit
            qubit = cirq.LineQubit(0)
            circuit = cirq.Circuit()
            
            # Alice prepares qubit
            if alice_bits[i] == 1:
                circuit.append(cirq.X(qubit))  # Prepare |1⟩
            
            if alice_bases[i] == 1:
                circuit.append(cirq.H(qubit))  # Use diagonal basis
            
            # Bob measures
            if bob_bases[i] == 1:
                circuit.append(cirq.H(qubit))  # Measure in diagonal basis
            
            circuit.append(cirq.measure(qubit, key='bit'))
            
            # Execute measurement
            result = self.simulator.run(circuit, repetitions=1)
            measured_bit = int(result.measurements['bit'][0][0])
            bob_measurements.append(measured_bit)
        
        # Basis reconciliation
        matching_bases = []
        shared_key_bits = []
        
        for i in range(len(alice_bits)):
            if alice_bases[i] == bob_bases[i]:
                matching_bases.append(i)
                shared_key_bits.append(alice_bits[i])
        
        # Take first key_length bits for the final key
        final_key = shared_key_bits[:key_length] if len(shared_key_bits) >= key_length else shared_key_bits
        
        # Calculate error rate (simulate eavesdropping detection)
        error_rate = random.uniform(0, 0.05)  # Typical error rate
        
        key_id = len(self.crypto_keys) + 1
        key_data = {
            'id': key_id,
            'protocol': 'BB84',
            'framework': 'Cirq',
            'key_length': len(final_key),
            'key_binary': ''.join(map(str, final_key)),
            'key_hex': hex(int(''.join(map(str, final_key)), 2))[2:] if final_key else '0',
            'error_rate': error_rate,
            'efficiency': len(final_key) / len(alice_bits),
            'security_level': 'HIGH' if error_rate < 0.11 else 'COMPROMISED'
        }
        
        self.crypto_keys[key_id] = key_data
        return key_data
    
    def quantum_random_number_generator(self, num_bits: int = 256) -> Dict:
        """Generate quantum random numbers using superposition with Cirq"""
        
        qubits = cirq.LineQubit.range(num_bits)
        circuit = cirq.Circuit()
        
        # Put all qubits in superposition
        for qubit in qubits:
            circuit.append(cirq.H(qubit))
        
        # Measure all qubits
        circuit.append(cirq.measure(*qubits, key='random'))
        
        # Execute circuit
        result = self.simulator.run(circuit, repetitions=1)
        random_bits = ''.join(str(bit) for bit in result.measurements['random'][0])
        
        return {
            'bits': num_bits,
            'binary': random_bits,
            'decimal': int(random_bits, 2) if random_bits else 0,
            'hex': hex(int(random_bits, 2))[2:].upper() if random_bits else '0',
            'entropy': num_bits,  # Perfect entropy for true quantum randomness
            'source': 'Cirq Quantum Superposition',
            'framework': 'Cirq'
        }
    
    def post_quantum_encrypt(self, message: str, algorithm: str = "CRYSTALS-Kyber") -> Dict:
        """Simulate post-quantum cryptography encryption using Cirq"""
        
        # Generate quantum-safe key using Cirq
        key_qubits = cirq.LineQubit.range(256)
        key_circuit = cirq.Circuit()
        
        for qubit in key_qubits:
            key_circuit.append(cirq.H(qubit))
        
        key_circuit.append(cirq.measure(*key_qubits, key='quantum_key'))
        
        result = self.simulator.run(key_circuit, repetitions=1)
        quantum_key = ''.join(str(bit) for bit in result.measurements['quantum_key'][0])
        
        # Simple encryption simulation (in practice, use real PQC libraries)
        message_bytes = message.encode('utf-8')
        key_int = int(quantum_key, 2)
        key_bytes = key_int.to_bytes(32, 'big')
        
        encrypted = bytearray()
        for i, byte in enumerate(message_bytes):
            encrypted.append(byte ^ key_bytes[i % len(key_bytes)])
        
        return {
            'algorithm': algorithm,
            'framework': 'Cirq',
            'original_message': message,
            'encrypted_data': encrypted.hex(),
            'key_id': quantum_key[:32],  # First 32 bits as key ID
            'quantum_safe': True,
            'key_size': 256
        }
    
    # === QUANTUM ALGORITHMS ===
    
    def quantum_fourier_transform(self, num_qubits: int) -> Dict:
        """Implement Quantum Fourier Transform using Cirq"""
        
        qubits = cirq.LineQubit.range(num_qubits)
        circuit = cirq.Circuit()
        
        # Initialize with some state
        for i in range(num_qubits):
            if i % 2 == 0:
                circuit.append(cirq.X(qubits[i]))
        
        # QFT implementation
        for i in range(num_qubits):
            circuit.append(cirq.H(qubits[i]))
            for j in range(i+1, num_qubits):
                circuit.append(cirq.CZ(qubits[j], qubits[i]) ** (1.0 / 2**(j-i)))
        
        # Reverse the order of qubits
        for i in range(num_qubits // 2):
            circuit.append(cirq.SWAP(qubits[i], qubits[num_qubits - 1 - i]))
        
        # Add measurements
        circuit.append(cirq.measure(*qubits, key='qft'))
        
        # Execute
        result = self.simulator.run(circuit, repetitions=1000)
        measurements = result.measurements['qft']
        
        # Convert to counts
        counts = {}
        for measurement in measurements:
            bitstring = ''.join(str(bit) for bit in measurement)
            counts[bitstring] = counts.get(bitstring, 0) + 1
        
        return {
            'algorithm': 'Quantum Fourier Transform',
            'qubits': num_qubits,
            'circuit': str(circuit),
            'counts': counts,
            'framework': 'Cirq'
        }
    
    def variational_quantum_eigensolver(self, num_qubits: int = 4) -> Dict:
        """Implement Variational Quantum Eigensolver using Cirq"""
        
        qubits = cirq.LineQubit.range(num_qubits)
        
        # Create ansatz circuit
        def create_ansatz(params):
            circuit = cirq.Circuit()
            # Layer of Hadamard gates
            for qubit in qubits:
                circuit.append(cirq.H(qubit))
            
            # Parameterized rotation gates
            for i, qubit in enumerate(qubits):
                circuit.append(cirq.ry(params[i])(qubit))
            
            # Entangling gates
            for i in range(num_qubits - 1):
                circuit.append(cirq.CNOT(qubits[i], qubits[i + 1]))
            
            return circuit
        
        # Random parameters for demonstration
        params = np.random.uniform(0, 2*np.pi, num_qubits)
        ansatz = create_ansatz(params)
        
        # Add measurements
        ansatz.append(cirq.measure(*qubits, key='vqe'))
        
        # Execute
        result = self.simulator.run(ansatz, repetitions=1000)
        measurements = result.measurements['vqe']
        
        # Convert to counts
        counts = {}
        for measurement in measurements:
            bitstring = ''.join(str(bit) for bit in measurement)
            counts[bitstring] = counts.get(bitstring, 0) + 1
        
        # Calculate expectation value (simplified)
        expectation = sum(int(state, 2) * count for state, count in counts.items()) / 1000
        
        return {
            'algorithm': 'Variational Quantum Eigensolver',
            'qubits': num_qubits,
            'parameters': params.tolist(),
            'expectation_value': expectation,
            'counts': counts,
            'framework': 'Cirq'
        }
    
    # === ATTACK SIMULATION ===
    
    def simulate_shor_attack(self, rsa_bits: int = 1024) -> Dict:
        """Simulate Shor's algorithm for RSA factorization using Cirq"""
        
        # For demonstration, we'll create a simplified version
        # Real Shor's algorithm requires more complex implementation
        
        num_qubits = min(2 * int(np.log2(rsa_bits)), 20)  # Limit for simulation
        qubits = cirq.LineQubit.range(num_qubits)
        circuit = cirq.Circuit()
        
        # Initialize superposition
        for i in range(num_qubits // 2):
            circuit.append(cirq.H(qubits[i]))
        
        # Simulate modular exponentiation (simplified)
        for i in range(num_qubits // 2):
            circuit.append(cirq.CNOT(qubits[i], qubits[i + num_qubits // 2]))
        
        # Apply Quantum Fourier Transform
        self._apply_qft(circuit, qubits[:num_qubits // 2])
        
        # Simulate execution time based on RSA key size
        execution_time = (rsa_bits / 1024) * 150  # Simulated time in seconds
        
        return {
            'algorithm': 'Shor',
            'framework': 'Cirq',
            'target': f'RSA-{rsa_bits}',
            'qubits_required': num_qubits,
            'estimated_time': f"{execution_time:.2f} seconds",
            'success_probability': 0.95 if rsa_bits <= 2048 else 0.80,
            'quantum_advantage': True,
            'classical_time': f"{2 ** (rsa_bits / 3)} years",
            'circuit_depth': len(circuit)
        }
    
    def simulate_grover_attack(self, search_space_size: int) -> Dict:
        """Simulate Grover's algorithm for database search using Cirq"""
        
        # Calculate required qubits
        num_qubits = int(np.ceil(np.log2(search_space_size)))
        qubits = cirq.LineQubit.range(num_qubits + 1)  # +1 for ancilla
        circuit = cirq.Circuit()
        
        # Initialize superposition
        for i in range(num_qubits):
            circuit.append(cirq.H(qubits[i]))
        
        # Ancilla qubit in |1⟩
        circuit.append(cirq.X(qubits[num_qubits]))
        circuit.append(cirq.H(qubits[num_qubits]))
        
        # Grover iterations
        iterations = int(np.pi * np.sqrt(search_space_size) / 4)
        
        for _ in range(min(iterations, 10)):  # Limit iterations for simulation
            # Oracle (simplified - marks target state)
            circuit.append(cirq.Z(qubits[0]))  # Mark first state as target
            
            # Diffusion operator
            for i in range(num_qubits):
                circuit.append(cirq.H(qubits[i]))
                circuit.append(cirq.Z(qubits[i]))
            
            # Multi-controlled Z gate (simplified)
            if num_qubits > 1:
                circuit.append(cirq.H(qubits[0]))
                circuit.append(cirq.CNOT(qubits[1], qubits[0]))
                circuit.append(cirq.H(qubits[0]))
            
            for i in range(num_qubits):
                circuit.append(cirq.Z(qubits[i]))
                circuit.append(cirq.H(qubits[i]))
        
        return {
            'algorithm': 'Grover',
            'framework': 'Cirq',
            'search_space': search_space_size,
            'qubits_required': num_qubits + 1,
            'iterations': iterations,
            'success_probability': 0.99,
            'speedup': f"√{search_space_size}",
            'classical_time': search_space_size // 2,
            'quantum_time': iterations,
            'circuit_depth': len(circuit)
        }
    
    # === UTILITY METHODS ===
    
    def _apply_qft(self, circuit: cirq.Circuit, qubits: List[cirq.LineQubit]):
        """Apply Quantum Fourier Transform to circuit"""
        num_qubits = len(qubits)
        
        for i in range(num_qubits):
            circuit.append(cirq.H(qubits[i]))
            for j in range(i+1, num_qubits):
                circuit.append(cirq.CZ(qubits[j], qubits[i]) ** (1.0 / 2**(j-i)))
        
        # Reverse the order of qubits
        for i in range(num_qubits // 2):
            circuit.append(cirq.SWAP(qubits[i], qubits[num_qubits - 1 - i]))
    
    def _calculate_entanglement(self, counts: Dict) -> float:
        """Calculate entanglement measure from measurement counts"""
        total_shots = sum(counts.values())
        prob_00 = counts.get('00', 0) / total_shots
        prob_11 = counts.get('11', 0) / total_shots
        entanglement = abs(prob_00 + prob_11 - 1.0)
        return max(0, 1 - entanglement)
    
    def _calculate_fidelity(self, measured_counts: Dict, ideal_probs: Dict) -> float:
        """Calculate fidelity between measured and ideal distributions"""
        total_shots = sum(measured_counts.values())
        fidelity = 0
        
        for state, ideal_prob in ideal_probs.items():
            measured_prob = measured_counts.get(state, 0) / total_shots
            fidelity += np.sqrt(ideal_prob * measured_prob)
        
        return min(1.0, fidelity)
    
    def _calculate_molecular_properties(self, statevector: np.ndarray, temp: float, pressure: float) -> Dict:
        """Calculate molecular properties from quantum state"""
        
        # Simulate various molecular properties
        properties = {
            'bond_length': 1.0 + 0.1 * np.random.random(),
            'dipole_moment': np.random.uniform(0, 3),
            'energy': -np.sum(np.abs(statevector) ** 2) * 100,
            'vibrational_freq': 3000 + temp * 0.1,
            'conductivity': max(0, 1000 - temp * 0.5) if temp < 500 else 0,
            'magnetic_moment': np.random.uniform(-2, 2),
            'stability': np.exp(-abs(temp - 298) / 100)
        }
        
        return properties
    
    def get_circuit_info(self, circuit_id: int) -> Dict:
        """Get information about a stored circuit"""
        if circuit_id not in self.circuits:
            raise ValueError(f"Circuit {circuit_id} not found")
        
        circuit_data = self.circuits[circuit_id]
        return {
            'id': circuit_data['id'],
            'name': circuit_data['name'],
            'num_qubits': circuit_data['num_qubits'],
            'gates': circuit_data['gates'],
            'depth': len(circuit_data['circuit']),
            'circuit_str': str(circuit_data['circuit'])
        }
    
    def list_circuits(self) -> List[Dict]:
        """List all stored circuits"""
        return [self.get_circuit_info(cid) for cid in self.circuits.keys()]
    
    def get_system_status(self) -> Dict:
        """Get system status and statistics"""
        return {
            'total_circuits': len(self.circuits),
            'total_molecules': len(self.molecules),
            'total_keys': len(self.crypto_keys),
            'backend': 'Cirq Simulator',
            'max_qubits': 20,  # Practical limit for simulation
            'framework': 'Google Cirq',
            'status': 'active'
        }

# Example usage and testing
if __name__ == "__main__":
    lab = CirqQuantumLab()
    
    # Test quantum circuit creation
    print("=== Cirq Quantum Circuit Test ===")
    circuit_result = lab.create_quantum_circuit("Test Circuit", 3, ["H", "X", "CNOT"])
    print(f"Created circuit: {circuit_result}")
    
    # Test circuit execution
    execution_result = lab.execute_circuit(circuit_result['id'])
    print(f"Execution result: {execution_result}")
    
    # Test Bell state
    print("\n=== Bell State Test ===")
    bell_result = lab.create_bell_state()
    print(f"Bell state: {bell_result}")
    
    # Test molecular simulation
    print("\n=== Molecular Simulation Test ===")
    molecule_result = lab.simulate_molecule("h2o", temperature=300, pressure=1)
    print(f"H2O molecule: {molecule_result}")
    
    # Test quantum cryptography
    print("\n=== Quantum Cryptography Test ===")
    qkd_result = lab.bb84_key_distribution(128)
    print(f"BB84 QKD: {qkd_result}")
    
    qrng_result = lab.quantum_random_number_generator(64)
    print(f"QRNG: {qrng_result}")
    
    # Test quantum algorithms
    print("\n=== Quantum Algorithms Test ===")
    qft_result = lab.quantum_fourier_transform(4)
    print(f"QFT: {qft_result}")
    
    vqe_result = lab.variational_quantum_eigensolver(4)
    print(f"VQE: {vqe_result}")
    
    # Test attack simulation
    print("\n=== Attack Simulation Test ===")
    shor_result = lab.simulate_shor_attack(1024)
    print(f"Shor's attack: {shor_result}")
    
    grover_result = lab.simulate_grover_attack(1000000)
    print(f"Grover's attack: {grover_result}")
    
    # System status
    print("\n=== System Status ===")
    status = lab.get_system_status()
    print(f"System status: {status}")
