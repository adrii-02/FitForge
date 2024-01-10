<template>
    <div>
      <h1>Registrarse</h1>
      <form @submit.prevent="register">
        <input v-model="user.username" type="text" placeholder="Nombre de usuario" />
        <input v-model="user.email" type="email" placeholder="Correo electrónico" />
        <input v-model="user.password" type="password" placeholder="Contraseña" />
        <!-- Añade más campos según sea necesario -->
        <button type="submit">Registrarse</button>
      </form>
      <!-- Mensaje de error si el registro falla -->
      <p v-if="error">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'RegisterComponent',
    data() {
      return {
        user: {
          username: '',
          email: '',
          password: ''
          // Agrega más campos según lo requieras
        },
        error: false,
        errorMessage: ''
      };
    },
    methods: {
      async register() {
        try {
          const response = await axios.post('/api/register/', this.user);
          // Manejar la respuesta
          if (response.data.status === 'success') {
            // Manejar el éxito del registro, como redirigir o mostrar un mensaje
          } else {
            this.error = true;
            this.errorMessage = 'Registro fallido';
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
  /* Estilos específicos de RegisterComponent */
  </style>
  