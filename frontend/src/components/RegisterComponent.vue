// Vue.js - RegistroComponent.vue
<template>
  <form @submit.prevent="register">
    <!-- Campos del formulario -->
    <button type="submit">Registrar</button>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: {
        username: '',
        password: '',
        // Otros campos...
      }
    };
  },
  methods: {
    register() {
      axios.post('http://localhost:8000/register/', this.user)
        .then(response => {
          // Manejar respuesta...
        })
        .catch(error => {
          // Manejar error...
        });
    }
  }
};
</script>
