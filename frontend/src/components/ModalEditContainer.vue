<template>
  <v-dialog v-model="open" :max-width="maxWidth" persistent>
    <v-card>
      <v-card-title class="d-flex align-center justify-space-between">
        <span class="text-h6" style="flex: 1; text-align: left;">{{ title }}</span>
        <v-btn icon @click="close" class="close-btn" aria-label="Fechar" variant="plain">
          x
        </v-btn>
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

debugger

const props = defineProps<{
  modelValue: boolean,
  apiRoute: string,
  title?: string,
  maxWidth?: string | number,
  fetchOnOpen?: boolean
}>()
const emit = defineEmits(['update:modelValue', 'loaded', 'error'])

debugger

const open = ref(props.modelValue)
const loading = ref(false)
const error = ref<null | any>(null)
const data = ref<any>(null)

watch(() => props.modelValue, v => {
  debugger
  open.value = v
  if (v && props.fetchOnOpen !== false) fetchData()
})
watch(open, v => emit('update:modelValue', v))

async function fetchData() {
  if (!props.apiRoute) return
  loading.value = true
  error.value = null
  try {
    debugger
    const res = await axios.get(props.apiRoute)
    data.value = res.data
    emit('loaded', data.value)
  } catch (e) {
    debugger
    error.value = e
    emit('error', e)
  } finally {
    debugger
    loading.value = false
  }
}

function close() {
  open.value = false
}

</script>

<style scoped>
.close-btn {
  background: none !important;
  box-shadow: none !important;
  margin-left: auto;
}

.text-error {
  color: #f44336;
  text-align: center;
}
</style>