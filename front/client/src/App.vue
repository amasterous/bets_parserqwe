<template>
  <div id="app">
      <h1><center>Bets Parser</center></h1>
      <div class="container">
        <h3>
          <a href="#" v-on:click="changePageType(1)">stats</a>
          <a href="#" v-on:click="changePageType(0)" class="ml-1">bets</a>
          <a href="#" v-on:click="changePageType(2)" class="ml-1">test</a>
        </h3>
      </div>
      <hr>
      <Posts v-if="this.pageType==0" />
      <Test v-if="this.pageType==2" />
      <StatsMain v-if="this.pageType==1" />
  </div>
</template>

<script>
import Posts from './components/posts/Posts'
import StatsMain from './components/stats/StatsMain'
import Test from './components/test/Test'

export default {
  name: 'App',
  data() {
    return {
      pageType: 2,
    }
  },
  components: {
    Posts, StatsMain, Test
  },
  methods: {
    changePageType (type) {
      this.pageType = type
    }
  },
};
</script>

<style>
#app {
  margin-top: 60px;
}
</style>
