<template>
  <el-row id="uper-index-container" align="center" justify="space-around" :type="device === 'desktop' ? 'flex' : ''">

    <el-col :span="6" :xs="24">
      <keep-alive>
        <UpInfo :id="id" :uperInfo="uperInfo" />
      </keep-alive>
    </el-col>

    <el-col :span="15" :xs="24">
      <el-row justify="center" type="flex">
        <el-col class="selector" :span="24" :xs="24">
          <el-tabs v-model="analyzer" @tab-click="handleClick">
            <el-tab-pane :label="$t('upinfo.trend_analyze')" name="trend"/>
            <el-tab-pane :label="$t('upinfo.work_analyze')" name="work"/>
            <el-tab-pane :label="$t('upinfo.fan_analyze')" name="fan"/>
            <el-tab-pane :label="$t('upinfo.word_analyze')" name="word"/>
          </el-tabs>
        </el-col>

      </el-row>

      <keep-alive>
        <router-view :uperInfo="uperInfo" :key="key"></router-view>
      </keep-alive>


    </el-col>
  </el-row>
</template>

<script>
import {UpInfo} from "./components";
import {mapGetters} from 'vuex'
import {getUpByUid} from "@/api/up";

export default {

  name: "Uper",
  components: {
    UpInfo
  },
  computed: {
    ...mapGetters(['device']),
    key() {
      return this.$route.name
    },
    id() {
      return this.$route.params.id
    },
    analyzer: {
      set(val) {
        return val;
      },
      get() {
        let routes = this.$route.path.split('/')
        return routes[routes.length - 1]
      }
    },
  },
  data() {
    return {
      uperInfo: {
        channel: 'animation'
      }
    }
  },
  watch: {
    id() {
      this.getUpByUid()
    }
  },
  created() {
    console.log('uper created')
    this.getUpByUid()
  },
  methods: {
    getUpByUid() {
      const loading = this.$loading({
        lock: true,
        text: 'Loading',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      });
      getUpByUid(this.id).then(res => {
        this.uperInfo = res
      }).finally(() => {
        loading.close()
      })
    },
    handleClick(tab, event) {
      if (this.analyzer !== tab.name)
        this.$router.push({path: tab.name})
    }
  }
}
</script>

<style lang="scss" scoped>
.selector {
  background: #ffffff;
  margin-bottom: 20px;
}

</style>
<style lang="scss">
#uper-index-container {
  .selector {
    display: flex;
    justify-content: center;

    .el-tabs__content {
      display: none;
    }

    .is-active {
      font-weight: 700;
      color: #3e4040;
    }

    .el-tabs__header {
      margin: 0;
    }

    //.el-tabs__nav-scroll {
    //  display: flex;
    //  justify-content: center;
    //}
    //.el-tabs__nav {
    //  width: 85%;
    //  display: flex;
    //  justify-content: space-around;
    //}
  }
}
</style>