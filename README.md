
# Quantum Computing Laboratory with Qiskit, Cirq & Full-Stack Web Interface

A comprehensive quantum computing laboratory implementing quantum algorithms, simulations, and cryptography protocols using **Qiskit** and **Cirq** frameworks, with a full-stack web application featuring Vue.js frontend and dual backend support (ASP.NET Core & Python Flask).

## 🚀 Features

### Quantum Frameworks
- **Qiskit Integration**: IBM's quantum computing framework for advanced quantum algorithms
- **Cirq Integration**: Google's quantum computing framework for quantum circuits and simulations
- **Automatic Backend Selection**: Seamlessly switches between available frameworks
- **Dual Backend Architecture**: Choose between Python Flask or ASP.NET Core backends

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

### Molecular Simulation
- **Molecular Structure Generation**: Visualize molecular structures (H2O, CO2, NH3)
- **Quantum Chemistry**: Quantum chemistry calculations for small molecules
- **Ground State Energy**: Calculate molecular ground states using VQE

### Quantum Cryptography
- **BB84 Quantum Key Distribution**: Secure key exchange using quantum mechanics
- **Quantum Random Number Generator (QRNG)**: True randomness from quantum measurements
- **Quantum Digital Signatures**: Cryptographic signatures using quantum protocols
- **Post-Quantum Cryptography**: Support for quantum-resistant algorithms (CRYSTALS-Kyber, Dilithium, SPHINCS+, FALCON)

### Security & Attack Simulation
- **Attack Protocols**: Simulate various quantum cryptographic attacks:
  - BB84 Intercept-Resend
  - Man-in-the-Middle
  - Photon Number Splitting
  - Trojan Horse
- **Security Analysis**: Real-time success and detection rate calculations
- **Security Recommendations**: Best practices for quantum-safe communications

### Advanced Features
- **Quantum State Analysis**: Entanglement measurement and fidelity calculations
- **Real-time Visualization**: Interactive quantum state and circuit visualization
- **Error Analysis**: Quantum error rates and decoherence studies
- **API Testing & Monitoring**: Built-in API testing interface with comprehensive logging

## 🛠️ Technology Stack

### Quantum Computing Frameworks
- **Qiskit**: IBM's open-source quantum computing framework
- **Cirq**: Google's Python library for quantum circuits
- **NumPy**: Numerical computing for quantum state mathematics

### Backend Technologies
- **Python 3.10+**: Core programming language for quantum algorithms
- **Flask**: Python web server for quantum API endpoints
- **ASP.NET Core 8**: Alternative high-performance web API framework
- **C#**: Type-safe backend development (ASP.NET option)
- **Aer Simulator**: Qiskit's quantum circuit simulator
- **Cirq Simulator**: Google's quantum state simulator

### Frontend Technologies
- **Vue.js 3**: Modern reactive frontend framework
- **Vite**: Fast build tool and development server
- **Axios**: HTTP client for API communication
- **Chart.js**: Data visualization
- **HTML5 Canvas**: Quantum state visualization
- **CSS3**: Modern styling with quantum-themed gradients and animations

### Development Tools
- **Swagger/OpenAPI**: API documentation and testing
- **CORS**: Cross-origin resource sharing support

## 📦 Installation & Setup

### Prerequisites
- **Python 3.10+**
- **Node.js** (v16 or higher)
- **.NET 8 SDK** (optional, for ASP.NET backend)
- **pip** package manager
- **Git**

### Install Quantum Computing Packages
```bash
pip install qiskit qiskit-aer cirq numpy flask
```

### Clone Repository
```bash
git clone <repository-url>
cd quantum-lab
```

### Python Flask Backend Setup
```bash
python quantum_server.py
```
The API will be available at `http://localhost:5000`

### ASP.NET Core Backend Setup (Alternative)
```bash
cd QuantumLab.API
dotnet restore
dotnet run
```
The API will be available at `http://localhost:5000`

### Frontend Setup
```bash
cd quantum-lab-frontend
npm install
npm run dev
```
The frontend will be available at `http://localhost:3000`

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
├── QuantumLab.API/             # ASP.NET Core Backend (Alternative)
│   ├── Controllers/            # API Controllers
│   │   ├── QuantumController.cs
│   │   ├── CryptographyController.cs
│   │   └── SimulationController.cs
│   ├── Models/                 # Data Models
│   │   └── QuantumModels.cs
│   ├── Program.cs             # Application Entry Point
│   └── QuantumLab.API.csproj  # Project Configuration
├── quantum-lab-frontend/       # Vue.js Frontend
│   ├── src/
│   │   ├── components/        # Vue Components
│   │   │   ├── QuantumSimulation.vue
│   │   │   ├── QuantumCryptography.vue
│   │   │   ├── AttackSimulation.vue
│   │   │   └── APITesting.vue
│   │   ├── services/          # API Services
│   │   │   └── api.js
│   │   ├── App.vue           # Main Application Component
│   │   ├── main.js           # Application Entry Point
│   │   └── style.css         # Global Styles
│   ├── index.html            # HTML Template
│   ├── package.json          # Dependencies
│   └── vite.config.js        # Build Configuration
├── QuantumCryptography.qs     # Legacy Q# cryptography (deprecated)
├── QuantumSimulation.qs       # Legacy Q# simulation (deprecated)
├── QuantumMaterials.qs        # Legacy Q# materials (deprecated)
└── README.md                  # This documentation
```

## 🔧 API Endpoints

### Quantum Circuit Operations
- `GET /api/bell_state` - Create Bell state pairs
- `POST /api/execute_circuit` - Execute custom quantum circuits
- `GET /api/entanglement` - Measure quantum entanglement
- `GET /api/fidelity` - Calculate quantum state fidelity
- `GET /api/quantum/circuits` - Get all circuits
- `POST /api/quantum/circuits` - Create new circuit
- `GET /api/quantum/circuits/{id}` - Get specific circuit
- `PUT /api/quantum/circuits/{id}` - Update circuit
- `DELETE /api/quantum/circuits/{id}` - Delete circuit
- `POST /api/quantum/circuits/{id}/execute` - Execute circuit

### Quantum Cryptography
- `POST /api/bb84` - BB84 quantum key distribution
- `POST /api/qrng` - Quantum random number generation
- `POST /api/quantum_sign` - Quantum digital signatures
- `POST /api/cryptography/qkd/start` - Start QKD protocol
- `POST /api/cryptography/qrng/generate` - Generate quantum random numbers
- `POST /api/cryptography/pqc/encrypt` - Encrypt with post-quantum cryptography
- `POST /api/cryptography/pqc/decrypt` - Decrypt with post-quantum cryptography
- `GET /api/cryptography/keys` - Get all generated keys

### Advanced Algorithms (Qiskit)
- `POST /api/vqe_simulation` - Variational quantum eigensolver
- `POST /api/grovers_search` - Grover's search algorithm
- `POST /api/qft` - Quantum Fourier transform

### Advanced Algorithms (Cirq)
- `POST /api/phase_estimation` - Quantum phase estimation
- `POST /api/quantum_teleportation` - Quantum teleportation
- `POST /api/quantum_walk` - Quantum walk simulation

### Molecular Simulation
- `GET /api/simulation/molecules` - Get all molecules
- `POST /api/simulation/molecules/generate` - Generate new molecule
- `POST /api/simulation/attacks/simulate` - Simulate cryptographic attack

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

### Creating a Quantum Circuit (Web API)
```javascript
const circuit = {
  name: "Bell State Circuit",
  gates: ["H", "CNOT"],
  qubits: 2
};

const response = await quantumAPI.createCircuit(circuit);
```

### BB84 Quantum Key Distribution
```python
from quantum_interface import quantum_interface

shared_key, error_rate = quantum_interface.bb84_key_distribution(256)
print(f"Generated {len(shared_key)} bit key with {error_rate:.2f}% error rate")
```

### Generating Quantum Keys (Web API)
```javascript
const qkdRequest = {
  keyLength: 256
};

const key = await cryptographyAPI.startQKD(qkdRequest);
```

### Simulating Molecular Structures
```javascript
const moleculeRequest = {
  type: "h2o",
  temperature: 300,
  pressure: 1
};

const molecule = await simulationAPI.generateMolecule(moleculeRequest);
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
- **Quantum-Safe Algorithms**: Implementation of NIST-approved post-quantum cryptographic algorithms
- **Attack Simulation**: Comprehensive testing against known quantum attacks
- **Real-time Monitoring**: Continuous security assessment and alerting
- **Best Practices**: Built-in security recommendations and guidelines

## 🚀 Deployment

### Local Development (Python Flask)
```bash
python quantum_server.py
```

### Local Development (ASP.NET Core)
1. Start the backend: `dotnet run` in `QuantumLab.API/`
2. Start the frontend: `npm run dev` in `quantum-lab-frontend/`

### Production Build
```bash
# Frontend
cd quantum-lab-frontend
npm run build

# Backend (ASP.NET)
cd QuantumLab.API
dotnet publish -c Release
```

## 🧪 Testing

### API Testing
The application includes a built-in API testing interface accessible through the "API Testing" tab.

### Manual Testing
```bash
# Test quantum circuit creation
curl -X POST http://localhost:5000/api/quantum/circuits \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","gates":["H","X"],"qubits":1}'

# Test QKD protocol
curl -X POST http://localhost:5000/api/cryptography/qkd/start \
  -H "Content-Type: application/json" \
  -d '{"keyLength":256}'
```

## 📊 Performance Considerations

- **Efficient State Management**: Optimized quantum state calculations
- **Lazy Loading**: Components loaded on demand
- **Caching**: Strategic caching of API responses
- **Responsive Design**: Mobile-first approach for all interfaces

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
- **Real Quantum Hardware Integration**: Connect to IBM Quantum, IonQ, or other quantum cloud services
- **Advanced Visualization**: 3D quantum state representations
- **Machine Learning**: AI-powered quantum algorithm optimization
- **Collaborative Features**: Multi-user quantum circuit development
- **Extended Attack Library**: Additional quantum cryptographic attacks
- **Performance Analytics**: Detailed quantum algorithm performance metrics

## 🤝 Contributing

We welcome contributions to expand the quantum algorithm library:

1. **Add New Algorithms**: Implement additional quantum algorithms
2. **Improve Visualizations**: Enhance quantum state representations
3. **Educational Content**: Add tutorials and explanations
4. **Performance Optimization**: Optimize quantum simulations
5. Fork the repository
6. Create a feature branch (`git checkout -b feature/amazing-feature`)
7. Commit your changes (`git commit -m 'Add amazing feature'`)
8. Push to the branch (`git push origin feature/amazing-feature`)
9. Open a Pull Request

## 📄 License

This project is open-source and available under the MIT License.

## 🆘 Support

For support, email support@quantumlab.dev or join our [Discord community](https://discord.gg/quantumlab).

## 🏆 Acknowledgments

- **IBM Qiskit Team**: For the comprehensive quantum computing framework
- **Google Cirq Team**: For the advanced quantum circuit simulator
- **Quantum Computing Community**: For continuous innovation and research
- **NIST**: Post-quantum cryptography standards
- **Vue.js Community**: Excellent documentation and ecosystem
- **ASP.NET Core Team**: Robust backend framework

## 📈 Project Status

- ✅ Quantum Circuit Simulation (Qiskit & Cirq)
- ✅ Cryptography Protocols
- ✅ Attack Simulation
- ✅ API Integration (Flask & ASP.NET)
- ✅ Responsive Web Interface
- ✅ Molecular Simulation
- ✅ Advanced Quantum Algorithms
- 🔄 Real Hardware Integration (In Progress)
- 📋 Extended Documentation (Planned)
- 🔄 Performance Optimization (In Progress)

---

**Experience the power of quantum computing with Qiskit, Cirq, and modern web technologies!** 🌌⚛️

**Built with ❤️ for the quantum computing community**
