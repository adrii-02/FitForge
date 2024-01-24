import { createRouter, createWebHistory } from 'vue-router';
import UserList from '../components/UserList.vue';
import UserLogin from '../components/UserLogin.vue';
import UserRegister from '../components/UserRegister.vue';

const routes = [
    {
        path: '/',
        name: 'users',
        component: UserList,
        meta: { requiresAuth: true }
    },
    {
        path: '/login',
        name: 'login',
        component: UserLogin
    },
    {
        path: '/register',
        name: 'register',
        component: UserRegister
    }
    // otras rutas...
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach((to, from, next) => {
    const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
    const currentUser = JSON.parse(localStorage.getItem('user'));

    if (requiresAuth && !currentUser) {
        next('/login');
    } else {
        next();
    }
});

export default router;
