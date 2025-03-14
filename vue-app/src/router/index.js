import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/home.vue';
import SearchUV from '../components/SearchUV.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/check-uv', component: SearchUV }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
