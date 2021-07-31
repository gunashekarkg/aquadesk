import Vue from 'vue'
import Router from 'vue-router'
import Datavisualisation from '../views/Datavisualisation.vue'
import DatabaseTable from '../views/DatabaseTable.vue'
import DataVisualisation1 from '../views/DataVisualisation1'

Vue.use(Router)

export default new Router({
  mode:'history',
  base:process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Datavisualisation',
      component: Datavisualisation
    },
    {
      path: '/',
      name: 'DatabaseTable',
      component: DatabaseTable
    },
    {
      path: '/',
      name: 'DataVisualisation1',
      component: DataVisualisation1
    },
  ]
  })