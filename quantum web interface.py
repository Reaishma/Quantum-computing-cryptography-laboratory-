
"""
Django web interface for quantum computing laboratory
Integrates Qiskit, Cirq, and Q# implementations
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import sys
import os

# Add quantum algorithms to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'quantum_algorithms'))

from quantum_algorithms.qiskit_implementation import QiskitQuantumLab
from quantum_algorithms.cirq_implementation import CirqQuantumLab
from quantum_algorithms.qsharp_implementation import QSharpQuantumLab

def quantum_lab_home(request):
    """Serve the main quantum lab interface"""
    with open('attached_assets/index (1)_1753267859587.html', 'r') as f:
        html_content = f.read()
    return render(request, 'quantum_lab.html', {'html_content': html_content})

@csrf_exempt
def quantum_api(request):
    """Main API endpoint for quantum operations"""
    if request.method == 'POST':
        data = json.loads(request.body)
        framework = data.get('framework', 'qiskit')
        operation = data.get('operation')
        params = data.get('params', {})
        
        try:
            if framework == 'qiskit':
                lab = QiskitQuantumLab()
                result = execute_qiskit_operation(lab, operation, params)
            elif framework == 'cirq':
                lab = CirqQuantumLab()
                result = execute_cirq_operation(lab, operation, params)
            elif framework == 'qsharp':
                lab = QSharpQuantumLab()
                result = execute_qsharp_operation(lab, operation, params)
            else:
                return JsonResponse({'error': 'Invalid framework'}, status=400)
                
            return JsonResponse({
                'success': True,
                'framework': framework,
                'operation': operation,
                'result': result
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def execute_qiskit_operation(lab, operation, params):
    """Execute Qiskit operations"""
    operations = {
        'molecular_simulation': lambda: lab.create_molecular_simulation(
            params.get('molecule', 'H2O')
        ),
        'build_circuit': lambda: lab.build_quantum_circuit(
            params.get('gates', [])
        ).draw('text'),
        'execute_circuit': lambda: lab.execute_circuit(
            lab.build_quantum_circuit(params.get('gates', []))
        ),
        'bb84_qkd': lambda: lab.bb84_key_distribution(
            params.get('key_length', 128)
        ),
        'quantum_random': lambda: lab.quantum_random_generator(
            params.get('bits', 128)
        ),
        'shors_algorithm': lambda: lab.shors_algorithm(
            params.get('number', 15)
        ),
        'grovers_search': lambda: lab.grovers_search(
            params.get('target', 'item'),
            params.get('database_size', 1000000)
        ),
        'material_simulation': lambda: lab.simulate_material_properties(
            params.get('material', 'Silicon'),
            params.get('temperature', 300),
            params.get('pressure', 1)
        )
    }
    
    if operation in operations:
        return operations[operation]()
    else:
        raise ValueError(f"Unknown Qiskit operation: {operation}")

def execute_cirq_operation(lab, operation, params):
    """Execute Cirq operations"""
    operations = {
        'vqe_simulation': lambda: lab.variational_quantum_eigensolver(
            params.get('molecule', 'H2')
        ),
        'qaoa_optimization': lambda: lab.quantum_approximate_optimization(
            params.get('problem_size', 4)
        ),
        'quantum_ml': lambda: lab.quantum_machine_learning_circuit(
            params.get('data_points', 4)
        ),
        'error_correction': lambda: lab.quantum_error_correction(
            params.get('error_rate', 0.01)
        ),
        'quantum_fourier_transform': lambda: lab.quantum_fourier_transform(
            params.get('qubits', 4)
        ),
        'quantum_teleportation': lambda: lab.quantum_teleportation()
    }
    
    if operation in operations:
        return operations[operation]()
    else:
        raise ValueError(f"Unknown Cirq operation: {operation}")

def execute_qsharp_operation(lab, operation, params):
    """Execute Q# operations"""
    operations = {
        'phase_estimation': lambda: lab.quantum_phase_estimation(
            params.get('bits', 4)
        ),
        'dynamics_simulation': lambda: lab.quantum_dynamics_simulation(
            params.get('steps', 10)
        ),
        'quantum_ml_training': lambda: lab.quantum_machine_learning_training(
            params.get('data_size', 100)
        ),
        'cryptography_protocol': lambda: lab.quantum_cryptography_protocols(
            params.get('protocol', 'QKD')
        ),
        'azure_integration': lambda: lab.azure_quantum_integration(
            params.get('hardware', 'IonQ')
        ),
        'optimization_suite': lambda: lab.quantum_optimization_suite(
            params.get('problem', 'MaxCut')
        )
    }
    
    if operation in operations:
        return operations[operation]()
    else:
        raise ValueError(f"Unknown Q# operation: {operation}")

@csrf_exempt
def quantum_comparison(request):
    """Compare results across all three frameworks"""
    if request.method == 'POST':
        data = json.loads(request.body)
        operation_type = data.get('type', 'basic_circuit')
        
        qiskit_lab = QiskitQuantumLab()
        cirq_lab = CirqQuantumLab()
        qsharp_lab = QSharpQuantumLab()
        
        results = {}
        
        if operation_type == 'molecular_simulation':
            results['qiskit'] = qiskit_lab.create_molecular_simulation('H2O')
            results['cirq'] = cirq_lab.variational_quantum_eigensolver('H2O')
            results['qsharp'] = qsharp_lab.quantum_dynamics_simulation(10)
            
        elif operation_type == 'optimization':
            results['qiskit'] = qiskit_lab.grovers_search('target', 1000)
            results['cirq'] = cirq_lab.quantum_approximate_optimization(4)
            results['qsharp'] = qsharp_lab.quantum_optimization_suite('MaxCut')
            
        elif operation_type == 'cryptography':
            results['qiskit'] = qiskit_lab.bb84_key_distribution(128)
            results['cirq'] = {"protocol": "Quantum error correction for secure communication"}
            results['qsharp'] = qsharp_lab.quantum_cryptography_protocols('QKD')
        
        return JsonResponse({
            'comparison_type': operation_type,
            'frameworks': results,
            'analysis': {
                'qiskit_strengths': 'Hardware integration, extensive algorithms',
                'cirq_strengths': 'NISQ algorithms, Google hardware',
                'qsharp_strengths': 'Enterprise integration, Azure cloud'
            }
        })
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
