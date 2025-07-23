
import axios from 'axios'

const API_BASE_URL = 'http://localhost:5000/api'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
})

export const quantumAPI = {
  getCircuits: () => api.get('/quantum/circuits'),
  getCircuit: (id) => api.get(`/quantum/circuits/${id}`),
  createCircuit: (data) => api.post('/quantum/circuits', data),
  updateCircuit: (id, data) => api.put(`/quantum/circuits/${id}`, data),
  deleteCircuit: (id) => api.delete(`/quantum/circuits/${id}`),
  executeCircuit: (id) => api.post(`/quantum/circuits/${id}/execute`),
  generateMolecule: (data) => api.post('/simulation/molecules/generate', data)
}

export const cryptographyAPI = {
  startQKD: (data) => api.post('/cryptography/qkd/start', data),
  generateQuantumRandom: (data) => api.post('/cryptography/qrng/generate', data),
  encryptPQC: (data) => api.post('/cryptography/pqc/encrypt', data),
  decryptPQC: (data) => api.post('/cryptography/pqc/decrypt', data),
  getKeys: () => api.get('/cryptography/keys')
}

export const simulationAPI = {
  getMolecules: () => api.get('/simulation/molecules'),
  generateMolecule: (data) => api.post('/simulation/molecules/generate', data),
  simulateAttack: (data) => api.post('/simulation/attacks/simulate', data)
}

export default api
