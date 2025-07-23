
<template>
  <div class="container">
    <div class="header">
      <h1>Quantum Computing & Cryptography Laboratory</h1>
      <p>Comprehensive simulation of quantum systems, cryptography protocols, and full-stack quantum applications</p>
    </div>

    <div class="tabs">
      <button class="tab" :class="{active: activeTab === 'quantum'}" @click="activeTab = 'quantum'">
        Quantum Simulation
      </button>
      <button class="tab" :class="{active: activeTab === 'crypto'}" @click="activeTab = 'crypto'">
        Quantum Cryptography
      </button>
      <button class="tab" :class="{active: activeTab === 'attacks'}" @click="activeTab = 'attacks'">
        Attack Simulation
      </button>
      <button class="tab" :class="{active: activeTab === 'api'}" @click="activeTab = 'api'">
        API Testing
      </button>
    </div>

    <!-- Quantum Simulation Tab -->
    <div class="tab-content" :class="{active: activeTab === 'quantum'}">
      <QuantumSimulation />
    </div>

    <!-- Quantum Cryptography Tab -->
    <div class="tab-content" :class="{active: activeTab === 'crypto'}">
      <QuantumCryptography />
    </div>

    <!-- Attack Simulation Tab -->
    <div class="tab-content" :class="{active: activeTab === 'attacks'}">
      <AttackSimulation />
    </div>

    <!-- API Testing Tab -->
    <div class="tab-content" :class="{active: activeTab === 'api'}">
      <APITesting />
    </div>
  </div>
</template>

<script>
import QuantumSimulation from './components/QuantumSimulation.vue'
import QuantumCryptography from './components/QuantumCryptography.vue'
import AttackSimulation from './components/AttackSimulation.vue'
import APITesting from './components/APITesting.vue'

export default {
  name: 'App',
  components: {
    QuantumSimulation,
    QuantumCryptography,
    AttackSimulation,
    APITesting
  },
  data() {
    return {
      activeTab: 'quantum'
    }
  }
}
</script>
</template>
