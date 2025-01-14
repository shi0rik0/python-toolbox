import './index.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createRouter, createMemoryHistory } from 'vue-router'
import App from './App.vue'

const app = createApp(App)
const pinia = createPinia()
const router = createRouter({
  history: createMemoryHistory(),
  routes: [],
})

app.use(pinia).use(router).mount('#app')
