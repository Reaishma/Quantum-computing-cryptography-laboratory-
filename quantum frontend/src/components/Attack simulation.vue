
<template>
  <div class="grid">
    <div class="card">
      <h3>Quantum Attack Simulation</h3>
      <select class="input" v-model="attackProtocol">
        <option>BB84 Intercept-Resend</option>
        <option>Man-in-the-Middle</option>
        <option>Photon Number Splitting</option>
        <option>Trojan Horse</option>
      </select>
      
      <button class="button danger" @click="simulateAttack">Launch Attack</button>
      
      <div class="stats" v-if="attackResult">
        <div class="stat">
          <div class="stat-value">{{ attackResult.successRate }}%</div>
          <div class="stat-label">Success Rate</div>
        </div>
        <div class="stat">
          <div class="stat-value">{{ attackResult.detectionRate }}%</div>
          <div class="stat-label">Detection Rate</div>
        </div>
      </div>
      
      <div class="quantum-state" v-if="attackResult">
        <strong>Protocol:</strong> {{ attackResult.protocol }}<br>
        <strong>Description:</strong> {{ attackResult.description }}
      </div>
    </div>

    <div class="card">
      <h3>Attack History</h3>
      <div class="attack-list">
        <div v-for="(attack, index) in attackHistory" :key="index" class="attack-item">
          <div class="attack-info">
            <strong>{{ attack.protocol }}</strong>
            <span>Success: {{ attack.successRate }}%</span>
            <span>Detection: {{ attack.detectionRate }}%</span>
          </div>
          <div class="attack-time">
            {{ attack.timestamp }}
          </div>
        </div>
      </div>
    </div>

    <div class="card">
      <h3>Security Recommendations</h3>
      <div class="recommendations">
        <div class="recommendation" v-for="(rec, index) in recommendations" :key="index">
          <h4>{{ rec.title }}</h4>
          <p>{{ rec.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { simulationAPI } from '../services/api'

export default {
  name: 'AttackSimulation',
  data() {
    return {
      attackProtocol: 'BB84 Intercept-Resend',
      attackResult: null,
      attackHistory: [],
      recommendations: [
        {
          title: 'Use Decoy States',
          description: 'Implement decoy state protocols to detect photon number splitting attacks.'
        },
        {
          title: 'Monitor Error Rates',
          description: 'Continuously monitor quantum bit error rates to detect eavesdropping attempts.'
        },
        {
          title: 'Implement Authentication',
          description: 'Use classical authentication methods to prevent man-in-the-middle attacks.'
        },
        {
          title: 'Regular Security Audits',
          description: 'Perform regular security assessments of quantum communication systems.'
        }
      ]
    }
  },
  methods: {
    async simulateAttack() {
      try {
        const response = await simulationAPI.simulateAttack({
          protocol: this.attackProtocol
        })
        
        this.attackResult = response.data
        
        // Add to history
        this.attackHistory.unshift({
          ...response.data,
          timestamp: new Date().toLocaleString()
        })
        
        // Keep only last 10 attacks
        if (this.attackHistory.length > 10) {
          this.attackHistory = this.attackHistory.slice(0, 10)
        }
        
      } catch (error) {
        console.error('Error simulating attack:', error)
      }
    }
  }
}
</script>
