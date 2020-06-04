import Vue from 'vue';
import Router from 'vue-router';
// import Ping from './components/Ping.vue';
import Posts from './components/Posts.vue';
import HelloWorld from './components/HelloWorld.vue';
import Test from './components/Test.vue';

Vue.use(Router);

export default new Router({
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Posts',
      component: Posts,
    },
    {
      path: '/test',
      name: 'Test',
      component: Test,
    },
    // {
    //   path: '/ping',
    //   name: 'Ping',
    //   component: Ping,
    // },
    {
      path: '/hello',
      name: 'Hello',
      component: HelloWorld,
    },
  ],
  mode: 'history',
});
