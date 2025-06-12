<template>
  <div class="datatable-wrapper">
    <DataTable
        :options="tableOptions"
        class="table table-striped"
        ref="dataTableRef"
    >
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

DataTable.use(DataTablesCore)

interface Column {
  key: string;
  label: string;
}

interface Props {
  apiRoute: string,
  columns: Column[],
  refreshTrigger?: number
}

const props = defineProps<Props>()
const emit = defineEmits(['edit', 'delete', 'error'])
const dataTableRef = ref()

const tableOptions = {
  serverSide: true,
  processing: true,
  ajax: {
    dataSrc: '',
    url: props.apiRoute,
    error: (error: any) => {
      console.error('Erro ao buscar dados: ', error)
      emit('error', error)
    }
  },
  columns: [
      ...props.columns.map(column => ({
        data: column.key,
        title: column.label
      })),
    {
      data: null,
      orderable: false,
      render: function(data: any, type: string, row: any) {
        let buttons = "";
        buttons += `<button class="btn btn-sm btn-outline-primary edit-btn" title="Editar"> ✏️ </button>`
        buttons += `<button class="btn btn-sm btn-outline-danger delete-btn" title="Excluir"> 🗑️ </button>`
        return buttons;
      }
    }
  ],
  language: {
    url: '//cdn.datatables.net/plug-ins/1.13.7/i18n/pt-BR.json'
  },
  dom: 'Bfrtip',
  buttons: [
      'copy', 'csv', 'excel', 'pdf', 'print'
  ],
  pageLength: 10,
  responsive: true,
}

onMounted(() => {
  const table = dataTableRef.value.dt;

  table.on('click', 'button.delete-btn', function (e: MouseEvent) {
    const tr = (e.target as HTMLElement).closest('tr');
    const row = table.row(tr).data();
    emit('delete', row);
  });

  table.on('click', 'button.edit-btn', function (e: MouseEvent) {
    const target = e.target as HTMLElement;
    const tr = target.closest('tr');
    if (tr) {
      const row = table.row(tr).data();
      emit('edit', row);
    }
  });

  watch(() => props.refreshTrigger, () => {
    if (dataTableRef.value) {
      dataTableRef.value.dt.ajax.reload()
    }
  });

  watch(() => props.apiRoute, (newRoute) => {
    if (dataTableRef.value) {
      dataTableRef.value.dt.ajax.url(newRoute).load()
    }
  });
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
  margin: 0 0.25rem;
  border: 1px solid transparent;
  border-radius: 4px;
  cursor: pointer;
}

.btn-outline-primary:hover {
  background-color: #e8f0fe;
}

.btn-outline-danger:hover {
  background-color: #fee8e8;
}
</style>