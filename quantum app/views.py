
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
from quantum_circuits import QuantumCircuitImplementations

quantum_impl = QuantumCircuitImplementations()

def quantum_dashboard(request):
    """Render the quantum dashboard"""
    return render(request, 'quantum_dashboard.html')

@csrf_exempt
def execute_quantum_circuit(request):
    """Execute quantum circuits via API"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            circuit_type = data.get('circuit_type', 'basic')
            framework = data.get('framework', 'qiskit')
            
            if framework == 'qiskit':
                if circuit_type == 'basic':
                    qc, counts = quantum_impl.qiskit_basic_gates()
                    return JsonResponse({
                        'success': True,
                        'results': counts,
                        'circuit': str(qc),
                        'framework': 'Qiskit'
                    })
                elif circuit_type == 'bell':
                    qc, counts = quantum_impl.qiskit_bell_state()
                    return JsonResponse({
                        'success': True,
                        'results': counts,
                        'circuit': str(qc),
                        'framework': 'Qiskit'
                    })
                elif circuit_type == 'grover':
                    target = data.get('target', 3)
                    qc, counts = quantum_impl.qiskit_grover_search(target)
                    return JsonResponse({
                        'success': True,
                        'results': counts,
                        'circuit': str(qc),
                        'framework': 'Qiskit'
                    })
                    
            elif framework == 'cirq':
                if circuit_type == 'basic':
                    circuit, result = quantum_impl.cirq_basic_gates()
                    return JsonResponse({
                        'success': True,
                        'results': {str(k): int(v) for k, v in result.histogram(key='q0').items()},
                        'circuit': str(circuit),
                        'framework': 'Cirq'
                    })
                elif circuit_type == 'bell':
                    circuit, result = quantum_impl.cirq_bell_state()
                    return JsonResponse({
                        'success': True,
                        'results': {str(k): int(v) for k, v in result.histogram(key='q0').items()},
                        'circuit': str(circuit),
                        'framework': 'Cirq'
                    })
                elif circuit_type == 'grover':
                    target = data.get('target', 3)
                    circuit, result = quantum_impl.cirq_grover_search(target)
                    return JsonResponse({
                        'success': True,
                        'results': {str(k): int(v) for k, v in result.histogram(key='q0').items()},
                        'circuit': str(circuit),
                        'framework': 'Cirq'
                    })
                elif circuit_type == 'teleportation':
                    circuit, result = quantum_impl.cirq_quantum_teleportation()
                    return JsonResponse({
                        'success': True,
                        'results': {str(k): int(v) for k, v in result.histogram(key='bob_final').items()},
                        'circuit': str(circuit),
                        'framework': 'Cirq'
                    })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@csrf_exempt
def quantum_simulation(request):
    """Run quantum simulations"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            simulation_type = data.get('type', 'basic')
            
            if simulation_type == 'all':
                # Run all examples
                quantum_impl.run_all_examples()
                return JsonResponse({
                    'success': True,
                    'message': 'All quantum simulations completed successfully'
                })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})
