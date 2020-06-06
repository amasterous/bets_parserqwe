<template>
    <div>
      <table class="table">
        <thead>
          <tr>
            <th style="min-width:250px;" scope="col">author</th>
            <th scope="col">content</th>
            <th scope="col">time</th>
            <th scope="col">other</th>
          </tr>
        </thead>
        <tbody>
            <PostItem 
            v-for="post in posts"
            v-bind:post="post"
            v-bind:title="title"
            v-bind:key="post.time"
            v-bind:getPostsType="getPostsType"
            v-bind:game_type="game_type"
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
  }
}
</script>