<template>
    <div class="container">
      <div class="row">
        <div class="col-sm-1">
          <h3>{{ title }}</h3>
        </div>
        <div class="col ml-2">
          <button class="btn btn-info ml-3" v-on:click="reloadPage">refresh</button>
        </div>
      </div>
      <div>
        <a href="#" @click="getPostsType('posts')">posts</a>
        <a class="ml-1" href="#" @click="getPostsType('bets')">bets</a>
        <a class="ml-1" href="#" @click="getPostsType('trash')">ALL POSTs</a>
      </div>
      <hr />
      <div v-if="title == 'bets'">
        <a href="#" @click="getPostsType('bets', 'csgo')">csgo</a>
        <a class="ml-1" href="#" @click="getPostsType('bets', 'dota')">dota 2</a>
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
      path: '',
    }
  },
  components: {
    PostsList,
  },
  methods:{
    getPostsType(type, game='') {
      this.path = `http://127.0.0.1:5000/${type}`;
      if (type == "bets"){
        if (this.game_type != '') {
          this.title = 'bets';
          this.path = `http://127.0.0.1:5000/${this.game_type}`;
        }
        else {
          this.title = 'bets';
          this.path = `http://127.0.0.1:5000/${type}`;
        }
      }
      else {
        this.title = type
        this.path = `http://127.0.0.1:5000/${type}`;
      }
      if (type == "bets" && game != ''){
          this.title = 'bets';
          this.game_type = game
          this.path = `http://127.0.0.1:5000/${this.game_type}`;
      }
      axios
        .get(this.path)
        .then(res => {
          this.posts = res.data.posts;
          console.log(this.path);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    reloadPage() {
      this.getPostsType(this.title)
    },
  },
  created() {
    this.getPostsType("posts");
  },
}
</script>