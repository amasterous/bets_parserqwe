<template>
  <div class="container">
      <!-- <h2>This page: {{ data.page }}</h2>
      <h2 v-if="data.next_page != 0">Next page {{ data.next_page }}</h2>
      <h2 v-if="data.prev_page != 0">Prev page {{ data.prev_page }}</h2>
      <h2>Last page: {{ data.total_pages }}</h2> -->

      <!-- <a :href="'?page=' + (Number(page)+1)" v-if="data.next_page !=0">next page</a><br>
      <a :href="'?page=' + (Number(page)-1)" v-if="data.prev_page !=0">prev page</a><br> -->

      <!-- <a href="#" @click="changePage(page+1)" v-if="data.next_page !=0">next page</a><br>
      <a href="#" @click="changePage(page-1)" v-if="data.prev_page !=0">prev page</a> -->

      <hr>

      <div>
        <!-- <div v-for="post in data.posts" :key="post.id">
          <p>{{ post.id }}</p>
          <p>{{ post.author }}</p>
          <p>{{ post.time }}</p>
        </div> -->
        <div v-infinite-scroll="this.loadMore" infinite-scroll-disabled="busy" infinite-scroll-distance="10">
          <div v-for="post in this.posts" :key="post.id">
            <p>{{ post.id }}</p>
            <p>{{ post.author }}</p>
            <p>{{ post.time }}</p>
          </div>
        </div>
      </div>

  </div>

</template>

<script>

import axios from 'axios';
export default {
  data() {
    return {
      data: [],
      posts: [],
      page: 1,
      busy: false,
      error: '',
    }
  },
  methods: {
    loadMore: function() {
      this.busy = true;
      this.page++
      this.getStats()
      this.busy = false
    },
    getStats() {
      // if (Number.isSafeInteger(parseInt(this.$route.query.page))){
      //   this.page = this.$route.query.page
      // }
      const path = `http://127.0.0.1:5000/supertest?page=${this.page}`;
      axios
        .get(path)
        .then(res => {
          this.data = res.data;
          this.posts.push(...res.data.posts);
          if(this.data.status == 'failure'){
            console.log('failure')
          }
          console.log(this.path)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    changePage(page) {
      this.page = page;
      this.getStats()
    }
    
  },
  created() {
    this.getStats();
  },

}

</script>