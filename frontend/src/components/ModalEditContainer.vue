<template>
  <v-dialog v-model="open" :width="width">
    <v-card>
      <v-card-title class="d-flex justify-center">
        <span class="text-h5">{{ title }}</span>
      </v-card-title>
      <v-card-text>
        <slot
            :data="data"
            :loading="loading"
            :error="error"
            :refresh="fetchData"
            :close="close"
        >
          <div v-if="loading">Carregando...</div>
          <div v-else-if="error" class="text-error">Erro ao carregar dados.</div>
        </slot>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import {ref, watch, defineProps, defineEmits} from 'vue'
import axios from 'axios'

const props = defineProps<{
  modelValue: boolean,
  apiRoute: string,
  title?: string,
  width?: string | number,
  fetchOnOpen?: boolean
}>()
const emit = defineEmits(['update:modelValue', 'loaded', 'error'])

const open = ref(props.modelValue)
const loading = ref(false)
const error = ref<null | any>(null)
const data = ref<any>(null)

watch(() => props.modelValue, v => {
  open.value = v
  if (v && props.fetchOnOpen){
    fetchData();
  }
})
watch(open, v => emit('update:modelValue', v))

async function fetchData() {
  if (!props.apiRoute) return
  loading.value = true
  error.value = null
  try {
    const res = await axios.get(props.apiRoute)
    data.value = res.data
    emit('loaded', data.value)
  } catch (e) {
    error.value = e
    emit('error', e)
  } finally {
    loading.value = false
  }
}

function close() {
  open.value = false
}
</script>