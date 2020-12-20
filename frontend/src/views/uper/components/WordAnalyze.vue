<template>
  <el-card :body-style="{ padding: '20px' }" class="container" shadow="hover">
    <img style="width: 100%;" :src="`https://rks.cool/img-newbrank/${uperInfo.channel}/${uperInfo.name}.png`" alt="word cloud">
  </el-card>
</template>

<script>
export default {
  name: "WordAnalyze",
  props: ["uperInfo"]
}
</script>

<style scoped>

</style>