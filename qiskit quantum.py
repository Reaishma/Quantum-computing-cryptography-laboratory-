
from qiskit import QuantumCircuit, transpile, Aer, execute
from qiskit.quantum_info import Statevector, DensityMatrix, entropy
from qiskit.providers.aer import AerSimulator
from qiskit.algorithms import VQE, QAOA
from qiskit.circuit.library import TwoLocal
from qiskit.opflow import PauliSumOp
import numpy as np
from typing import List, Tuple, Dict, Any
import random

class QiskitQuantumLab:
    def __init__(self):
        self.simulator = AerSimulator()
        self.backend = Aer.get_backend('qasm_simulator')
        
    def create_bell_state(self) -> Tuple[int, int]:
        """Create and measure a Bell state using Qiskit"""
        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure_all()
        
        job = execute(qc, self.backend, shots=1)
        result = job.result()
        counts = result.get_counts(qc)
        
        measurement = list(counts.keys())[0]
        return (int(measurement[1]), int(measurement[0]))
    
    def execute_quantum_circuit(self, gates: List[str]) -> List[int]:
        """Execute quantum circuit with given gates"""
        qc = QuantumCircuit(3, 3)
        
        for gate in gates:
            if gate == "H":
                qc.h(0)
            elif gate == "X":
                qc.x(0)
            elif gate == "Y":
                qc.y(0)
            elif gate == "Z":
                qc.z(0)
            elif gate == "CNOT":
                qc.cx(0, 1)
            elif gate == "RZ":
                qc.rz(np.pi/4, 0)
            elif gate == "RY":
                qc.ry(np.pi/4, 0)
        
        qc.measure_all()
        
        job = execute(qc, self.backend, shots=1)
        result = job.result()
        counts = result.get_counts(qc)
        
        if counts:
            measurement = list(counts.keys())[0]
            return [int(bit) for bit in reversed(measurement)]
        return [0, 0, 0]
    
    def measure_entanglement(self) -> float:
        """Measure quantum entanglement using Qiskit"""
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0, 1)
        
        statevector = Statevector.from_instruction(qc)
        dm = DensityMatrix(statevector)
        
        # Calculate von Neumann entropy for entanglement measure
        rho_a = dm.partial_trace([1])
        entanglement = entropy(rho_a, base=2)
        
        return float(entanglement)
    
    def calculate_fidelity(self, iterations: int = 100) -> float:
        """Calculate quantum state fidelity"""
        qc = QuantumCircuit(1)
        qc.ry(np.pi/4, 0)
        
        statevector1 = Statevector.from_instruction(qc)
        
        qc2 = QuantumCircuit(1)
        qc2.ry(np.pi/4 + 0.1, 0)  # Slightly different angle
        
        statevector2 = Statevector.from_instruction(qc2)
        
        fidelity = np.abs(statevector1.inner(statevector2))**2
        return float(fidelity)
    
    def bb84_key_distribution(self, key_length: int) -> Tuple[List[bool], float]:
        """Implement BB84 protocol using Qiskit"""
        shared_key = []
        errors = 0
        
        for _ in range(key_length * 2):  # Generate more bits to account for basis mismatch
            # Alice's preparation
            alice_bit = random.choice([0, 1])
            alice_basis = random.choice([0, 1])  # 0: Z basis, 1: X basis
            
            qc = QuantumCircuit(1, 1)
            
            if alice_bit == 1:
                qc.x(0)
            
            if alice_basis == 1:
                qc.h(0)
            
            # Bob's measurement
            bob_basis = random.choice([0, 1])
            
            if bob_basis == 1:
                qc.h(0)
            
            qc.measure(0, 0)
            
            job = execute(qc, self.backend, shots=1)
            result = job.result()
            counts = result.get_counts(qc)
            bob_result = int(list(counts.keys())[0])
            
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
        """Generate quantum random numbers using Qiskit"""
        qc = QuantumCircuit(num_bits, num_bits)
        
        for i in range(num_bits):
            qc.h(i)
            qc.measure(i, i)
        
        job = execute(qc, self.backend, shots=1)
        result = job.result()
        counts = result.get_counts(qc)
        
        if counts:
            binary = list(counts.keys())[0]
            decimal = int(binary, 2)
            hex_val = hex(decimal)[2:].upper()
            
            return {
                'binary': binary,
                'decimal': decimal,
                'hex': hex_val
            }
        
        return {'binary': '0', 'decimal': 0, 'hex': '0'}
    
    def vqe_simulation(self, molecule: str) -> Dict[str, float]:
        """Variational Quantum Eigensolver simulation"""
        # Simple Hamiltonian for demonstration
        if molecule == "H2":
            # Simplified H2 Hamiltonian
            from qiskit.opflow import I, X, Y, Z
            H = -1.0523732 * (I ^ I) - 0.39793742 * (I ^ Z) - 0.39793742 * (Z ^ I) \
                - 0.01128010 * (Z ^ Z) + 0.18093119 * (X ^ X)
        else:
            # Default simple Hamiltonian
            from qiskit.opflow import Z
            H = Z ^ Z
        
        # Create ansatz
        ansatz = TwoLocal(2, 'ry', 'cz', reps=1)
        
        # Use classical optimizer
        from qiskit.algorithms.optimizers import COBYLA
        optimizer = COBYLA(maxiter=100)
        
        # VQE
        vqe = VQE(ansatz, optimizer, quantum_instance=self.backend)
        result = vqe.compute_minimum_eigenvalue(H)
        
        return {
            'ground_state_energy': float(result.eigenvalue.real),
            'optimal_parameters': result.optimal_parameters.tolist() if result.optimal_parameters is not None else [],
            'convergence': bool(result.optimizer_result.success if hasattr(result, 'optimizer_result') else True)
        }
    
    def quantum_fourier_transform(self, n_qubits: int) -> str:
        """Implement Quantum Fourier Transform"""
        qc = QuantumCircuit(n_qubits)
        
        def qft_rotations(circuit, n):
            if n == 0:
                return circuit
            n -= 1
            circuit.h(n)
            for qubit in range(n):
                circuit.cp(np.pi/2**(n-qubit), qubit, n)
            qft_rotations(circuit, n)
        
        qft_rotations(qc, n_qubits)
        
        # Swap qubits
        for qubit in range(n_qubits//2):
            qc.swap(qubit, n_qubits-qubit-1)
        
        return str(qc)
    
    def grovers_algorithm(self, n_qubits: int, marked_item: int) -> Dict[str, Any]:
        """Implement Grover's search algorithm"""
        qc = QuantumCircuit(n_qubits, n_qubits)
        
        # Initialize superposition
        qc.h(range(n_qubits))
        
        # Number of iterations
        iterations = int(np.pi/4 * np.sqrt(2**n_qubits))
        
        for _ in range(iterations):
            # Oracle for marked item
            if marked_item < 2**n_qubits:
                binary_marked = format(marked_item, f'0{n_qubits}b')
                for i, bit in enumerate(binary_marked):
                    if bit == '0':
                        qc.x(i)
                
                qc.mcp(np.pi, list(range(n_qubits-1)), n_qubits-1)
                
                for i, bit in enumerate(binary_marked):
                    if bit == '0':
                        qc.x(i)
            
            # Diffusion operator
            qc.h(range(n_qubits))
            qc.x(range(n_qubits))
            qc.mcp(np.pi, list(range(n_qubits-1)), n_qubits-1)
            qc.x(range(n_qubits))
            qc.h(range(n_qubits))
        
        qc.measure_all()
        
        job = execute(qc, self.backend, shots=1024)
        result = job.result()
        counts = result.get_counts(qc)
        
        most_likely = max(counts, key=counts.get)
        probability = counts[most_likely] / 1024
        
        return {
            'found_item': int(most_likely, 2),
            'probability': probability,
            'iterations_used': iterations,
            'all_results': dict(counts)
        }

# Global Qiskit interface
qiskit_lab = QiskitQuantumLab()
