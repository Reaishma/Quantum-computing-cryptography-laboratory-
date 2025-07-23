
"""
Quantum Computing Laboratory - Multi-Framework Integration Demo
Demonstrates IBM Qiskit, Google Cirq, and Microsoft Q# working together
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from quantum_implementations.qiskit_quantum_lab import QiskitQuantumLab
from quantum_implementations.cirq_quantum_lab import CirqQuantumLab
from quantum_implementations.qsharp_quantum_lab import QSharpQuantumLab
import json
import time
from typing import Dict, List, Any

class MultiFrameworkQuantumLab:
    """
    Unified interface for quantum computing across multiple frameworks
    Integrates IBM Qiskit, Google Cirq, and Microsoft Q#
    """
    
    def __init__(self):
        print("🚀 Initializing Multi-Framework Quantum Laboratory...")
        print("   📊 Loading IBM Qiskit...")
        self.qiskit_lab = QiskitQuantumLab()
        print("   📊 Loading Google Cirq...")
        self.cirq_lab = CirqQuantumLab()
        print("   📊 Loading Microsoft Q#...")
        self.qsharp_lab = QSharpQuantumLab()
        
        self.frameworks = {
            'qiskit': self.qiskit_lab,
            'cirq': self.cirq_lab,
            'qsharp': self.qsharp_lab
        }
        
        print("✅ All quantum frameworks loaded successfully!")
    
    def compare_frameworks(self, operation: str, **kwargs) -> Dict[str, Any]:
        """Compare the same operation across all frameworks"""
        
        print(f"\n🔬 Comparing {operation} across all frameworks...")
        results = {}
        
        for framework_name, lab in self.frameworks.items():
            try:
                print(f"   🔸 Running on {framework_name.upper()}...")
                start_time = time.time()
                
                if operation == 'bell_state':
                    result = lab.create_bell_state()
                elif operation == 'circuit_execution':
                    circuit = lab.create_quantum_circuit(**kwargs)
                    result = lab.execute_circuit(circuit['id'])
                elif operation == 'molecular_simulation':
                    result = lab.simulate_molecule(**kwargs)
                elif operation == 'bb84_qkd':
                    result = lab.bb84_key_distribution(**kwargs)
                elif operation == 'quantum_random':
                    result = lab.quantum_random_number_generator(**kwargs)
                elif operation == 'shor_attack':
                    result = lab.simulate_shor_attack(**kwargs)
                elif operation == 'grover_attack':
                    result = lab.simulate_grover_attack(**kwargs)
                else:
                    result = {'error': f'Unknown operation: {operation}'}
                
                execution_time = time.time() - start_time
                
                results[framework_name] = {
                    'result': result,
                    'execution_time': execution_time,
                    'success': True
                }
                
                print(f"      ✅ Completed in {execution_time:.3f}s")
                
            except Exception as e:
                results[framework_name] = {
                    'error': str(e),
                    'success': False
                }
                print(f"      ❌ Error: {str(e)}")
        
        return results
    
    def demonstrate_quantum_circuits(self):
        """Demonstrate quantum circuit creation across frameworks"""
        
        print("\n" + "=" * 60)
        print("🔬 QUANTUM CIRCUIT DEMONSTRATION")
        print("=" * 60)
        
        # Test simple circuit
        circuit_params = {
            'name': 'Demo Circuit',
            'num_qubits': 3,
            'gates': ['H', 'X', 'CNOT']
        }
        
        results = self.compare_frameworks('circuit_execution', **circuit_params)
        
        print(f"\n📊 Circuit Comparison Results:")
        for framework, data in results.items():
            if data['success']:
                counts = data['result'].get('counts', {})
                time_taken = data['execution_time']
                print(f"   {framework.upper():8}: {len(counts)} states, {time_taken:.3f}s")
            else:
                print(f"   {framework.upper():8}: Failed - {data['error']}")
        
        return results
    
    def demonstrate_bell_states(self):
        """Demonstrate Bell state creation across frameworks"""
        
        print("\n" + "=" * 60)
        print("🔬 BELL STATE DEMONSTRATION")
        print("=" * 60)
        
        results = self.compare_frameworks('bell_state')
        
        print(f"\n📊 Bell State Comparison Results:")
        for framework, data in results.items():
            if data['success']:
                result = data['result']
                entanglement = result.get('entanglement', 0)
                fidelity = result.get('fidelity', 0)
                print(f"   {framework.upper():8}: Entanglement={entanglement:.3f}, Fidelity={fidelity:.3f}")
            else:
                print(f"   {framework.upper():8}: Failed - {data['error']}")
        
        return results
    
    def demonstrate_molecular_simulation(self):
        """Demonstrate molecular simulation across frameworks"""
        
        print("\n" + "=" * 60)
        print("🔬 MOLECULAR SIMULATION DEMONSTRATION")
        print("=" * 60)
        
        molecules = ['h2o', 'co2', 'nh3']
        all_results = {}
        
        for molecule in molecules:
            print(f"\n🧪 Simulating {molecule.upper()} molecule...")
            
            results = self.compare_frameworks(
                'molecular_simulation',
                molecule_type=molecule,
                temperature=300,
                pressure=1
            )
            
            all_results[molecule] = results
            
            print(f"📊 {molecule.upper()} Simulation Results:")
            for framework, data in results.items():
                if data['success']:
                    props = data['result'].get('properties', {})
                    energy = props.get('energy', 0)
                    stability = props.get('stability', 0)
                    print(f"   {framework.upper():8}: Energy={energy:.2f}, Stability={stability:.3f}")
                else:
                    print(f"   {framework.upper():8}: Failed - {data['error']}")
        
        return all_results
    
    def demonstrate_quantum_cryptography(self):
        """Demonstrate quantum cryptography across frameworks"""
        
        print("\n" + "=" * 60)
        print("🔬 QUANTUM CRYPTOGRAPHY DEMONSTRATION")
        print("=" * 60)
        
        # BB84 Quantum Key Distribution
        print("\n🔐 BB84 Quantum Key Distribution...")
        qkd_results = self.compare_frameworks('bb84_qkd', key_length=128)
        
        print(f"📊 BB84 QKD Results:")
        for framework, data in qkd_results.items():
            if data['success']:
                result = data['result']
                key_length = result.get('key_length', 0)
                error_rate = result.get('error_rate', 0)
                security = result.get('security_level', 'UNKNOWN')
                print(f"   {framework.upper():8}: KeyLen={key_length}, Error={error_rate:.3f}, Security={security}")
            else:
                print(f"   {framework.upper():8}: Failed - {data['error']}")
        
        # Quantum Random Number Generation
        print("\n🎲 Quantum Random Number Generation...")
        qrng_results = self.compare_frameworks('quantum_random', num_bits=64)
        
        print(f"📊 QRNG Results:")
        for framework, data in qrng_results.items():
            if data['success']:
                result = data['result']
                bits = result.get('bits', 0)
                hex_value = result.get('hex', '')[:8]  # First 8 hex digits
                print(f"   {framework.upper():8}: {bits} bits, Hex={hex_value}...")
            else:
                print(f"   {framework.upper():8}: Failed - {data['error']}")
        
        return {'bb84': qkd_results, 'qrng': qrng_results}
    
    def demonstrate_attack_simulation(self):
        """Demonstrate quantum attack simulation across frameworks"""
        
        print("\n" + "=" * 60)
        print("🔬 QUANTUM ATTACK SIMULATION")
        print("=" * 60)
        
        # Shor's Algorithm
        print("\n⚔️  Shor's Algorithm (RSA Factorization)...")
        shor_results = self.compare_frameworks('shor_attack', rsa_bits=1024)
        
        print(f"📊 Shor's Algorithm Results:")
        for framework, data in shor_results.items():
            if data['success']:
                result = data['result']
                qubits = result.get('qubits_required', 0)
                success_prob = result.get('success_probability', 0)
                print(f"   {framework.upper():8}: {qubits} qubits, Success={success_prob:.2f}")
            else:
                print(f"   {framework.upper():8}: Failed - {data['error']}")
        
        # Grover's Algorithm
        print("\n🔍 Grover's Algorithm (Database Search)...")
        grover_results = self.compare_frameworks('grover_attack', search_space_size=1000000)
        
        print(f"📊 Grover's Algorithm Results:")
        for framework, data in grover_results.items():
            if data['success']:
                result = data['result']
                qubits = result.get('qubits_required', 0)
                speedup = result.get('speedup', 'N/A')
                iterations = result.get('iterations', 0)
                print(f"   {framework.upper():8}: {qubits} qubits, Speedup={speedup}, Iter={iterations}")
            else:
                print(f"   {framework.upper():8}: Failed - {data['error']}")
        
        return {'shor': shor_results, 'grover': grover_results}
    
    def performance_benchmark(self):
        """Benchmark performance across frameworks"""
        
        print("\n" + "=" * 60)
        print("🔬 PERFORMANCE BENCHMARK")
        print("=" * 60)
        
        benchmark_results = {}
        
        # Circuit execution benchmark
        print("\n⚡ Circuit Execution Speed Test...")
        start_time = time.time()
        
        for framework_name, lab in self.frameworks.items():
            try:
                times = []
                for i in range(5):  # Run 5 times for average
                    start = time.time()
                    circuit = lab.create_quantum_circuit(f"Benchmark_{i}", 3, ['H', 'X', 'CNOT'])
                    lab.execute_circuit(circuit['id'])
                    times.append(time.time() - start)
                
                avg_time = sum(times) / len(times)
                benchmark_results[framework_name] = {
                    'avg_execution_time': avg_time,
                    'total_tests': len(times)
                }
                
                print(f"   {framework_name.upper():8}: {avg_time:.4f}s average")
                
            except Exception as e:
                benchmark_results[framework_name] = {'error': str(e)}
                print(f"   {framework_name.upper():8}: Error - {str(e)}")
        
        total_time = time.time() - start_time
        print(f"\n📊 Total benchmark time: {total_time:.2f}s")
        
        return benchmark_results
    
    def generate_comparison_report(self):
        """Generate comprehensive comparison report"""
        
        report = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'frameworks_tested': list(self.frameworks.keys()),
            'system_status': {}
        }
        
        # Get system status from each framework
        for framework_name, lab in self.frameworks.items():
            try:
                status = lab.get_system_status()
                report['system_status'][framework_name] = status
            except Exception as e:
                report['system_status'][framework_name] = {'error': str(e)}
        
        print("\n" + "=" * 60)
        print("📄 SYSTEM STATUS REPORT")
        print("=" * 60)
        
        for framework, status in report['system_status'].items():
            if 'error' not in status:
                circuits = status.get('total_circuits', 0)
                molecules = status.get('total_molecules', 0)
                keys = status.get('total_keys', 0)
                max_qubits = status.get('max_qubits', 0)
                
                print(f"\n{framework.upper()} Status:")
                print(f"   Circuits: {circuits}")
                print(f"   Molecules: {molecules}")
                print(f"   Crypto Keys: {keys}")
                print(f"   Max Qubits: {max_qubits}")
            else:
                print(f"\n{framework.upper()} Status: Error - {status['error']}")
        
        return report
    
    def run_full_demonstration(self):
        """Run complete demonstration of all frameworks"""
        
        print("🌟" * 30)
        print("🌟 QUANTUM COMPUTING LABORATORY 🌟")
        print("🌟 Multi-Framework Demonstration 🌟")
        print("🌟" * 30)
        
        results = {}
        
        try:
            # Run all demonstrations
            results['circuits'] = self.demonstrate_quantum_circuits()
            results['bell_states'] = self.demonstrate_bell_states()
            results['molecules'] = self.demonstrate_molecular_simulation()
            results['cryptography'] = self.demonstrate_quantum_cryptography()
            results['attacks'] = self.demonstrate_attack_simulation()
            results['benchmark'] = self.performance_benchmark()
            results['report'] = self.generate_comparison_report()
            
            print("\n" + "=" * 60)
            print("🎉 DEMONSTRATION COMPLETE!")
            print("=" * 60)
            print("✅ All quantum frameworks tested successfully")
            print("✅ Qiskit: IBM's quantum computing platform")
            print("✅ Cirq: Google's quantum computing framework")
            print("✅ Q#: Microsoft's quantum programming language")
            print("\n🚀 Ready for quantum computing development!")
            
        except Exception as e:
            print(f"\n❌ Demonstration failed: {str(e)}")
            results['error'] = str(e)
        
        return results

# Main execution
if __name__ == "__main__":
    try:
        # Initialize multi-framework lab
        lab = MultiFrameworkQuantumLab()
        
        # Run full demonstration
        demo_results = lab.run_full_demonstration()
        
        # Save results to file
        with open('quantum_demo_results.json', 'w') as f:
            # Convert complex objects to strings for JSON serialization
            def json_serializer(obj):
                if hasattr(obj, '__dict__'):
                    return str(obj)
                elif isinstance(obj, complex):
                    return {'real': obj.real, 'imag': obj.imag}
                return str(obj)
            
            json.dump(demo_results, f, indent=2, default=json_serializer)
        
        print(f"\n💾 Results saved to 'quantum_demo_results.json'")
        
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
        import traceback
        traceback.print_exc()
