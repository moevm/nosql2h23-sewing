import { createApp } from 'vue'
import vue3dLoader from "vue-3d-loader";
import App from './App.vue'
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css";
import 'bootstrap/dist/css/bootstrap.css'

createApp(App).use(vue3dLoader).mount("#app");
