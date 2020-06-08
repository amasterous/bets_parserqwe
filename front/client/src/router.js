import Vue from 'vue';
import Router from 'vue-router';

import Posts from './components/Posts.vue';
import Pists from './components/Pists.vue';
import Stats from './components/Stats.vue';

Vue.use(Router);

export default new Router({
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Pists',
      component: Pists,
    },
    {
      path: '/posts',
      name: 'Pists',
      component: Pists,
    },
    {
      path: '/stats',
      name: 'Stats',
      component: Stats,
    },
  
    // {
    //   path: '/ping',
    //   name: 'Ping',
    //   component: Ping,
    // },
    // {
    //   path: '/hello',
    //   name: 'Hello',
    //   component: HelloWorld,
    // },
  ],
  mode: 'history',
});
