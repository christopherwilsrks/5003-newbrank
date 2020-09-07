<template>
  <div>
    <keep-alive :exclude="[]">
      <router-view :key="key"></router-view>
    </keep-alive>
  </div>
</template>
<script>
export default {
  name: 'Layout',
  computed: {
    key() {
      return this.$route.path
    }
  }
}
</script>