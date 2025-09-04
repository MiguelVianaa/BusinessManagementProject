<template>
  <v-form @submit.prevent="onSubmit" ref="formRef" v-if="model">
    <v-row>
      <v-col cols="12">
        <v-text-field
            v-model="model.nome"
            label="Nome do Setor"
            :rules="[v => !!v || 'O nome do setor é obrigatório']"
            required
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-textarea
            v-model="model.descricao"
            label="Descrição"
            rows="1"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" class="d-flex justify-center">
        <v-btn color="primary" type="submit">Salvar</v-btn>
      </v-col>
    </v-row>
  </v-form>
</template>

<script setup lang="ts">

import { ref, watch, toRef } from 'vue'

const props = defineProps<{ model: any }>()
const emit = defineEmits(['submit'])
const formRef = ref()
const model = ref({ ...props.model })

watch(() => props.model, v => {
  model.value = { ...v }
})

function onSubmit() {
  emit('submit', model.value)
}

</script>

<style scoped>

</style>