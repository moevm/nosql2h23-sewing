import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import {createApp} from 'vue'
import naive from "naive-ui";
import {createRouter, createWebHistory} from 'vue-router'
import App from './App.vue'
import Login from './Login.vue'
import Registration from "@/Registration";
import Constructor from "./Constructor";
// import TestLogin from './TestLogin'

const router = createRouter({
    routes: [
        {
            path: '/',
            component: Constructor
        },
        {
            path: '/login',
            component: Login
        },
        {
            path: '/registration',
            component: Registration
        }
    ],
    history: createWebHistory()
})

const app = createApp(App)
app.use(naive)
app.use(router)
app.mount("#app");
