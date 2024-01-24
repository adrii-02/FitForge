import { createApp } from 'vue';
import App from './App.vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import router from './router'; // Asegúrate de que la ruta sea correcta
import http from './services/http_common'; // Asegúrate de que la ruta sea correcta

const app = createApp(App);

app.config.globalProperties.$http = http; // Configurar Axios globalmente
app.use(router); // Usar el enrutador Vue

app.mount('#app');
