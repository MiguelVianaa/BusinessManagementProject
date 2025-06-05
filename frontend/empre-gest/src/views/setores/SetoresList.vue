<template>
  <ul>
    <li v-for="setor in setores" :key="setor.id">{{ setor.nome }}</li>
  </ul>
</template>
<script setup>
  import { ref, onMounted } from "vue"
  import axios from 'axios'

  const setores = ref([])

  onMounted(async () => {
    const response = await axios.get('http://localhost:8000/api/setores')
    setores.value = response.data
  });


</script>