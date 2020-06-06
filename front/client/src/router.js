import Vue from 'vue';
import Router from 'vue-router';
// import Ping from './components/Ping.vue';
import Posts from './components/Posts.vue';
// import HelloWorld from './components/HelloWorld.vue';
import Test from './components/posts/Test.vue';
import Pists from './components/Pists.vue';

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
      name: 'Pists',
      component: Pists,
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
