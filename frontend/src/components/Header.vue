<template>
  <header class="header">
    <img src="@/assets/logo.png" alt="Business Management" class="logo">
    <div class="auth-buttons">
      <!-- <button @click="navigateToLogin" class="btn btn-login">Login</button>-->
      <!-- <button @click="navigateToRegister" class="btn btn-register">Registrar</button>-->
    </div>
  </header>
</template>

<script setup lang="ts">
import {useRouter} from 'vue-router'

const router = useRouter()

const navigateToLogin = () => router.push('/login')
const navigateToRegister = () => router.push('/register')
</script>

<style scoped>
.header {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 4rem;
  background-color: #ffffff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  height: 80px;
}

.logo {
  max-height: 60px;
  width: auto;
  object-fit: contain;
  margin: 0;
}

.auth-buttons {
  display: flex;
  gap: 1rem;
}

.btn {
  padding: 0.7rem 1.5rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.3s ease;
  font-size: 1rem;
}

.btn-login {
  background-color: #fff;
  color: #2196f3;
  border: 1px solid #2196f3;
}

.btn-login:hover {
  background-color: #2196f3;
  color: #fff;
}

.btn-register {
  background-color: #2196f3;
  color: #fff;
}

.btn-register:hover {
  background-color: #1976d2;
}

@media (max-width: 768px) {
  .header {
    height: 70px;
    padding: 1rem;
    flex-direction: column;
    gap: 1rem;
  }

  .logo {
    max-height: 50px;
  }
}
</style>