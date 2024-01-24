<template>
    <div>
        <h2>Lista de Usuarios</h2>
        <table class="table table-striped">
        <thead>
            <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Email</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="user in users" :key="user.id">
            <td>{{ user.id }}</td>
            <td>{{ user.username }}</td>
            <td>{{ user.email }}</td>
            </tr>
        </tbody>
        </table>
    </div>
</template>
  
  
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'UserList',
    data() {
      return {
        users: []
      };
    },
    mounted() {
      this.fetchUsers();
    },
    methods: {
      fetchUsers() {
        axios.get('http://127.0.0.1:8000/users/')
          .then(response => {
            console.log(response.data);
            this.users = response.data;
          })
          .catch(error => {
            console.error('Error al obtener los usuarios:', error);
          });
      }
    }
  };
  </script>
  