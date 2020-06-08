<template>
    <div>
      <button @click="checkSortBet('bet')">sort bet</button>
      <button @click="checkSortBet('coef')">sort coef</button>
      <table class="table">
        <thead>
          <tr>
            <th style="min-width:250px;" scope="col">author</th>
            <th scope="col">content</th>
            <th style="min-width:100px;" scope="col">time</th>
            <th scope="col">other</th>
          </tr>
        </thead>
        <tbody>
            <PostItem 
            v-for="post in sortedPosts"
            v-bind:post="post"
            v-bind:title="title"
            v-bind:getPostsType="getPostsType"
            v-bind:game_type="game_type"


            v-bind:key="post.time"
            />
        </tbody>
      </table>
    </div>
</template>

<script>
import PostItem from '@/components/posts/PostItem'
export default {
  props: ['posts', 'title', 'game_type', 'getPostsType', 'game_type'],
  components: {
    PostItem
  },
  data () {
    return {
      sortParam: '',
    }
  },
  methods: {
    // TODO: сделано очень плохо) надо посмотреть потом как это можно сделать лучше.
    checkSortBet: function (casee) {
      console.log(this.sortParam)
      if (casee == 'bet'){
        if (this.sortParam != ''){
          if (this.sortParam == 'bet1') {
            this.sortParam = 'bet2'
          }
          else if (this.sortParam == 'bet2') {
            this.sortParam = 'bet1'
          }
          else {
            this.sortParam = 'bet1'
          }
        }
        else {
          this.sortParam = 'bet1'
        }
      }
      else if (casee == 'coef') {
        if (this.sortParam != ''){
          if (this.sortParam == 'coef1') {
            this.sortParam = 'coef2'
          }
          else if (this.sortParam == 'coef2') {
            this.sortParam = 'coef1'
          }
          else {
            this.sortParam = 'coef1'
          }
        }
        else {
          this.sortParam = 'coef1'
        }
      }
    }
  },
  computed: {
    // TODO: сделано очень плохо) надо посмотреть потом как это можно сделать лучше.
    sortedPosts () {
      switch(this.sortParam) {
        case 'bet1': return this.posts.sort(sortByBet1);
        case 'bet2': return this.posts.sort(sortByBet2);

        case 'coef1': return this.posts.sort(sortByCoef1);
        case 'coef2': return this.posts.sort(sortByCoef2);
        default: return this.posts;
      }
    }
  }
}
// TODO: сделано очень плохо) надо посмотреть потом как это можно сделать лучше.
var sortByBet1 = function (d1, d2) { return (Number.parseFloat(d1.bet) < Number.parseFloat(d2.bet)) ? 1 : -1; };
var sortByBet2 = function (d1, d2) { return (Number.parseFloat(d1.bet) > Number.parseFloat(d2.bet)) ? 1 : -1; };
var sortByCoef1 = function (d1, d2) { return (Number.parseFloat(d1.coef) < Number.parseFloat(d2.coef)) ? 1 : -1; };
var sortByCoef2 = function (d1, d2) { return (Number.parseFloat(d1.coef) > Number.parseFloat(d2.coef)) ? 1 : -1; };
</script>