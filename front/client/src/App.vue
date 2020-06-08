<template>
  <div id="app">
      <h1><center>Bets Parser</center></h1>
      <div class="container">
        <h3>
          <a href="/stats">stats</a>
          <a href="/posts" class="ml-1">bets</a>
        </h3>
      </div>
      <hr>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  margin-top: 60px;
}
</style>
