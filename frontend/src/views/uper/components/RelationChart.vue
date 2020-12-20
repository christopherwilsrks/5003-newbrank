<template>
  <el-card :body-style="{ padding: '20px' }" class="relation-chart-container" shadow="hover" :style="`width: ${chartWidth}px;height: ${docHeight - 150}px;`">
    <div id="map" class="map" ref="map" :style="`width: ${chartWidth - 40}px;height: ${docHeight - 190}px;`">
    </div>
  </el-card>
</template>

<script>
import RelationChart from 'relation-chart'
import data from '@/statics/data'
import {mapGetters} from "vuex";

export default {
  name: "RelationChart",
  computed: {
    ...mapGetters(['device', 'docWidth', 'docHeight']),
    chartWidth() {
      let width = 0;
      if (this.device === 'desktop') {
        width = this.docWidth * .58
      } else {
        width = this.docWidth - 30
      }
      return width;
    }
  },
  data() {
    return {}
  },
  mounted() {
    new RelationChart(this.$refs.map, data.健身)
  },
}
</script>

<style lang="scss">
.relation-chart-container {
  .el-card__body {
    width: 100%;
    height: 100%;
  }
}
</style>