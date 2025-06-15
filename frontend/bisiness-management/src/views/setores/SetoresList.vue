<template>
  <div class="setores-view">
    <Header />
    <PageContainer title="Setores" :showBackButton="true">
      <template #actions>
        <button class="btn-primary" @click="handleNewSetor">
          Novo Setor
        </button>
      </template>

      <DataTable
          :api-route="'/api/setores/'"
          :columns="columns"
          :refresh-trigger="refreshTrigger"
          @edit="handleEdit"
          @delete="handleDelete"
      />
    </PageContainer>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from "vue-router";
import Header from "@/components/Header.vue";
import PageContainer from "@/components/PageContainer.vue";
import DataTable from "@/components/DataTable.vue";
import axios from 'axios';

const router = useRouter()
const refreshTrigger = ref(0)

const columns = [
  { key: 'nome', label: 'Setor'},
  { key: 'descricao', label: 'Descrição'},
]

const handleNewSetor = () => {
  router.push('/setores/show')
}

const handleEdit = (item: any) => {
  router.push(`/setores/editar/${item.id}`)
}

const handleDelete = async (item: any) => {
  if (confirm('Deseja realmente excluir este setor?')) {
    try {
      await axios.delete(`/api/setores/${item.id}`);
      refreshTrigger.value++;
    } catch (error) {
      console.error('Erro ao excluir:', error);
      alert('Erro ao excluir o setor');
    }
  }
};

</script>

<style scoped>
.setores-view {
  min-height: 100vh;
  background-color: #f5f5f5;
}

.btn-primary {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s ease;
}

.btn-primary:hover {
  background-color: #45a049;
}

</style>