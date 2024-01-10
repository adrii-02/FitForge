import { createRouter, createWebHistory } from 'vue-router';
import HomeComponent from '@/components/HomeComponent';
import LoginComponent from '@/components/LoginComponent';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomeComponent
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginComponent
    },
    // Añade aquí más rutas según sea necesario
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
