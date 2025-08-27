<template>
  <v-dialog
      v-model="open"
      max-width="450"
      persistent
  >
    <v-card class="text-center pa-2">

      <v-card-text class="pt-5">
        <div class="sa-icon sa-error">
          <span class="sa-x-mark">
            <span class="sa-line sa-left"></span>
            <span class="sa-line sa-right"></span>
          </span>
        </div>
      </v-card-text>

      <v-card-title class="text-h5 text-wrap font-weight-bold">
        {{ config.title }}
      </v-card-title>

      <v-card-text class="pt-0">
        <div class="mb-4">{{ config.msg }}</div>

        <div v-if="config.getName && item" class="font-weight-bold mt-4">
          {{ config.getName(item) }}
        </div>
      </v-card-text>

      <v-card-actions class="pb-4">
        <v-spacer></v-spacer>
        <v-btn
            @click="close"
            variant="text"
            size="large"
        >
          {{ config.cancelButtonName || 'Cancelar' }}
        </v-btn>
        <v-btn
            color="error"
            variant="elevated"
            @click="confirm"
            size="large"
        >
          {{ config.confirmButtonName || 'Excluir' }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <v-snackbar v-model="snackbarShow" :color="snackbarColor" location="top right">
    {{ snackbarMsg }}
  </v-snackbar>
</template>

<script setup lang="ts">
import { ref, watch, defineProps, defineEmits } from 'vue';
import axios from 'axios';
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

const props = defineProps<{
  config: any,
  show: boolean,
  item: any
}>();
const emit = defineEmits(['update:show', 'deleted', 'error']);
const open = ref(props.show);
watch(() => props.show, v => open.value = v);
watch(open, v => emit('update:show', v));
const snackbarShow = ref(false);
const snackbarMsg = ref('');
const snackbarColor = ref('error');
function close() { open.value = false; }
async function confirm() {
  try {
    await axios.delete(props.config.route(props.item));
    open.value = false;
    snackbarMsg.value = props.config.msgSuccess || 'Excluído com sucesso!';
    snackbarColor.value = 'success';
    snackbarShow.value = true;
    emit('deleted', props.item);
  } catch (e) {
    snackbarMsg.value = props.config.msgFailed || 'Erro ao excluir.';
    snackbarColor.value = 'error';
    snackbarShow.value = true;
    emit('error', e);
  }
}
</script>

<style scoped>
.sa-icon {
  width: 80px;
  height: 80px;
  border: 4px solid #F44336;
  border-radius: 50%;
  margin: 0 auto 16px;
  position: relative;
  box-sizing: content-box;
  animation: scale-in 0.3s forwards;
}
.sa-icon.sa-error .sa-x-mark {
  position: relative;
  display: block;
}
.sa-icon.sa-error .sa-line {
  position: absolute;
  height: 5px;
  width: 47px;
  background-color: #F44336;
  display: block;
  top: 37px;
  border-radius: 2px;
}
.sa-icon.sa-error .sa-line.sa-left {
  transform: rotate(45deg);
  left: 17px;
  animation: draw-x-left 0.3s 0.1s forwards;
}
.sa-icon.sa-error .sa-line.sa-right {
  transform: rotate(-45deg);
  right: 16px;
  animation: draw-x-right 0.3s 0.1s forwards;
}
@keyframes scale-in {
  0% { transform: scale(0); opacity: 0; }
  100% { transform: scale(1); opacity: 1; }
}
@keyframes draw-x-left {
  0% { width: 0; left: 40px; }
  100% { width: 47px; left: 17px; }
}
@keyframes draw-x-right {
  0% { width: 0; right: 40px; }
  100% { width: 47px; right: 16px; }
}
</style>