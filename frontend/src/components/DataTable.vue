<template>
  <div class="datatable-wrapper">
    <DataTable :options="tableOptions" class="table table-striped" ref="dataTableRef">
      <thead>
      <tr>
        <th v-for="column in columns" :key="column.key">
          {{ column.label }}
        </th>
        <th>Ações</th>
      </tr>
      </thead>
    </DataTable>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from "vue";
import { DataTable } from "datatables.net-vue3";
import DataTablesCore from 'datatables.net-bs5';
import 'datatables.net-bs5/css/dataTables.bootstrap5.min.css';
import 'datatables.net-buttons-bs5/css/buttons.bootstrap5.min.css';
// 1. Importe o novo composable
import { useConfirmDelete } from "@/composables/useConfirmDelete";

DataTable.use(DataTablesCore);

interface Column { key: string; label: string; }
interface Props {
  apiRoute: string,
  columns: Column[],
  refreshTrigger?: number,
  deleteConfig: any // A prop continua aqui, perfeita!
}

const props = defineProps<Props>();
const emit = defineEmits(['edit', 'error']); // O emit 'delete' não é mais necessário
const dataTableRef = ref();

// O tableOptions permanece o mesmo...
const tableOptions = {
  // ... (todo o seu objeto de opções aqui, sem alterações)
  serverSide: true,
  processing: true,
  ajax: { dataSrc: 'data', url: props.apiRoute, error: (error: any) => { console.error('Erro ao buscar dados: ', error); emit('error', error) } },
  columns: [
    ...props.columns.map(column => ({ data: column.key, title: column.label })),
    {
      data: null, orderable: false, render: function (data: any, type: string, row: any) {
        return `<div style="display: flex; gap: 0.5rem; justify-content: center;"><button class="btn btn-sm btn-outline-primary edit-btn" title="Editar"><i class="bi bi-pencil-square"></i></button><button class="btn btn-sm btn-outline-danger delete-btn" title="Excluir"><i class="bi bi-trash-fill"></i></button></div>`;
      }
    }
  ],
  language: { url: 'https://cdn.datatables.net/plug-ins/1.13.7/i18n/pt-BR.json' },
  dom: 'Bfrtip', buttons: ['copy', 'csv', 'excel', 'pdf', 'print'], pageLength: 10, responsive: true,
};

// 2. A lógica de callback continua a mesma, mas agora será chamada pelo composable
function onDeleted() {
  if (dataTableRef.value) dataTableRef.value.dt.ajax.reload();
}

function onDeleteError(e: any) {
  // Não tratamos o 'cancelled' como um erro real
  if (e !== 'cancelled') {
    emit('error', e);
  }
}

onMounted(() => {
  const table = dataTableRef.value.dt;

  // O evento de 'edit' não muda
  table.on('click', 'button.edit-btn', function (e: MouseEvent) {
    const target = e.target as HTMLElement;
    const tr = target.closest('tr');
    if (tr) {
      const row = table.row(tr).data();
      emit('edit', row);
    }
  });

  // 3. ✨ AQUI ESTÁ A MÁGICA ✨
  // O evento de 'delete' agora chama o nosso composable
  table.on('click', 'button.delete-btn', function (e: MouseEvent) {
    const tr = (e.target as HTMLElement).closest('tr');
    if (tr) {
      const rowData = table.row(tr).data();
      // Chama o composable passando o item e o config recebido via props
      useConfirmDelete(rowData, props.deleteConfig)
          .then(() => {
            // SUCEsSO: A tabela é recarregada
            onDeleted();
          })
          .catch((error) => {
            // ERRO: O erro é emitido (ou ignorado se for apenas um cancelamento)
            onDeleteError(error);
          });
    }
  });

  // Os watchers não mudam
  watch(() => props.refreshTrigger, () => { if (dataTableRef.value) { dataTableRef.value.dt.ajax.reload() } });
  watch(() => props.apiRoute, (newRoute) => { if (dataTableRef.value) { dataTableRef.value.dt.ajax.url(newRoute).load() } });
});
</script>

<style scoped>
@import 'datatables.net-bs5/css/dataTables.bootstrap5.min.css';
@import 'datatables.net-buttons-bs5/css/buttons.bootstrap5.min.css';

.datatable-wrapper {
  padding: 1rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.btn-sm {
  padding: 0.25rem 0.5rem;
  border: 1px solid transparent;
  border-radius: 4px;
  cursor: pointer;
  margin: 0;
}

th:last-child,
td:last-child {
  text-align: center;
  vertical-align: middle;
  min-width: 110px;
}
</style>