import {createRouter, createWebHistory} from 'vue-router'
import Home from './pages/Home.vue'
import Login from './pages/Login.vue'
import Register from "./pages/Register.vue";
import dashboard from "./pages/dashboard.vue";
const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/register',
        name: 'register',
        component: Register
    },
    {
        path: '/dashboard',
        name: 'dashboard',
        component: dashboard
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
