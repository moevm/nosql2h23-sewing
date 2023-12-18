import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import {createApp} from 'vue'
import naive from "naive-ui";
import {createRouter, createWebHistory} from 'vue-router'
import App from './App.vue'
import Login from './Login.vue'
import ModelEditor from './admin/ModelEditor.vue'
import NewApplication from './admin/NewApplications.vue'
import Registration from "@/Registration";
import Constructor from "./Constructor";
import LoadModel from "./admin/LoadModel.vue";

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
            component: Registration,
        },
        {
            path: '/admin/load_model',
            component: LoadModel,
            meta: {
                requiresAuth: false
            }
        },
        {
            path: '/admin/new_applications',
            component: NewApplication,
            meta: {
                requiresAuth: false
            }
        },
        {
            path: '/admin/model_editor',
            component: ModelEditor,
            meta: {
                requiresAuth: false
            }
        },
    ],
    history: createWebHistory()
})

router.beforeEach((to, from, next) => {
    if (to.meta.requiresAuth) {
        const token = localStorage.getItem('token');
        if (token) {
            next();
        } else {
            next('/login');
        }
    } else {
        next();
    }
});

const app = createApp(App)
app.use(naive)
app.use(router)
app.mount("#app");
