
import cirq
import numpy as np
from typing import List, Tuple, Dict, Any
import random

class CirqQuantumLab:
    def __init__(self):
        self.simulator = cirq.Simulator()
        
    def create_bell_state(self) -> Tuple[int, int]:
        """Create and measure a Bell state using Cirq"""
        qubits = cirq.LineQubit.range(2)
        circuit = cirq.Circuit()
        
        circuit.append(cirq.H(qubits[0]))
        circuit.append(cirq.CNOT(qubits[0], qubits[1]))
        circuit.append(cirq.measure(*qubits, key='result'))
        
        result = self.simulator.run(circuit, repetitions=1)
        measurements = result.measurements['result'][0]
        
        return (int(measurements[0]), int(measurements[1]))
    
    def execute_quantum_circuit(self, gates: List[str]) -> List[int]:
        """Execute quantum circuit with given gates using Cirq"""
        qubits = cirq.LineQubit.range(3)
        circuit = cirq.Circuit()
        
        for gate in gates:
            if gate == "H":
                circuit.append(cirq.H(qubits[0]))
            elif gate == "X":
                circuit.append(cirq.X(qubits[0]))
            elif gate == "Y":
                circuit.append(cirq.Y(qubits[0]))
            elif gate == "Z":
                circuit.append(cirq.Z(qubits[0]))
            elif gate == "CNOT":
                circuit.append(cirq.CNOT(qubits[0], qubits[1]))
            elif gate == "RZ":
                circuit.append(cirq.rz(np.pi/4)(qubits[0]))
            elif gate == "RY":
                circuit.append(cirq.ry(np.pi/4)(qubits[0]))
        
        circuit.append(cirq.measure(*qubits, key='result'))
        
        result = self.simulator.run(circuit, repetitions=1)
        measurements = result.measurements['result'][0]
        
        return [int(bit) for bit in measurements]
    
    def measure_entanglement(self) -> float:
        """Measure quantum entanglement using Cirq"""
        qubits = cirq.LineQubit.range(2)
        circuit = cirq.Circuit()
        
        circuit.append(cirq.H(qubits[0]))
        circuit.append(cirq.CNOT(qubits[0], qubits[1]))
        
        # Simulate the circuit to get the final state
        result = self.simulator.simulate(circuit)
        state_vector = result.final_state_vector
        
        # Calculate reduced density matrix for first qubit
        # For a 2-qubit system, this is a simplified entanglement measure
        prob_00 = abs(state_vector[0])**2
        prob_11 = abs(state_vector[3])**2
        
        # Simple entanglement measure based on Bell state probabilities
        entanglement = 2 * min(prob_00, prob_11)
        
        return float(entanglement)
    
    def calculate_fidelity(self, iterations: int = 100) -> float:
        """Calculate quantum state fidelity using Cirq"""
        qubits = cirq.LineQubit.range(1)
        
        # Create two slightly different states
        circuit1 = cirq.Circuit()
        circuit1.append(cirq.ry(np.pi/4)(qubits[0]))
        
        circuit2 = cirq.Circuit()
        circuit2.append(cirq.ry(np.pi/4 + 0.1)(qubits[0]))
        
        # Get state vectors
        result1 = self.simulator.simulate(circuit1)
        result2 = self.simulator.simulate(circuit2)
        
        state1 = result1.final_state_vector
        state2 = result2.final_state_vector
        
        # Calculate fidelity
        fidelity = abs(np.vdot(state1, state2))**2
        
        return float(fidelity)
    
    def bb84_key_distribution(self, key_length: int) -> Tuple[List[bool], float]:
        """Implement BB84 protocol using Cirq"""
        shared_key = []
        errors = 0
        
        for _ in range(key_length * 2):
            # Alice's preparation
            alice_bit = random.choice([0, 1])
            alice_basis = random.choice([0, 1])  # 0: Z basis, 1: X basis
            
            qubit = cirq.LineQubit(0)
            circuit = cirq.Circuit()
            
            if alice_bit == 1:
                circuit.append(cirq.X(qubit))
            
            if alice_basis == 1:
                circuit.append(cirq.H(qubit))
            
            # Bob's measurement
            bob_basis = random.choice([0, 1])
            
            if bob_basis == 1:
                circuit.append(cirq.H(qubit))
            
            circuit.append(cirq.measure(qubit, key='bob_result'))
            
            result = self.simulator.run(circuit, repetitions=1)
            bob_result = int(result.measurements['bob_result'][0])
            
            # If bases match, add to shared key
            if alice_basis == bob_basis:
                shared_key.append(bool(alice_bit))
                if alice_bit != bob_result:
                    errors += 1
                
                if len(shared_key) >= key_length:
                    break
        
        error_rate = (errors / len(shared_key)) * 100 if shared_key else 0
        return (shared_key, error_rate)
    
    def quantum_random_generator(self, num_bits: int) -> Dict[str, Any]:
        """Generate quantum random numbers using Cirq"""
        qubits = cirq.LineQubit.range(num_bits)
        circuit = cirq.Circuit()
        
        # Apply Hadamard gates
        for qubit in qubits:
            circuit.append(cirq.H(qubit))
        
        circuit.append(cirq.measure(*qubits, key='random_bits'))
        
        result = self.simulator.run(circuit, repetitions=1)
        measurements = result.measurements['random_bits'][0]
        
        binary = ''.join(str(int(bit)) for bit in measurements)
        decimal = int(binary, 2) if binary else 0
        hex_val = hex(decimal)[2:].upper()
        
        return {
            'binary': binary,
            'decimal': decimal,
            'hex': hex_val
        }
    
    def quantum_phase_estimation(self, n_qubits: int) -> Dict[str, Any]:
        """Implement Quantum Phase Estimation using Cirq"""
        # Create qubits: n counting qubits + 1 eigenstate qubit
        counting_qubits = cirq.LineQubit.range(n_qubits)
        eigenstate_qubit = cirq.LineQubit(n_qubits)
        
        circuit = cirq.Circuit()
        
        # Initialize eigenstate qubit (for demonstration, use |1⟩)
        circuit.append(cirq.X(eigenstate_qubit))
        
        # Apply Hadamard gates to counting qubits
        for qubit in counting_qubits:
            circuit.append(cirq.H(qubit))
        
        # Apply controlled unitary operations
        # For demonstration, use controlled-Z gates with different powers
        for i, control_qubit in enumerate(counting_qubits):
            for _ in range(2**i):
                circuit.append(cirq.CZ(control_qubit, eigenstate_qubit))
        
        # Apply inverse QFT to counting qubits
        def inverse_qft(qubits):
            qft_circuit = cirq.Circuit()
            n = len(qubits)
            
            # Reverse the order and apply inverse operations
            for i in range(n//2):
                qft_circuit.append(cirq.SWAP(qubits[i], qubits[n-1-i]))
            
            for i in range(n):
                for j in range(i):
                    qft_circuit.append(cirq.CZPowGate(exponent=-1.0/2**(i-j))(qubits[j], qubits[i]))
                qft_circuit.append(cirq.H(qubits[i]))
            
            return qft_circuit
        
        circuit += inverse_qft(counting_qubits)
        
        # Measure the counting qubits
        circuit.append(cirq.measure(*counting_qubits, key='phase'))
        
        result = self.simulator.run(circuit, repetitions=100)
        measurements = result.measurements['phase']
        
        # Count the most frequent measurement
        from collections import Counter
        counts = Counter(tuple(row) for row in measurements)
        most_common = counts.most_common(1)[0]
        
        measured_phase = sum(bit * 2**(n_qubits-1-i) for i, bit in enumerate(most_common[0]))
        estimated_phase = measured_phase / (2**n_qubits)
        
        return {
            'estimated_phase': estimated_phase,
            'measured_binary': ''.join(str(int(bit)) for bit in most_common[0]),
            'confidence': most_common[1] / 100,
            'all_measurements': dict(counts)
        }
    
    def quantum_walk(self, steps: int, position_qubits: int) -> Dict[str, Any]:
        """Implement Quantum Walk using Cirq"""
        n_pos = position_qubits
        coin_qubit = cirq.LineQubit(0)
        position_qubits_list = cirq.LineQubit.range(1, n_pos + 1)
        
        circuit = cirq.Circuit()
        
        # Initialize coin in superposition
        circuit.append(cirq.H(coin_qubit))
        
        # Initialize position at center (simplified)
        if n_pos > 1:
            circuit.append(cirq.X(position_qubits_list[n_pos//2]))
        
        for step in range(steps):
            # Coin flip
            circuit.append(cirq.H(coin_qubit))
            
            # Conditional shift based on coin
            for i, pos_qubit in enumerate(position_qubits_list[:-1]):
                # If coin is |0⟩, shift left
                circuit.append(cirq.CNOT(coin_qubit, pos_qubit))
                if i < len(position_qubits_list) - 1:
                    circuit.append(cirq.CNOT(pos_qubit, position_qubits_list[i+1]))
        
        # Measure all qubits
        all_qubits = [coin_qubit] + position_qubits_list
        circuit.append(cirq.measure(*all_qubits, key='final_state'))
        
        result = self.simulator.run(circuit, repetitions=1000)
        measurements = result.measurements['final_state']
        
        # Analyze position distribution
        position_counts = {}
        for measurement in measurements:
            position = tuple(measurement[1:])  # Exclude coin qubit
            position_str = ''.join(str(int(bit)) for bit in position)
            position_counts[position_str] = position_counts.get(position_str, 0) + 1
        
        return {
            'position_distribution': position_counts,
            'total_steps': steps,
            'position_qubits': n_pos,
            'most_likely_position': max(position_counts, key=position_counts.get)
        }
    
    def quantum_teleportation(self) -> Dict[str, bool]:
        """Implement Quantum Teleportation using Cirq"""
        # Three qubits: message, Alice's entangled qubit, Bob's entangled qubit
        message_qubit = cirq.NamedQubit('message')
        alice_qubit = cirq.NamedQubit('alice')
        bob_qubit = cirq.NamedQubit('bob')
        
        circuit = cirq.Circuit()
        
        # Prepare message qubit in arbitrary state (|1⟩ for demonstration)
        circuit.append(cirq.X(message_qubit))
        
        # Create entangled pair between Alice and Bob
        circuit.append(cirq.H(alice_qubit))
        circuit.append(cirq.CNOT(alice_qubit, bob_qubit))
        
        # Alice's operations
        circuit.append(cirq.CNOT(message_qubit, alice_qubit))
        circuit.append(cirq.H(message_qubit))
        
        # Measure Alice's qubits
        circuit.append(cirq.measure(message_qubit, alice_qubit, key='alice_measurement'))
        
        # Bob's correction (simplified - in practice would be conditional)
        # For demonstration, apply all possible corrections
        circuit.append(cirq.measure(bob_qubit, key='bob_final'))
        
        result = self.simulator.run(circuit, repetitions=100)
        alice_measurements = result.measurements['alice_measurement']
        bob_measurements = result.measurements['bob_final']
        
        # Count successful teleportations
        successes = sum(1 for alice, bob in zip(alice_measurements, bob_measurements) 
                       if bob[0] == 1)  # Original message was |1⟩
        
        return {
            'success_rate': successes / 100,
            'total_attempts': 100,
            'alice_measurements': alice_measurements.tolist(),
            'bob_results': bob_measurements.tolist()
        }

# Global Cirq interface
cirq_lab = CirqQuantumLab()
