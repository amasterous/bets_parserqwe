<template>
    <div class="container">
      <h3>{{ title }}</h3>
      <button v-on:click="reloadPage">refresh</button>
      <div>
        <a href="#" @click="getPostsType('posts')">posts</a>
        <a class="ml-1" href="#" @click="getPostsType('bets')">bets</a>
        <a class="ml-1" href="#" @click="getPostsType('trash')">ALL POSTs</a>
      </div>
      <hr />
      <div v-if="title == 'bets'">
        <a href="#" @click="getPostsType('csgo', false)">csgo</a>
        <a class="ml-1" href="#" @click="getPostsType('dota', false)">dota 2</a>
      </div>

      <PostsList
      v-bind:posts="posts"
      v-bind:title="title"
      v-bind:getPostsType="getPostsType"
      v-bind:game_type="game_type"
      />
    </div>
</template>

<script>
import axios from 'axios';
import PostsList from '@/components/posts/PostsList'
export default {
  data() {
    return {
      posts: [],
      title: '',
      game_type: '',
    }
  },
  components: {
    PostsList,
  },
  methods:{
    getPostsType(type, changetype = true) {
      const path = `http://127.0.0.1:5000/${type}`;
      axios
        .get(path)
        .then(res => {
          if (changetype == true) {
            this.title = type;
          }
          if (type == "dota" || type == "csgo") {
            this.game_type = type;
            this.title = 'bets'
          }
          else {
            this.game_type = '';
          }
          this.posts = res.data.posts;
          console.log(path);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    reloadPage() {
      this.getPostsType(this.title)
    },
  },
  created() {
    this.getPostsType("trash");
  },
}
</script>