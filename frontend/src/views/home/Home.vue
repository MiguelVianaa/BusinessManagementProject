<template>
  <div class="home-container">
    <Header/>

    <!-- Container principal -->
    <main class="main-content">
      <h2 class="welcome-text">Bem-vindo ao Sistema de Gestão de Empresas</h2>

      <!-- Grid de módulos -->
      <div class="modules-grid">
        <div v-for="module in modules"
             :key="module.name"
             class="module-card"
             @click="navigateToModule(module.route)">
          <span class="module-icon">{{ module.icon }}</span>
          <h3>{{ module.name }}</h3>
          <p>{{ module.description }}</p>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import {useRouter} from 'vue-router'
import Header from "@/components/Header.vue";

const router = useRouter()

const modules = [
  {
    name: 'Colaboradores',
    description: 'Gestão de funcionários e equipe',
    route: '/colaboradores',
    icon: '👥'
  },
  {
    name: 'Empresas',
    description: 'Cadastro e gestão de empresas',
    route: '/empresas',
    icon: '🏢'
  },
  {
    name: 'Setores',
    description: 'Organização de departamentos',
    route: '/setores',
    icon: '🏗️'
  },
  {
    name: 'Cargos',
    description: 'Gerenciamento de funções',
    route: '/cargos',
    icon: '💼'
  }
]

const navigateToModule = (route: string) => router.push(route)
</script>

<style scoped>
/* @import './Home.css'; */
.home-container {
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
}

.main-content {
  flex: 1;
  padding: 3rem 4rem;
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
}

.welcome-text {
  text-align: center;
  color: #333;
  font-size: 2.5rem;
  margin-bottom: 4rem;
}

.modules-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
  padding: 1rem;
  width: 100%;
}

.module-card {
  background-color: #fff;
  border-radius: 12px;
  padding: 2rem;
  text-align: center;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  height: 100%;
  min-height: 250px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.module-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0,0,0,0.1);
}

.module-icon {
  font-size: 3.5rem;
  margin-bottom: 1.5rem;
  display: block;
}

.module-card h3 {
  color: #333;
  margin: 0.5rem 0;
  font-size: 1.5rem;
}

.module-card p {
  color: #666;
  font-size: 1rem;
  margin: 0.5rem 0 0 0;
}

@media (max-width: 1024px) {
  .header {
    padding: 1rem 2rem;
  }

  .main-content {
    padding: 2rem;
  }

  .modules-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .welcome-text {
    font-size: 2rem;
    margin-bottom: 3rem;
  }
}
</style>