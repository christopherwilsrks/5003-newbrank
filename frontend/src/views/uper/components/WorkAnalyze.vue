<template>
  <el-card :body-style="{ padding: '20px' }" class="container" shadow="hover">
    <el-table
        :data="video_list"
        highlight-current-row
        ref="multipleTable"
        style="width: 100%; margin-top: 20px;"
        v-loading.body="listLoading"
    >
      <!-- 视频信息 -->
      <el-table-column :label="$t('workinfo.video_info')" min-width="150px">
        <template slot-scope="scope">
          <a class="video-link scope-ellipsis" :href="`https://www.bilibili.com/video/${scope.row.bvid}`" target="_blank">
            <div class="video-info-container">
              <div class="div-cover" v-show="device === 'desktop'">
                <img class="cover-img" :src="scope.row.pic" alt="cover">
              </div>
              <div class="video-info-container2">
                <span class="video-info-title">{{ scope.row.title }}</span>
                <div style="font-size: 12px;">
                  <span style="margin-right: 8px;">{{ $t('workinfo.created') }}</span>
                  <span>{{ scope.row.created | toDate(language) }}</span>
                </div>
              </div>
            </div>
          </a>
        </template>
      </el-table-column>
      <!-- 播放数 -->
      <el-table-column align="center" :label="$t('workinfo.views')">
        <template slot-scope="scope">
          <span class="video-figure">{{ scope.row.play }}</span>
        </template>
      </el-table-column>
      <!-- 评论数 -->
      <el-table-column align="center" :label="$t('workinfo.comments')" v-if="device === 'desktop'">
        <template slot-scope="scope">
          <span class="video-figure">{{ scope.row.comment }}</span>
        </template>
      </el-table-column>
    </el-table>


    <!-- 分页器 -->
    <div class="pagination-container">
<!--      <el-row justify="center" type="flex">-->
<!--        <el-col :span="18">-->
          <el-pagination
              :current-page.sync="listQuery.page"
              :page-size="listQuery.size"
              :page-sizes="[10, 20, 30]"
              :total="total"
              @current-change="handleCurrentChange"
              @size-change="handleSizeChange"
              align="center"
              :layout="device === 'desktop' ? 'total, sizes, prev, pager, next, jumper' : 'pager, total'"
          ></el-pagination>
<!--        </el-col>-->
<!--      </el-row>-->
    </div>
  </el-card>
</template>

<script>
import {mapGetters} from "vuex";
import {getVideosByUid} from "@/api/video";

export default {
  name: "WorkAnalyze",
  data() {
    return {
      listLoading: false,
      video_list: [
        {
          "id": 1,
          "uid": 328245631,
          "title": "音乐欢快，动作简单，这样的尊巴初学者也能轻松上手！",
          "subtitle": "",
          "description": "https://mparticle.uc.cn/video.html?uc_param_str=frdnsnpfvecpntnwprdssskt&wm_aid=1040fd46f922473ab62968f612fac4a4",
          "pic": "https://rks.cool/newbrank-img/i1.hdslb.com/bfs/archive/bd8c8e71ef137eeff1e6460fb2431a1776d29e5e.jpg",
          "author": "BBT健身尊巴舞Zumba",
          "mid": 328245631,
          "created": 1605491606,
          "length": "04:10",
          "aid": "670344300",
          "bvid": "BV1Da4y1p7fk",
          "play": 498,
          "comment": 0,
          "videoReview": 0,
          "typeid": 164,
          "review": 0
        },
        {
          "id": 2,
          "uid": 328245631,
          "title": "太燃了，劲爆DJ舞曲配尊巴Zumba，比跳广场舞还要嗨！",
          "subtitle": "",
          "description": "https://mparticle.uc.cn/video.html?uc_param_str=frdnsnpfvecpntnwprdssskt&wm_aid=df0b8d266f6444eb9b5f60138a8b3833",
          "pic": "https://rks.cool/newbrank-img/i2.hdslb.com/bfs/archive/de92b4b9e39cb9d4ce7d215dbafc0119d0acde1a.jpg",
          "author": "BBT健身尊巴舞Zumba",
          "mid": 328245631,
          "created": 1605491335,
          "length": "04:10",
          "aid": "970353123",
          "bvid": "BV1Np4y1r7ms",
          "play": 198,
          "comment": 0,
          "videoReview": 0,
          "typeid": 164,
          "review": 0
        }],
      total: 0,
      listQuery: {
        page: 1,
        size: 10,
        uid: 0
      }
    }
  },
  filters: {
    toDate(value, language) {
      let unixTimestamp = new Date(value * 1000);
      return unixTimestamp.toLocaleString(language)
    }
  },
  computed: {
    ...mapGetters(['device', 'docWidth', 'language']),
    id() {
      this.listQuery.uid = this.$route.params.id
      return this.$route.params.id
    }
  },
  watch: {
    id(val) {
      this.listQuery.uid = val
      this.listQuery.page = 1
      this.listQuery.size = 10
      this.getVideosByUid()
    }
  },
  created() {
    this.getVideosByUid()
  },
  methods: {
    getVideosByUid() {
      this.listLoading = true
      getVideosByUid(this.listQuery).then(res => {
        this.total = res.total
        this.video_list = res.records
      }).finally(() => {
        this.listLoading = false
      })
    },
    handleSizeChange(val) {
      this.listQuery.size = val
      this.getVideosByUid()
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.getVideosByUid()
    },
  }
}
</script>

<style lang="scss" scoped>
.video-link {
  text-decoration: none;
}

.video-info-container {

  display: flex;
  align-items: center;

  .div-cover {
    height: 75px;
    width: auto;
    margin-right: 16px;

    .cover-img {
      height: 100%;
      border-radius: 4px;
    }
  }
}

.video-info-container2 {
  font-size: 14px;
  flex: 1 1;
  flex-direction: column;
  justify-content: space-between;
  overflow: hidden;
  flex-basis: 0;
  min-height: 75px;
  color: #949999;

  .video-info-title {
    font-weight: 400;
    font-size: 16px;
    line-height: 22px;
    color: #3e4040;
    overflow: hidden;
    text-overflow: ellipsis;
    position: relative;

    &:hover {
      color: #00a0d8;
    }
  }
}

.video-figure {
  font-weight: 500;
  color: #3e4040;
  font-size: 16px;
}

.pagination-container {
  margin-top: 20px;
}
</style>