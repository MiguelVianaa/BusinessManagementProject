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
        :api-route="'/api/setores/datatable/'"
        :columns="columns"
        :refresh-trigger="refreshTrigger"
        @edit="handleEdit"
        :delete-config="deleteConfig"
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

const router = useRouter()
const refreshTrigger = ref(0)

const columns = [
  { key: 'id', label: 'ID'},
  { key: 'nome', label: 'Setor'},
  { key: 'descricao', label: 'Descrição'},
]

const handleNewSetor = () => {
  router.push('/setores/show')
}

const handleEdit = (item: any) => {
  router.push(`/setores/editar/${item.id}`)
}

interface SetorItem {
  id: number;
  nome :string;
  [key: string]: any
}

const route = (id: number) => `/api/setores/${id}/`
const getId = (item: SetorItem) => item.id
const getName = (item: SetorItem) => item.nome

const deleteConfig = {
  route,
  title: 'Tem certeza que deseja excluir este setor?',
  msg: 'Você não poderá reverter essa ação.',
  confirmButtonName: 'Excluir',
  cancelButtonName: 'Cancelar',
  msgFailed: 'Erro ao excluir setor.',
  getId,
  getName
}

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