
<template>
  <div class="grid">
    <div class="card">
      <h3>API Endpoints</h3>
      <select class="input" v-model="selectedEndpoint">
        <option value="circuits">GET /api/quantum/circuits</option>
        <option value="create-circuit">POST /api/quantum/circuits</option>
        <option value="qkd">POST /api/cryptography/qkd/start</option>
        <option value="qrng">POST /api/cryptography/qrng/generate</option>
        <option value="molecule">POST /api/simulation/molecules/generate</option>
        <option value="attack">POST /api/simulation/attacks/simulate</option>
      </select>
      
      <select class="input" v-model="httpMethod">
        <option>GET</option>
        <option>POST</option>
        <option>PUT</option>
        <option>DELETE</option>
      </select>
      
      <textarea 
        class="input" 
        v-model="requestPayload" 
        placeholder="JSON Payload" 
        rows="6"
      ></textarea>
      
      <button class="button" @click="callAPI">Call API</button>
      
      <div class="log">
        <h4>Request</h4>
        <pre>{{ requestLog }}</pre>
        
        <h4>Response</h4>
        <pre>{{ responseLog }}</pre>
      </div>
    </div>

    <div class="card">
      <h3>API Status</h3>
      <div class="status-indicators">
        <div class="status-item">
          <div class="status-dot" :class="{ active: apiStatus.quantum }"></div>
          <span>Quantum API</span>
        </div>
        <div class="status-item">
          <div class="status-dot" :class="{ active: apiStatus.cryptography }"></div>
          <span>Cryptography API</span>
        </div>
        <div class="status-item">
          <div class="status-dot" :class="{ active: apiStatus.simulation }"></div>
          <span>Simulation API</span>
        </div>
      </div>
      
      <button class="button" @click="checkAPIStatus">Check Status</button>
    </div>

    <div class="card">
      <h3>Quick Tests</h3>
      <div class="quick-tests">
        <button class="button" @click="testQuantumCircuit">Test Quantum Circuit</button>
        <button class="button" @click="testQKD">Test QKD</button>
        <button class="button" @click="testMolecule">Test Molecule Generation</button>
        <button class="button" @click="testAttack">Test Attack Simulation</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_BASE_URL = 'http://localhost:5000/api'

export default {
  name: 'APITesting',
  data() {
    return {
      selectedEndpoint: 'circuits',
      httpMethod: 'GET',
      requestPayload: '',
      requestLog: '',
      responseLog: '',
      apiStatus: {
        quantum: false,
        cryptography: false,
        simulation: false
      }
    }
  },
  mounted() {
    this.checkAPIStatus()
  },
  methods: {
    async callAPI() {
      const endpoints = {
        'circuits': { url: '/quantum/circuits', method: 'GET' },
        'create-circuit': { url: '/quantum/circuits', method: 'POST' },
        'qkd': { url: '/cryptography/qkd/start', method: 'POST' },
        'qrng': { url: '/cryptography/qrng/generate', method: 'POST' },
        'molecule': { url: '/simulation/molecules/generate', method: 'POST' },
        'attack': { url: '/simulation/attacks/simulate', method: 'POST' }
      }
      
      const endpoint = endpoints[this.selectedEndpoint]
      if (!endpoint) return
      
      try {
        const config = {
          method: endpoint.method,
          url: `${API_BASE_URL}${endpoint.url}`,
          headers: {
            'Content-Type': 'application/json'
          }
        }
        
        if (this.requestPayload && endpoint.method !== 'GET') {
          config.data = JSON.parse(this.requestPayload)
        }
        
        this.requestLog = `${config.method} ${config.url}\n${JSON.stringify(config.data || {}, null, 2)}`
        
        const response = await axios(config)
        this.responseLog = `Status: ${response.status}\n${JSON.stringify(response.data, null, 2)}`
        
      } catch (error) {
        this.responseLog = `Error: ${error.message}\n${JSON.stringify(error.response?.data || {}, null, 2)}`
      }
    },
    
    async checkAPIStatus() {
      // Check Quantum API
      try {
        await axios.get(`${API_BASE_URL}/quantum/circuits`)
        this.apiStatus.quantum = true
      } catch {
        this.apiStatus.quantum = false
      }
      
      // Check Cryptography API
      try {
        await axios.get(`${API_BASE_URL}/cryptography/keys`)
        this.apiStatus.cryptography = true
      } catch {
        this.apiStatus.cryptography = false
      }
      
      // Check Simulation API
      try {
        await axios.get(`${API_BASE_URL}/simulation/molecules`)
        this.apiStatus.simulation = true
      } catch {
        this.apiStatus.simulation = false
      }
    },
    
    testQuantumCircuit() {
      this.selectedEndpoint = 'create-circuit'
      this.httpMethod = 'POST'
      this.requestPayload = JSON.stringify({
        name: 'Test Circuit',
        gates: ['H', 'X', 'CNOT'],
        qubits: 2
      }, null, 2)
    },
    
    testQKD() {
      this.selectedEndpoint = 'qkd'
      this.httpMethod = 'POST'
      this.requestPayload = JSON.stringify({
        keyLength: 256
      }, null, 2)
    },
    
    testMolecule() {
      this.selectedEndpoint = 'molecule'
      this.httpMethod = 'POST'
      this.requestPayload = JSON.stringify({
        type: 'h2o',
        temperature: 300,
        pressure: 1
      }, null, 2)
    },
    
    testAttack() {
      this.selectedEndpoint = 'attack'
      this.httpMethod = 'POST'
      this.requestPayload = JSON.stringify({
        protocol: 'BB84 Intercept-Resend'
      }, null, 2)
    }
  }
}
</script>
