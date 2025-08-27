import './assets/main.css';
import { createApp } from 'vue';
import App from './App.vue';
import router from "@/router";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-icons/font/bootstrap-icons.css';
import 'vuetify/styles';
import { createVuetify } from "vuetify";
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css'

const vuefity = createVuetify({components, directives });

const app = createApp(App);
app.use(router);
app.use(vuefity);
app.use(VueSweetalert2);
app.mount('#app');