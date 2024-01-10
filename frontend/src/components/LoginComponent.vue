<template>
    <div>
      <h1>Iniciar Sesión</h1>
      <form @submit.prevent="login">
        <input v-model="credentials.username" type="text" placeholder="Nombre de usuario" />
        <input v-model="credentials.password" type="password" placeholder="Contraseña" />
        <button type="submit">Iniciar Sesión</button>
      </form>
      <!-- Mensaje de error si el inicio de sesión falla -->
      <p v-if="error">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'LoginComponent',
    data() {
      return {
        credentials: {
          username: '',
          password: ''
        },
        error: false,
        errorMessage: ''
      };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('/api/login/', this.credentials);
          // Manejar la respuesta
          if (response.data.status === 'success') {
            // Redireccionar al usuario o cambiar el estado de autenticación
          } else {
            this.error = true;
            this.errorMessage = 'Inicio de sesión fallido';
          }
        } catch (error) {
          this.error = true;
          this.errorMessage = 'Error de servidor';
        }
      }
    }
  };
  </script>
  
  <style>
  /* Estilos específicos de LoginComponent */
  </style>
  