<template>
  <el-row type="flex" justify="center">
    <el-col :span="18">
      <el-card class="header-container" :body-style="{ padding: '20px' }" shadow="hover">
        <el-row :gutter="3">
          <el-col :span="4">{{ $t('channel') }}:</el-col>
          <el-col :span="18">
            <router-link v-for="channel in channels" :key="channel.name"
                         :class="{tag_selected: channel.name === tag, tag: true, tag_en: language === 'en'}"
                         :to="'/relation/' + channel.name">
              {{ $t('channels.' + channel.name) }}
            </router-link>
          </el-col>
        </el-row>
      </el-card>

      <el-card :body-style="{ padding: '20px' }" class="relation-chart-container" shadow="hover"
               :style="`width: 100%;height: ${docHeight - 200}px;margin-top: 20px;`">
        <div id="map" class="map" ref="map" :style="`width: ${chartWidth - 40}px;height: ${docHeight - 200}px;`">
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
import RelationChart from 'relation-chart'
import data from '@/statics/data'
import {mapGetters} from "vuex";

export default {
  name: "RelationChart",
  computed: {
    ...mapGetters(['device', 'language', 'docWidth', 'docHeight', 'channels']),
    chartWidth() {
      let width = 0;
      if (this.device === 'desktop') {
        width = this.docWidth * .75
      } else {
        width = this.docWidth * .75
      }
      return width;
    },
    tag() {
      return this.$route.params.tag
    },
  },
  data() {
    return {
      relation_data: data,
    }
  },
  watch: {
    tag() {
      this.$refs.map.firstChild.remove()
      new RelationChart(this.$refs.map, data[this.tag])
    }
  },
  mounted() {
    new RelationChart(this.$refs.map, data[this.tag])
  },
  created() {
  }
}
</script>

<style lang="scss" scoped>
.header-container {
  color: #949999;

  .tag {
    cursor: pointer;
    color: #636666;
    font-size: 14px;
    text-decoration: none;

    margin: 0 8px 22px 0;
    line-height: 20px;
    padding: 0 7px;

    &:hover {
      color: #00a0d8;
    }
  }

  .tag_en {
    text-justify: distribute-all-lines !important;
    //word-break: break-all;
  }

  .tag_selected {
    background-color: #00a0d8;
    color: #fff !important;
    border: 1px solid #e1e1e6;
    border-radius: 4px;
  }
}
</style>
<style lang="scss">
.relation-chart-container {
  .el-card__body {
    width: 100%;
    height: 100%;
  }
}
</style>