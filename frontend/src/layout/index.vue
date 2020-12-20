<template>
  <div>
    <Navbar/>
    <keep-alive>
      <router-view :key="key"></router-view>
    </keep-alive>
  </div>
</template>
<script>
import {Navbar} from './components'
import ResizeMixin from './mixin/ResizeHandler'
export default {
  name: 'Layout',
  components: {
    Navbar
  },
  mixins: [ResizeMixin],
  computed: {
    key() {
      return this.$route.name
    }
  },
  created() {
    this.$store.dispatch('app/getChannels');
  }
}
</script>