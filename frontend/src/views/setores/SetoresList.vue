<template>
  <div class="setores-view">
    <Header/>
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

  <ModalEditContainer v-model="modalOpen" :api-route="editId !== null ? `/api/setores/${editId}/` : ''" :fetch-on-open="true" title="Editar Setor" width="70%">
    <template #default="{ data, loading, error, close, refresh }">
      <SetorEditForm v-if="data" :model="data" @submit="salvarSetor" />
      <div v-else-if="loading">Carregando...</div>
      <div v-else-if="error">Erro ao carregar dados.</div>
    </template>
  </ModalEditContainer>
</template>

<script setup lang="ts">
import {ref} from 'vue';
import {useRouter} from "vue-router";
import Header from "@/components/Header.vue";
import PageContainer from "@/components/PageContainer.vue";
import DataTable from "@/components/DataTable.vue";
import ModalEditContainer from "@/components/ModalEditContainer.vue";
import SetorEditForm from "@/views/setores/SetorEditForm.vue";

const router = useRouter()
const refreshTrigger = ref(0)

const columns = [
  {key: 'id', label: 'ID'},
  {key: 'nome', label: 'Setor'},
  {key: 'descricao', label: 'Descrição'},
]

const handleNewSetor = () => {
  router.push('/setores/show')
}

interface SetorItem {
  id: number;
  nome: string;
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

const modalOpen = ref(false)
const editId = ref<number | null>(null)

function handleEdit(item: any) {
  editId.value = item.id
  modalOpen.value = true
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