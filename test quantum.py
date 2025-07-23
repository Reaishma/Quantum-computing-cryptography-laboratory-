
#!/usr/bin/env python3
"""
Test script for quantum circuit implementations
Run with: python test_quantum.py
"""

from quantum_circuits import QuantumCircuitImplementations
import numpy as np

def main():
    print("Testing Quantum Circuit Implementations")
    print("=" * 50)
    
    # Initialize quantum implementations
    quantum = QuantumCircuitImplementations()
    
    print("\n1. Testing Qiskit Basic Gates...")
    try:
        qc, counts = quantum.qiskit_basic_gates()
        print(f"✓ Success! Results: {counts}")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    print("\n2. Testing Qiskit Bell State...")
    try:
        qc, counts = quantum.qiskit_bell_state()
        print(f"✓ Success! Results: {counts}")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    print("\n3. Testing Cirq Basic Gates...")
    try:
        circuit, result = quantum.cirq_basic_gates()
        print(f"✓ Success! Histogram: {result.histogram(key='q0')}")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    print("\n4. Testing Cirq Bell State...")
    try:
        circuit, result = quantum.cirq_bell_state()
        print(f"✓ Success! Histogram: {result.histogram(key='q0')}")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    print("\n5. Testing Grover's Algorithm (Qiskit)...")
    try:
        qc, counts = quantum.qiskit_grover_search(target_item=2)
        print(f"✓ Success! Results: {counts}")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    print("\n6. Testing Quantum Fourier Transform (Qiskit)...")
    try:
        qc = quantum.qiskit_qft(num_qubits=3)
        print("✓ Success! QFT circuit created")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    print("\n7. Testing Quantum Teleportation (Cirq)...")
    try:
        circuit, result = quantum.cirq_quantum_teleportation()
        print(f"✓ Success! Teleportation result: {result.histogram(key='bob_final')}")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    print("\n" + "=" * 50)
    print("All tests completed!")

if __name__ == "__main__":
    main()
