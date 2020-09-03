<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
<style>
html,
body,
#app {
  font-family: sans-serif, Helvetica, Arial;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  line-height: 1.5;
  font-size: 15px;
  height: 100%;
  width: 100%;
  margin: 0;
  /* margin-top: 60px; */
}
</style>
