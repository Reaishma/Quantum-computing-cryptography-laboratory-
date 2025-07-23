
# Quantum Computing & Cryptography Laboratory

A full-stack web application for quantum computing simulation, cryptography protocols, and attack simulation built with Vue.js frontend and ASP.NET Core backend.

## 🚀 Features

### Quantum Simulation
- **Quantum Circuit Builder**: Create and execute quantum circuits with various gates (H, X, Y, Z, CNOT, RZ)
- **Molecular Simulation**: Generate and visualize molecular structures (H2O, CO2, NH3)
- **Quantum State Visualization**: Real-time quantum state representation and circuit execution

### Quantum Cryptography
- **Quantum Key Distribution (QKD)**: Implementation of BB84 protocol for secure key exchange
- **Quantum Random Number Generator (QRNG)**: Generate truly random numbers using quantum principles
- **Post-Quantum Cryptography**: Support for quantum-resistant algorithms (CRYSTALS-Kyber, Dilithium, SPHINCS+, FALCON)

### Security & Attack Simulation
- **Attack Protocols**: Simulate various quantum cryptographic attacks:
  - BB84 Intercept-Resend
  - Man-in-the-Middle
  - Photon Number Splitting
  - Trojan Horse
- **Security Analysis**: Real-time success and detection rate calculations
- **Security Recommendations**: Best practices for quantum-safe communications

### API Testing & Monitoring
- **RESTful API**: Complete REST API for all quantum operations
- **Real-time Status Monitoring**: Live API health checks
- **Interactive Testing**: Built-in API testing interface
- **Comprehensive Logging**: Request/response logging with detailed error handling

## 🛠️ Technology Stack

### Frontend
- **Vue.js 3**: Modern reactive framework
- **Vite**: Fast build tool and development server
- **Axios**: HTTP client for API communication
- **Chart.js**: Data visualization
- **CSS3**: Custom styling with gradients and animations

### Backend
- **ASP.NET Core 8**: High-performance web API framework
- **C#**: Type-safe backend development
- **Swagger/OpenAPI**: API documentation and testing
- **CORS**: Cross-origin resource sharing support

## 📦 Installation & Setup

### Prerequisites
- **Node.js** (v16 or higher)
- **.NET 8 SDK**
- **Git**

### Clone Repository
```bash
git clone <repository-url>
cd quantum-lab
```

### Backend Setup
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

## 🏗️ Project Structure

```
quantum-lab/
├── QuantumLab.API/              # ASP.NET Core Backend
│   ├── Controllers/             # API Controllers
│   │   ├── QuantumController.cs
│   │   ├── CryptographyController.cs
│   │   └── SimulationController.cs
│   ├── Models/                  # Data Models
│   │   └── QuantumModels.cs
│   ├── Program.cs              # Application Entry Point
│   └── QuantumLab.API.csproj   # Project Configuration
│
├── quantum-lab-frontend/        # Vue.js Frontend
│   ├── src/
│   │   ├── components/         # Vue Components
│   │   │   ├── QuantumSimulation.vue
│   │   │   ├── QuantumCryptography.vue
│   │   │   ├── AttackSimulation.vue
│   │   │   └── APITesting.vue
│   │   ├── services/           # API Services
│   │   │   └── api.js
│   │   ├── App.vue            # Main Application Component
│   │   ├── main.js            # Application Entry Point
│   │   └── style.css          # Global Styles
│   ├── index.html             # HTML Template
│   ├── package.json           # Dependencies
│   └── vite.config.js         # Build Configuration
│
└── README.md                   # Documentation
```

## 🔧 API Endpoints

### Quantum Circuits
- `GET /api/quantum/circuits` - Get all circuits
- `POST /api/quantum/circuits` - Create new circuit
- `GET /api/quantum/circuits/{id}` - Get specific circuit
- `PUT /api/quantum/circuits/{id}` - Update circuit
- `DELETE /api/quantum/circuits/{id}` - Delete circuit
- `POST /api/quantum/circuits/{id}/execute` - Execute circuit

### Cryptography
- `POST /api/cryptography/qkd/start` - Start QKD protocol
- `POST /api/cryptography/qrng/generate` - Generate quantum random numbers
- `POST /api/cryptography/pqc/encrypt` - Encrypt with post-quantum cryptography
- `POST /api/cryptography/pqc/decrypt` - Decrypt with post-quantum cryptography
- `GET /api/cryptography/keys` - Get all generated keys

### Simulation
- `GET /api/simulation/molecules` - Get all molecules
- `POST /api/simulation/molecules/generate` - Generate new molecule
- `POST /api/simulation/attacks/simulate` - Simulate cryptographic attack

## 🎯 Usage Examples

### Creating a Quantum Circuit
```javascript
const circuit = {
  name: "Bell State Circuit",
  gates: ["H", "CNOT"],
  qubits: 2
};

const response = await quantumAPI.createCircuit(circuit);
```

### Generating Quantum Keys
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

## 🔐 Security Features

- **Quantum-Safe Algorithms**: Implementation of NIST-approved post-quantum cryptographic algorithms
- **Attack Simulation**: Comprehensive testing against known quantum attacks
- **Real-time Monitoring**: Continuous security assessment and alerting
- **Best Practices**: Built-in security recommendations and guidelines

## 🚀 Deployment

### Local Development
1. Start the backend: `dotnet run` in `QuantumLab.API/`
2. Start the frontend: `npm run dev` in `quantum-lab-frontend/`

### Production Build
```bash
# Frontend
cd quantum-lab-frontend
npm run build

# Backend
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

## 🔮 Future Enhancements

- **Real Quantum Hardware Integration**: Connect to IBM Quantum, IonQ, or other quantum cloud services
- **Advanced Visualization**: 3D quantum state representations
- **Machine Learning**: AI-powered quantum algorithm optimization
- **Collaborative Features**: Multi-user quantum circuit development
- **Extended Attack Library**: Additional quantum cryptographic attacks
- **Performance Analytics**: Detailed quantum algorithm performance metrics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support, email support@quantumlab.dev or join our [Discord community](https://discord.gg/quantumlab).

## 🙏 Acknowledgments

- **IBM Qiskit**: Inspiration for quantum circuit visualization
- **NIST**: Post-quantum cryptography standards
- **Vue.js Community**: Excellent documentation and ecosystem
- **ASP.NET Core Team**: Robust backend framework

---

**Built with ❤️ for the quantum computing community**

## 📈 Project Status

- ✅ Quantum Circuit Simulation
- ✅ Cryptography Protocols
- ✅ Attack Simulation
- ✅ API Integration
- ✅ Responsive Design
- 🔄 Real Hardware Integration (In Progress)
- 📋 Extended Documentation (Planned)
- 🔄 Performance Optimization (In Progress)

---

