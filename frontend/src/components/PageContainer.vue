<template>
  <div class="page-container">
    <div class="page-header">
      <div class="btn-back-container">
        <button
            v-if="showBackButton"
            class="btn-back"
            @click="goBack"
            :title="backButtonTitle"
        >
          ← Voltar
        </button>
      </div>
      <h1 class="page-title">{{ title }}</h1>
      <div class="page-actions">
        <slot name="actions"></slot>
      </div>
    </div>
    <div class="page-content">
      <slot></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

interface Props {
  title: string
  showBackButton?: boolean
  backButtonTitle?: string
}

const props = withDefaults(defineProps<Props>(), {
  showBackButton: true,
  backButtonTitle: 'Voltar para a página anterior'
})

const router = useRouter()

const goBack = () => {
  router.back()
}

defineExpose({
  goBack
})
</script>

<style scoped>
.page-container {
  padding: 2rem;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: 2rem;
  min-height: calc(100vh - 4rem);
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #e0e0e0;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.page-title {
  font-size: 1.75rem;
  color: #333;
  margin: 0;
}

.page-actions {
  display: flex;
  gap: 1rem;
}

.page-content {
  background-color: #fff;
}

.btn-back {
  display: flex;
  align-items: center;
  padding: 0.5rem 1rem;
  background-color: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
  color: #666;
  transition: all 0.3s ease;
}

.btn-back:hover {
  background-color: #e5e5e5;
  color: #333;
}

.btn-back:active {
  transform: translateY(1px);
}
</style>