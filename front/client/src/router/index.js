import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping'
import Posts from '@/components/Posts'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Posts',
      component: Posts,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
  mode: 'hash',
});
