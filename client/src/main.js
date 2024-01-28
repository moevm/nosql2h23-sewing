import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import {createApp} from 'vue'
import naive from "naive-ui";
import {createRouter, createWebHistory} from 'vue-router'
import App from './App.vue'
import Registration from "./Registration.vue";
import Login from './Login.vue'
import WaitPage from "./WaitPage.vue";
import CustomerProfile from './customer/Profile'
import CompanyProfile from './company/Profile'

import Constructor from "./customer/Constructor.vue";

import AdminLogin from "./admin/AdminLogin";
import CreateManager from "./admin/CreateManager";
import ModelList from './admin/ModelList.vue'
import Customers from './admin/Customers'
import Companies from './admin/Companies'
import CompanyEditor from './admin/CompanyEditor'
import CustomerEditor from './admin/CustomerEditor'
import ModelEditor from './admin/ModelEditor.vue'
import NewApplication from './admin/NewApplications.vue'
import LoadModel from "./admin/LoadModel.vue";
import ConstructorSettings from "./admin/ConstructorSettings";

const router = createRouter({
    routes: [
        {
            path: "/constructor",
            name: "Конструктор",
            component: Constructor,
            meta: {
                requiresAuth: false
            }
        },
        {
            path: "/customer/profile",
            name: "Личный кабинет заказчика",
            component: CustomerProfile,
            meta: {
                requiresAuth: false
            }
        },
        {
            path: "/company/profile",
            name: "Личный кабинет производителя",
            component: CompanyProfile,
            meta: {
                requiresAuth: false
            }
        },
        {
            path: "/login",
            name: "Авторизация",
            component: Login,
            meta: {
                requiresAuth: false
            }
        },
        {
            path: "/admin/login",
            name: "Админ Панель",
            component: AdminLogin,
            meta: {
                requiresAuth: false
            }
        },
        {
            path: "/register",
            name: "Регистрация",
            component: Registration,
            meta: {
                requiresAuth: false
            }
        },
        {
            path: "/wait_page",
            name: "Ожидайте!",
            component: WaitPage,
            meta: {
                requiresAuth: false
            }
        },
        {
            path: "/admin/load_model",
            name: "Загрузка модели",
            component: LoadModel,
            meta: {
                requiresAuth: false
            }
        },
        {
            path: "/admin/constructor_settings",
            name: "Настройки конструктора",
            component: ConstructorSettings,
            meta: {
                requiresAuth: false
            }
        },
        {
            path: "/admin/models/:id",
            name: "Редактирование модели",
            component: ModelEditor,
            meta: {
                requiresAuth: false
            }
        },
        {
            path: '/admin/new_applications',
            name: "Заявки",
            component: NewApplication,
            meta: {
                requiresAuth: false
            }
        },
        {
            path: "/admin/create_manager",
            name: "Добавление менеджера",
            component: CreateManager,
            meta: {
                requiresAuth: false
            }
        },
        {
            path: '/admin/models',
            component: ModelList,
            name: "Список моделей",
            meta: {
                requiresAuth: false
            }
        },
        {
            path: '/admin/customers',
            component: Customers,
            name: "Список заказчиков",
            meta: {
                requiresAuth: false
            }
        },
        {
            path: "/admin/customers/:id",
            name: "Сведения о заказчике",
            component: CustomerEditor,
            meta: {
                requiresAuth: false
            }
        },
        {
            path: '/admin/companies',
            component: Companies,
            name: "Список производителей",
            meta: {
                requiresAuth: false
            }
        },
        {
            path: "/admin/companies/:id",
            name: "Сведения о производителе",
            component: CompanyEditor,
            meta: {
                requiresAuth: false
            }
        },
    ],
    history: createWebHistory()
})

router.beforeEach((to, from, next) => {
    document.title = to.name;
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
