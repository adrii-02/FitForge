<template>
    <!--
    <div>
        <input v-model="username" type="text" placeholder="Username">
        <input v-model="password" type="password" placeholder="Password">
        <button @click="login">Login</button>
    </div>
    -->

    <div class="mainContainer">
        <form>
            <div class="mb-3">
                <!--<label for="exampleInputEmail1" class="form-label">Email address</label>-->
                <input v-model="username" type="email" placeholder="Username" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                <!--<div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>-->
            </div>
            <div class="mb-3">
                <!--<label for="exampleInputPassword1" class="form-label">Password</label>-->
                <input v-model="password" type="password" placeholder="Password" class="form-control" id="exampleInputPassword1">
            </div>
            <!--
            <div class="mb-3 form-check">
                <input type="checkbox" class="form-check-input" id="exampleCheck1">
                <label class="form-check-label" for="exampleCheck1">Check me out</label>
            </div>
            -->
            <button type="submit" class="btn btn-primary" @click="login">Login</button>
        </form>
    </div>
</template>

<script>
import AuthService from '../services/auth_service';

export default {
    data() {
        return {
            username: '',
            password: ''
        };
    },
    methods: {
        login() {
            AuthService.login({ username: this.username, password: this.password })
                .then(
                    () => this.$router.push({ name: 'home' }),
                    error => console.log(error)
                );
        }
    }
};
</script>
<style>
    .mainContainer {
        display: flex;
        flex-direction: column;
        margin-left: 25%;
        margin-right: 25%;
        align-self: center;
        /*border: solid 1px black;*/
    }

    .mainContainer form {
        width: 100%; /* Ajusta este valor según sea necesario */
    }

    .mb-3 {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .form-label {
        align-self: flex-start;
        margin-bottom: 5px; /* Espacio entre el título y el input */
    }

    .form-control, .btn {
        width: 50%; /* Ajusta el ancho de los inputs y el botón */
        margin: auto; /* Centra los inputs y el botón horizontalmente */
    }
</style>