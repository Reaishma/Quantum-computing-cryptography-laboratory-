
namespace QuantumLab {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Arrays;

    // Quantum Circuit Builder Operations
    operation CreateBellState() : (Result, Result) {
        use (q1, q2) = (Qubit(), Qubit());
        
        H(q1);
        CNOT(q1, q2);
        
        let result1 = M(q1);
        let result2 = M(q2);
        
        Reset(q1);
        Reset(q2);
        
        return (result1, result2);
    }

    operation QuantumCircuitBuilder(gates : String[]) : Result[] {
        let numQubits = 3;
        use qubits = Qubit[numQubits];
        mutable results = [];
        
        for gate in gates {
            if gate == "H" {
                H(qubits[0]);
            }
            elif gate == "X" {
                X(qubits[0]);
            }
            elif gate == "Y" {
                Y(qubits[0]);
            }
            elif gate == "Z" {
                Z(qubits[0]);
            }
            elif gate == "CNOT" {
                CNOT(qubits[0], qubits[1]);
            }
            elif gate == "RZ" {
                Rz(PI() / 4.0, qubits[0]);
            }
            elif gate == "RY" {
                Ry(PI() / 4.0, qubits[0]);
            }
        }
        
        for qubit in qubits {
            set results += [M(qubit)];
        }
        
        ResetAll(qubits);
        return results;
    }

    // Quantum State Simulation
    operation QuantumStateEvolution(iterations : Int) : Double {
        use qubit = Qubit();
        mutable fidelity = 0.0;
        
        for i in 1..iterations {
            H(qubit);
            Ry(IntAsDouble(i) * PI() / 10.0, qubit);
            
            let result = M(qubit);
            if result == Zero {
                set fidelity += 1.0;
            }
            Reset(qubit);
        }
        
        return fidelity / IntAsDouble(iterations);
    }

    // Quantum Entanglement Measurement
    operation MeasureEntanglement() : Double {
        use (q1, q2) = (Qubit(), Qubit());
        
        H(q1);
        CNOT(q1, q2);
        
        // Simulate entanglement measurement
        let result1 = M(q1);
        let result2 = M(q2);
        
        mutable entanglement = 0.0;
        if result1 == result2 {
            set entanglement = 0.75; // High entanglement
        } else {
            set entanglement = 0.25; // Low entanglement
        }
        
        Reset(q1);
        Reset(q2);
        
        return entanglement;
    }
}
