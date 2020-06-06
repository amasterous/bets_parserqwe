<template>
    <div>
      <table class="table">
        <thead>
          <tr>
            <th scope="col">author</th>
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
            />
        </tbody>
      </table>
    </div>
</template>

<script>
import PostItem from '@/components/posts/PostItem'
export default {
  props: ['posts', 'title', 'game_type'],
  components: {
    PostItem
  }
}
</script>