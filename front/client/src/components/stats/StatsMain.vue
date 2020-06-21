<template>
  <div class="container">
    <h1>Hello it is statistic section</h1>
    <a href="#">malish</a>
    <a href="#" class="ml-2">norch</a>
    <a href="#" class="ml-2">gagarin</a>
    <ul>
      <li>posts count: {{this.stats.posts_count}}</li>
      <li>bets count: {{this.stats.bets_count}}</li>
      <li>winrate: {{this.stats.winrate}}</li>
      <li>avg coef: {{this.stats.avgcoef}}</li>
      <li>avg bet: {{this.stats.avgbetamount}}</li>
    </ul>
  </div>

</template>

<script>

import axios from 'axios';
export default {
  data() {
    return {
      stats: []
    }
  },
  methods: {
    getStats() {
      const path = 'http://127.0.0.1:5000/stats/main';
      axios
        .get(path)
        .then(res => {
          this.stats = res.data;
          console.log(this.path)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created() {
    this.getStats();
  },

}

</script>