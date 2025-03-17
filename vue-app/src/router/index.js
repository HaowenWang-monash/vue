import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/home.vue';
import SearchUV from '../components/SearchUV.vue';
import GeneralInfo from '../components/GeneraLinfo.vue'; // ✅ UV Information 页面
import SunSafetyPlanner from '../components/SunSafetyPlanner.vue'; // ✅ Sun Safety Planner 页面
import Shop from '../components/Shop.vue'; // ✅ Shop 页面

const routes = [
  { path: '/', component: Home },
  { path: '/check-uv', component: SearchUV },
  { path: '/info', component: GeneralInfo }, // ✅ UV Information
  { path: '/planner', component: SunSafetyPlanner }, // ✅ Sun Safety Planner
  { path: '/shop', component: Shop } // ✅ Shop
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
