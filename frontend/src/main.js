import './assets/css/index.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

axios.defaults.baseURL = 'http://139.59.155.240'

const app = createApp(App)

app.use(createPinia())
app.use(router, axios)

app.mount('#app')