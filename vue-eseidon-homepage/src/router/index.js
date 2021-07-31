import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import { authGuard } from "../auth/authGuard";

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/About.vue')
    },
    {
      path: '/technology',
      name: 'technology',
      component: () => import('../views/Technology.vue')
    },
    {
      path: '/sustainability',
      name: 'sustainability',
      component: () => import('../views/Sustainability.vue')
    },
    {
      path: '/aquadesk',
      name: 'aquadesk',
      component: () => import('../views/AquaDesk.vue'),
      beforeEnter: authGuard
    }
  ]
})