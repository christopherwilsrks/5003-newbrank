<template>
  <el-card :body-style="{ padding: '20px' }" class="container" shadow="hover">
<!--    <el-row justify="center">-->
<!--      <el-col :span="24" :xs="24">-->

    <div class="header">{{ $t('upinfo.trend_title') }}</div>
    <div style="width: 100%; display: flex; justify-content: center;">

        <div class="chart-wrapper" :style="'width:' + chartWidth + 'px;'">
          <div id="trend-chart" style="height: 100%; width: 100%;" />
        </div>
        </div>
<!--        <v-chart :options="trendData"></v-chart>-->
<!--      </el-col>-->
<!--    </el-row>-->
  </el-card>
</template>

<script>
import mock from './mock'
import echarts from 'echarts'
import 'echarts/lib/chart/line'
import {mapGetters} from "vuex";

export default {
  name: "TrendAnalyze",
  data() {
    return {
      chart: null,
      trendData: {

      }
    }
  },
  computed: {
    ...mapGetters(['device', 'docWidth']),
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
  watch: {
    chartWidth(val) {
      this.chart.resize(val, 400)
    },
  },
  mounted() {
    if (this.$route.path.endsWith('trend'))
      this.initChart();
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  created() {
    console.log('trend created')
  },
  methods: {
    initChart() {
      this.chart = echarts.init(document.getElementById('trend-chart'));

      let xy = [['time', 'follower increment']]
      mock.data.forEach(item => {
        xy.push([item['gmtModify'], item['followerAdd']])
      })
      this.chart.setOption({
        xAxis: {
          type: 'time',
          axisLine: {
            show: false
          },
          splitLine: {
            show: false
          }
        },
        yAxis: {
          axisLine: {
            show: false
          }
        },
        tooltip: {
          backgroundColor: 'hsla(0,0%,100%,.9)',
          alwaysShowContent: true,
          // enterable: true,
          textStyle: {
            color: '#575757',
            fontFamily: "DINPro Medium,-apple-system,BlinkMacSystemFont,Segoe UI,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Helvetica Neue,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol",

          }
        },
        dataset: {
          source: xy
        },
        series: {
          type: 'line',
          showSymbol: true,
          lineStyle: {color: 'rgba(250, 111, 151)'},
          areaStyle: {
            normal: {
              color: 'rgba(250, 111, 151, 0.3)'
              // color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
              //   offset: 0,
              //   color: 'rgba(250, 111, 151, 0.7)'
              // }, {
              //   offset: 0.8,
              //   color: 'rgba(250, 111, 151, 0)'
              // }], false),
              // shadowColor: 'rgba(0, 0, 0, 0.1)',
              // shadowBlur: 10
            }
          },
        }
      });
    }
  }
}
</script>

<style lang="scss" scoped>
.header {
  margin-bottom: 24px;
  font-size: 16px;
  color: #3e4040;
  margin-left: 4px;
}
.chart-wrapper {
  min-height: 400px;
  height: 400px;
}
</style>