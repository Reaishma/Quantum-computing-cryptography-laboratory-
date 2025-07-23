
# Quantum Computing Laboratory with Qiskit & Cirq

A comprehensive quantum computing laboratory implementing quantum algorithms, simulations, and cryptography protocols using **Qiskit** and **Cirq** - the industry-standard quantum computing frameworks.

## 🚀 Features

### Quantum Frameworks
- **Qiskit Integration**: IBM's quantum computing framework for advanced quantum algorithms
- **Cirq Integration**: Google's quantum computing framework for quantum circuits and simulations
- **Automatic Backend Selection**: Seamlessly switches between available frameworks

### Quantum Simulation (Qiskit)
- **Quantum Circuit Builder**: Create and execute quantum circuits with various gates (H, X, Y, Z, CNOT, RZ, RY)
- **Bell State Generation**: Create and measure entangled Bell states
- **Variational Quantum Eigensolver (VQE)**: Molecular ground state energy calculations
- **Grover's Search Algorithm**: Quantum database search with quadratic speedup
- **Quantum Fourier Transform**: Essential quantum algorithm implementation

### Quantum Simulation (Cirq)
- **Quantum Phase Estimation**: Estimate eigenvalues of unitary operators
- **Quantum Walk**: Quantum random walk simulations
- **Quantum Teleportation**: Demonstrate quantum information transfer
- **Advanced Circuit Simulations**: Complex quantum state manipulations

### Quantum Cryptography
- **BB84 Quantum Key Distribution**: Secure key exchange using quantum mechanics
- **Quantum Random Number Generator**: True randomness from quantum measurements
- **Quantum Digital Signatures**: Cryptographic signatures using quantum protocols
- **Post-Quantum Cryptography**: Future-proof encryption algorithms

### Advanced Features
- **Quantum State Analysis**: Entanglement measurement and fidelity calculations
- **Real-time Visualization**: Interactive quantum state and circuit visualization
- **Molecular Simulation**: Quantum chemistry calculations for small molecules
- **Error Analysis**: Quantum error rates and decoherence studies

## 🛠️ Technology Stack

### Quantum Computing Frameworks
- **Qiskit**: IBM's open-source quantum computing framework
- **Cirq**: Google's Python library for quantum circuits
- **NumPy**: Numerical computing for quantum state mathematics

### Backend Technologies
- **Python 3.10+**: Core programming language
- **Flask**: Web server for quantum API endpoints
- **Aer Simulator**: Qiskit's quantum circuit simulator
- **Cirq Simulator**: Google's quantum state simulator

### Frontend Technologies  
- **Vue.js 3**: Reactive frontend framework
- **HTML5 Canvas**: Quantum state visualization
- **CSS3**: Modern styling with quantum-themed gradients

## 📦 Installation & Setup

### Prerequisites
- **Python 3.10+**
- **pip** package manager

### Install Quantum Computing Packages
```bash
pip install qiskit qiskit-aer cirq numpy flask
```

### Run the Quantum Laboratory
```bash
python quantum_server.py
```

The application will be available at `http://localhost:5000`

## 🔬 Quantum Algorithms Implemented

### Qiskit Algorithms
1. **Variational Quantum Eigensolver (VQE)**
   - Hybrid quantum-classical algorithm for finding ground state energies
   - Molecular simulation capabilities (H2, LiH, etc.)
   - Parameterized quantum circuits optimization

2. **Grover's Search Algorithm**
   - Quadratic speedup for database search
   - Configurable search space and marked items
   - Success probability analysis

3. **Quantum Fourier Transform**
   - Foundation for many quantum algorithms
   - Period finding applications
   - Phase estimation subroutines

### Cirq Algorithms
1. **Quantum Phase Estimation**
   - Estimates phases of quantum operators
   - High-precision eigenvalue calculations
   - Applications in quantum chemistry

2. **Quantum Teleportation**
   - Demonstrates quantum information transfer
   - Bell state preparation and measurement
   - Classical communication requirements

3. **Quantum Walk**
   - Quantum analogue of classical random walks
   - Faster mixing times and search capabilities
   - Position distribution analysis

## 🏗️ Project Structure

```
quantum-computing-lab/
├── qiskit_quantum.py           # Qiskit quantum algorithms
├── cirq_quantum.py             # Cirq quantum implementations  
├── quantum_interface.py        # Unified quantum backend interface
├── quantum_server.py           # Flask web server
├── QuantumCryptography.qs      # Legacy Q# cryptography (deprecated)
├── QuantumSimulation.qs        # Legacy Q# simulation (deprecated)
├── QuantumMaterials.qs         # Legacy Q# materials (deprecated)
└── README.md                   # This documentation
```

## 🔧 API Endpoints

### Quantum Circuit Operations
- `GET /api/bell_state` - Create Bell state pairs
- `POST /api/execute_circuit` - Execute custom quantum circuits
- `GET /api/entanglement` - Measure quantum entanglement
- `GET /api/fidelity` - Calculate quantum state fidelity

### Quantum Cryptography
- `POST /api/bb84` - BB84 quantum key distribution
- `POST /api/qrng` - Quantum random number generation
- `POST /api/quantum_sign` - Quantum digital signatures

### Advanced Algorithms (Qiskit)
- `POST /api/vqe_simulation` - Variational quantum eigensolver
- `POST /api/grovers_search` - Grover's search algorithm
- `POST /api/qft` - Quantum Fourier transform

### Advanced Algorithms (Cirq)  
- `POST /api/phase_estimation` - Quantum phase estimation
- `POST /api/quantum_teleportation` - Quantum teleportation
- `POST /api/quantum_walk` - Quantum walk simulation

## 🎯 Usage Examples

### Running VQE for H2 Molecule (Qiskit)
```python
from qiskit_quantum import qiskit_lab

result = qiskit_lab.vqe_simulation("H2")
print(f"Ground state energy: {result['ground_state_energy']} Hartree")
```

### Quantum Phase Estimation (Cirq)
```python
from cirq_quantum import cirq_lab

result = cirq_lab.quantum_phase_estimation(n_qubits=4)
print(f"Estimated phase: {result['estimated_phase']}")
```

### BB84 Quantum Key Distribution
```python
from quantum_interface import quantum_interface

shared_key, error_rate = quantum_interface.bb84_key_distribution(256)
print(f"Generated {len(shared_key)} bit key with {error_rate:.2f}% error rate")
```

## 📈 Quantum Advantages Demonstrated

1. **Quantum Parallelism**: Superposition enables parallel computation
2. **Quantum Entanglement**: Non-local correlations for cryptography
3. **Quantum Interference**: Amplitude amplification in search algorithms
4. **Quantum Speedup**: Exponential advantages for specific problems

## 🔐 Security Features

- **Quantum Key Distribution**: Information-theoretic security
- **Quantum Random Numbers**: True randomness from quantum measurements
- **Post-Quantum Cryptography**: Resistance to quantum attacks
- **Quantum Digital Signatures**: Unforgeable quantum authentication

## 📚 Educational Content

### Quantum Computing Concepts
- **Qubits and Superposition**: Fundamental quantum information units
- **Quantum Gates**: Building blocks of quantum circuits
- **Quantum Measurements**: Collapse of quantum states
- **Quantum Algorithms**: Speedups over classical computation

### Practical Applications
- **Quantum Chemistry**: Molecular simulation and drug discovery
- **Quantum Cryptography**: Secure communications
- **Quantum Machine Learning**: Enhanced pattern recognition
- **Quantum Optimization**: Solving complex optimization problems

## 🚀 Future Enhancements

- **Quantum Error Correction**: Implement surface codes and logical qubits
- **NISQ Algorithms**: Noise-intermediate scale quantum applications
- **Quantum Advantage**: Demonstrate quantum supremacy examples
- **Hardware Integration**: Connect to real quantum computers (IBM, Google, IonQ)

## 🤝 Contributing

We welcome contributions to expand the quantum algorithm library:

1. **Add New Algorithms**: Implement additional quantum algorithms
2. **Improve Visualizations**: Enhance quantum state representations
3. **Educational Content**: Add tutorials and explanations
4. **Performance Optimization**: Optimize quantum simulations

## 📄 License

This project is open-source and available under the MIT License.

## 🏆 Acknowledgments

- **IBM Qiskit Team**: For the comprehensive quantum computing framework
- **Google Cirq Team**: For the advanced quantum circuit simulator
- **Quantum Computing Community**: For continuous innovation and research

---

**Experience the power of quantum computing with Qiskit and Cirq!** 🌌⚛️
