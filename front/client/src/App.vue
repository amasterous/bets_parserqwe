<template>
  <div id="app">
      <h1><center>Bets Parser</center></h1>
      <div class="container">
        <h3>
          <a href="#" v-on:click="changePageType(1)">stats</a>
          <a href="#" v-on:click="changePageType(0)" class="ml-1">bets</a>
        </h3>
      </div>
      <hr>
      <Posts v-if="this.pageType==0" />
      <StatsMain v-if="this.pageType==1" />
  </div>
</template>

<script>
import Posts from './components/posts/Posts'
import StatsMain from './components/stats/StatsMain'
export default {

  name: 'App',
  data() {
    return {
      pageType: 0,
    }
  },
  components: {
    Posts, StatsMain,
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
