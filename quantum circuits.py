
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile, Aer, execute
from qiskit.visualization import plot_histogram
import cirq
import matplotlib.pyplot as plt

class QuantumCircuitImplementations:
    """Quantum circuit implementations using Qiskit and Cirq"""
    
    def __init__(self):
        self.simulator = Aer.get_backend('qasm_simulator')
        
    # Qiskit Implementations
    def qiskit_basic_gates(self):
        """Basic quantum gates using Qiskit"""
        # Create quantum circuit with 2 qubits and 2 classical bits
        qc = QuantumCircuit(2, 2)
        
        # Add gates
        qc.h(0)  # Hadamard gate on qubit 0
        qc.x(1)  # Pauli-X gate on qubit 1
        qc.cx(0, 1)  # CNOT gate
        qc.rz(np.pi/4, 0)  # RZ rotation
        qc.ry(np.pi/3, 1)  # RY rotation
        
        # Measure
        qc.measure([0, 1], [0, 1])
        
        print("Qiskit Basic Gates Circuit:")
        print(qc)
        
        # Execute circuit
        job = execute(qc, self.simulator, shots=1000)
        result = job.result()
        counts = result.get_counts(qc)
        
        return qc, counts
    
    def qiskit_bell_state(self):
        """Create Bell state using Qiskit"""
        qc = QuantumCircuit(2, 2)
        
        # Create Bell state |00⟩ + |11⟩
        qc.h(0)
        qc.cx(0, 1)
        qc.measure_all()
        
        print("\nQiskit Bell State Circuit:")
        print(qc)
        
        job = execute(qc, self.simulator, shots=1000)
        result = job.result()
        counts = result.get_counts(qc)
        
        return qc, counts
    
    def qiskit_grover_search(self, target_item=3, num_qubits=2):
        """Grover's algorithm implementation using Qiskit"""
        qc = QuantumCircuit(num_qubits, num_qubits)
        
        # Initialize superposition
        for qubit in range(num_qubits):
            qc.h(qubit)
        
        # Oracle for target item (simplified)
        if target_item == 3:  # |11⟩ state
            qc.cz(0, 1)
        elif target_item == 2:  # |10⟩ state
            qc.x(1)
            qc.cz(0, 1)
            qc.x(1)
        elif target_item == 1:  # |01⟩ state
            qc.x(0)
            qc.cz(0, 1)
            qc.x(0)
        
        # Diffusion operator
        for qubit in range(num_qubits):
            qc.h(qubit)
            qc.x(qubit)
        
        qc.cz(0, 1)
        
        for qubit in range(num_qubits):
            qc.x(qubit)
            qc.h(qubit)
        
        qc.measure_all()
        
        print(f"\nQiskit Grover's Algorithm (target: {target_item}):")
        print(qc)
        
        job = execute(qc, self.simulator, shots=1000)
        result = job.result()
        counts = result.get_counts(qc)
        
        return qc, counts
    
    def qiskit_qft(self, num_qubits=3):
        """Quantum Fourier Transform using Qiskit"""
        qc = QuantumCircuit(num_qubits)
        
        def qft_rotations(circuit, n):
            if n == 0:
                return circuit
            n -= 1
            circuit.h(n)
            for qubit in range(n):
                circuit.cp(np.pi/2**(n-qubit), qubit, n)
            qft_rotations(circuit, n)
        
        qft_rotations(qc, num_qubits)
        
        # Swap qubits
        for qubit in range(num_qubits//2):
            qc.swap(qubit, num_qubits-qubit-1)
        
        print(f"\nQiskit Quantum Fourier Transform ({num_qubits} qubits):")
        print(qc)
        
        return qc
    
    # Cirq Implementations
    def cirq_basic_gates(self):
        """Basic quantum gates using Cirq"""
        # Create qubits
        q0, q1 = cirq.LineQubit.range(2)
        
        # Create circuit
        circuit = cirq.Circuit()
        
        # Add gates
        circuit.append([
            cirq.H(q0),  # Hadamard
            cirq.X(q1),  # Pauli-X
            cirq.CNOT(q0, q1),  # CNOT
            cirq.rz(np.pi/4)(q0),  # RZ rotation
            cirq.ry(np.pi/3)(q1),  # RY rotation
        ])
        
        # Add measurements
        circuit.append([
            cirq.measure(q0, key='q0'),
            cirq.measure(q1, key='q1')
        ])
        
        print("\nCirq Basic Gates Circuit:")
        print(circuit)
        
        # Simulate
        simulator = cirq.Simulator()
        result = simulator.run(circuit, repetitions=1000)
        
        return circuit, result
    
    def cirq_bell_state(self):
        """Create Bell state using Cirq"""
        q0, q1 = cirq.LineQubit.range(2)
        
        circuit = cirq.Circuit()
        circuit.append([
            cirq.H(q0),
            cirq.CNOT(q0, q1),
            cirq.measure(q0, key='q0'),
            cirq.measure(q1, key='q1')
        ])
        
        print("\nCirq Bell State Circuit:")
        print(circuit)
        
        simulator = cirq.Simulator()
        result = simulator.run(circuit, repetitions=1000)
        
        return circuit, result
    
    def cirq_grover_search(self, target_item=3):
        """Grover's algorithm using Cirq"""
        q0, q1 = cirq.LineQubit.range(2)
        
        circuit = cirq.Circuit()
        
        # Initialize superposition
        circuit.append([cirq.H(q0), cirq.H(q1)])
        
        # Oracle
        if target_item == 3:  # |11⟩
            circuit.append(cirq.CZ(q0, q1))
        elif target_item == 2:  # |10⟩
            circuit.append([cirq.X(q1), cirq.CZ(q0, q1), cirq.X(q1)])
        elif target_item == 1:  # |01⟩
            circuit.append([cirq.X(q0), cirq.CZ(q0, q1), cirq.X(q0)])
        
        # Diffusion operator
        circuit.append([
            cirq.H(q0), cirq.H(q1),
            cirq.X(q0), cirq.X(q1),
            cirq.CZ(q0, q1),
            cirq.X(q0), cirq.X(q1),
            cirq.H(q0), cirq.H(q1)
        ])
        
        # Measure
        circuit.append([
            cirq.measure(q0, key='q0'),
            cirq.measure(q1, key='q1')
        ])
        
        print(f"\nCirq Grover's Algorithm (target: {target_item}):")
        print(circuit)
        
        simulator = cirq.Simulator()
        result = simulator.run(circuit, repetitions=1000)
        
        return circuit, result
    
    def cirq_quantum_teleportation(self):
        """Quantum teleportation protocol using Cirq"""
        # Alice's qubit, entangled pair
        alice_qubit = cirq.LineQubit(0)
        alice_ancilla = cirq.LineQubit(1)
        bob_qubit = cirq.LineQubit(2)
        
        circuit = cirq.Circuit()
        
        # Prepare state to teleport (|+⟩ state)
        circuit.append(cirq.H(alice_qubit))
        
        # Create entangled pair
        circuit.append([
            cirq.H(alice_ancilla),
            cirq.CNOT(alice_ancilla, bob_qubit)
        ])
        
        # Alice's measurements
        circuit.append([
            cirq.CNOT(alice_qubit, alice_ancilla),
            cirq.H(alice_qubit),
            cirq.measure(alice_qubit, key='alice_x'),
            cirq.measure(alice_ancilla, key='alice_z')
        ])
        
        # Bob's corrections (simplified - would be conditional in real implementation)
        circuit.append([
            cirq.measure(bob_qubit, key='bob_final')
        ])
        
        print("\nCirq Quantum Teleportation:")
        print(circuit)
        
        simulator = cirq.Simulator()
        result = simulator.run(circuit, repetitions=100)
        
        return circuit, result
    
    def run_all_examples(self):
        """Run all quantum circuit examples"""
        print("=" * 60)
        print("QUANTUM CIRCUIT IMPLEMENTATIONS")
        print("=" * 60)
        
        # Qiskit examples
        qiskit_basic_qc, qiskit_basic_counts = self.qiskit_basic_gates()
        print(f"Qiskit Basic Gates Results: {qiskit_basic_counts}")
        
        qiskit_bell_qc, qiskit_bell_counts = self.qiskit_bell_state()
        print(f"Qiskit Bell State Results: {qiskit_bell_counts}")
        
        qiskit_grover_qc, qiskit_grover_counts = self.qiskit_grover_search()
        print(f"Qiskit Grover Results: {qiskit_grover_counts}")
        
        qiskit_qft_qc = self.qiskit_qft()
        
        # Cirq examples
        cirq_basic_circuit, cirq_basic_result = self.cirq_basic_gates()
        print(f"Cirq Basic Gates Results: {cirq_basic_result.histogram(key='q0')}")
        
        cirq_bell_circuit, cirq_bell_result = self.cirq_bell_state()
        print(f"Cirq Bell State Results: {cirq_bell_result.histogram(key='q0')}")
        
        cirq_grover_circuit, cirq_grover_result = self.cirq_grover_search()
        print(f"Cirq Grover Results: {cirq_grover_result.histogram(key='q0')}")
        
        cirq_teleport_circuit, cirq_teleport_result = self.cirq_quantum_teleportation()
        print(f"Cirq Teleportation Results: {cirq_teleport_result.histogram(key='bob_final')}")

if __name__ == "__main__":
    quantum_impl = QuantumCircuitImplementations()
    quantum_impl.run_all_examples()
