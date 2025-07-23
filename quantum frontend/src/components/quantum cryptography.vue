
<template>
  <div class="grid">
    <div class="card">
      <h3>Quantum Key Distribution (QKD)</h3>
      <input class="input" v-model.number="keyLength" placeholder="Key Length (bits)">
      <button class="button" @click="startQKD">Start QKD Protocol</button>
      
      <div v-if="qkdResult" class="quantum-state">
        <strong>Key ID:</strong> {{ qkdResult.keyId }}<br>
        <strong>Key Length:</strong> {{ qkdResult.keyLength }} bits<br>
        <strong>Error Rate:</strong> {{ qkdResult.errorRate?.toFixed(2) }}%<br>
        <strong>Shared Key:</strong> {{ qkdResult.sharedKey?.substring(0, 32) }}...
      </div>
    </div>

    <div class="card">
      <h3>Quantum Random Number Generator</h3>
      <input class="input" v-model.number="randomBits" placeholder="Number of bits">
      <button class="button" @click="generateQuantumRandom">Generate</button>
      
      <div class="quantum-state" v-if="qrngResult">
        <strong>Random Bits:</strong> {{ qrngResult.binary?.substring(0, 32) }}...<br>
        <strong>Decimal:</strong> {{ qrngResult.decimal }}<br>
        <strong>Hex:</strong> {{ qrngResult.hex }}
      </div>
    </div>

    <div class="card">
      <h3>Post-Quantum Cryptography</h3>
      <select class="input" v-model="pqcAlgorithm">
        <option>CRYSTALS-Kyber</option>
        <option>CRYSTALS-Dilithium</option>
        <option>SPHINCS+</option>
        <option>FALCON</option>
      </select>
      
      <input class="input" v-model="pqcMessage" placeholder="Message to encrypt">
      <button class="button" @click="pqcEncrypt">Encrypt</button>
      <button class="button" @click="pqcDecrypt">Decrypt</button>
      
      <div class="quantum-state" v-if="pqcResult">
        <strong>Algorithm:</strong> {{ pqcResult.algorithm }}<br>
        <strong>Encrypted:</strong> {{ pqcResult.encrypted?.substring(0, 50) }}...<br>
        <strong>Decrypted:</strong> {{ pqcResult.decrypted }}
      </div>
    </div>

    <div class="card">
      <h3>Generated Keys</h3>
      <button class="button" @click="loadKeys">Refresh Keys</button>
      
      <div class="key-list">
        <div v-for="key in keys" :key="key.keyId" class="key-item">
          <div class="key-info">
            <strong>{{ key.keyId.substring(0, 8) }}...</strong>
            <span>{{ key.keyLength }} bits</span>
            <span>{{ key.protocol }}</span>
            <span>Error: {{ key.errorRate?.toFixed(2) }}%</span>
          </div>
          <div class="key-time">
            {{ new Date(key.generatedAt).toLocaleString() }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { cryptographyAPI } from '../services/api'

export default {
  name: 'QuantumCryptography',
  data() {
    return {
      keyLength: 256,
      qkdResult: null,
      randomBits: 128,
      qrngResult: null,
      pqcAlgorithm: 'CRYSTALS-Kyber',
      pqcMessage: '',
      pqcResult: null,
      keys: []
    }
  },
  mounted() {
    this.loadKeys()
  },
  methods: {
    async startQKD() {
      try {
        const response = await cryptographyAPI.startQKD({ keyLength: this.keyLength })
        this.qkdResult = response.data
        this.loadKeys()
      } catch (error) {
        console.error('Error starting QKD:', error)
      }
    },
    
    async generateQuantumRandom() {
      try {
        const response = await cryptographyAPI.generateQuantumRandom({ bits: this.randomBits })
        this.qrngResult = response.data
      } catch (error) {
        console.error('Error generating quantum random:', error)
      }
    },
    
    async pqcEncrypt() {
      if (!this.pqcMessage) {
        alert('Please enter a message to encrypt')
        return
      }
      
      try {
        const response = await cryptographyAPI.encryptPQC({
          message: this.pqcMessage,
          algorithm: this.pqcAlgorithm
        })
        this.pqcResult = response.data
      } catch (error) {
        console.error('Error encrypting:', error)
      }
    },
    
    async pqcDecrypt() {
      if (!this.pqcResult?.encrypted) {
        alert('No encrypted message to decrypt')
        return
      }
      
      try {
        const response = await cryptographyAPI.decryptPQC({
          encrypted: this.pqcResult.encrypted,
          algorithm: this.pqcAlgorithm
        })
        this.pqcResult.decrypted = response.data.decrypted
      } catch (error) {
        console.error('Error decrypting:', error)
      }
    },
    
    async loadKeys() {
      try {
        const response = await cryptographyAPI.getKeys()
        this.keys = response.data
      } catch (error) {
        console.error('Error loading keys:', error)
      }
    }
  }
}
</script>
