<template>
  <el-row class="up-list-container" type="flex" justify="center">
    <el-col :span="20">

      <el-card class="header-container" :body-style="{ padding: '20px' }" shadow="hover">
        <el-row :gutter="3">
          <el-col :span="4">{{ $t('channel') }}:</el-col>
          <el-col :span="18">
            <a v-for="channel in channels" :key="channel.name"
                         :class="{tag_selected: channel.name === tag, tag: true, tag_en: language === 'en'}"
                         @click="() => {tag = channel.name;getUpListByChannel()}"
            >
              {{ $t('channels.' + channel.name) }}
            </a>
          </el-col>
        </el-row>
      </el-card>

      <el-table
          :data="up_list"
          highlight-current-row
          ref="multipleTable"
          style="width: 100%; margin-top: 20px;"
          v-loading.body="listLoading"
      >
        <!-- up主号 -->
        <el-table-column :label="$t('uplist.upid')" min-width="150px">
          <template slot-scope="scope">
            <div class="up-id-container">
              <div class="div-avatar" v-show="device === 'desktop'">
                <img class="avatar" :src="scope.row.face" alt="avatar">
              </div>
              <router-link class="up-id-scope scope-ellipsis" :to="`/uper/${scope.row.uid}`">
                <div class="up-id-scope-title">
                  <span class="up-id-scope-name">{{ scope.row.name }}</span>
                  <span class="up-id-scope-level">lv{{ scope.row.level }}</span>
                  <span class="up-id-scope-category"
                        v-show="device === 'desktop'">{{ $t('channels.' + scope.row.channel) }}</span>
                </div>
                <span class="up-id-scope-uid">Uid: {{ scope.row.uid }}</span>
                <span class="up-id-scope-sign scope-ellipsis"
                      v-show="device === 'desktop'">个性签名：{{ scope.row.sign }}</span>
              </router-link>
            </div>
          </template>
        </el-table-column>
        <!-- 作品数 -->
        <el-table-column align="left" :label="$t('uplist.works')">
          <template slot-scope="scope">
            <span class="up-id-figures">{{ scope.row.video }}</span>
          </template>
        </el-table-column>
        <!-- 获赞数 -->
        <el-table-column align="center" :label="$t('uplist.sex')" v-if="device === 'desktop'">
          <template slot-scope="scope">
            <span class="up-id-figures">{{ scope.row.sex }}</span>
          </template>
        </el-table-column>
        <!-- 充电人数 -->
        <el-table-column align="center" :label="$t('uplist.following')" v-if="device === 'desktop'">
          <template slot-scope="scope">
            <span class="up-id-figures">{{ scope.row.following }}</span>
          </template>
        </el-table-column>
        <!-- 粉丝数 -->
        <el-table-column align="center" :label="$t('uplist.fans')">
          <template slot-scope="scope">
            <span class="up-id-figures">{{ scope.row.follower }}</span>
          </template>
        </el-table-column>
      </el-table>
    </el-col>
  </el-row>
</template>

<script>
import {mapGetters} from 'vuex'
import {getUpListByChannel} from "@/api/up";

export default {
  name: "UpList",
  computed: {
    ...mapGetters(['device', 'language', 'docWidth', 'docHeight', 'channels']),
    // tag() {
    //   return this.$route.params.tag ? this.$route.params.tag : 'animation'
    // },
  },
  data() {
    return {
      up_list: [
        {
          "id": 1,
          "uid": 328245631,
          "name": "BBT健身尊巴舞Zumba",
          channel: "aerobics",
          "sex": "保密",
          "face": "https://rks.cool/newbrank-img/i0.hdslb.com/bfs/face/a40c3f0de87c2d0893d3cfb48fe40e07cfef4744.jpg",
          "sign": "",
          "level": 5,
          "birthday": "",
          "fansBadge": "0",
          "official": "{'role': 0, 'title': '', 'desc': '', 'type': -1}",
          "vip": "{'type': 0, 'status': 0, 'theme_type': 0, 'label': {'path': '', 'text': '', 'label_theme': ''}, 'avatar_subscript': 0, 'nickname_color': ''}",
          "nameplate": "{'nid': 0, 'name': '', 'image': '', 'image_small': '', 'level': '', 'condition': ''}",
          "topPhoto": "https://rks.cool/newbrank-img/i2.hdslb.com/bfs/space/cb1c3ef50e22b6096fde67febe863494caefebad.png",
          "liveRoom": "{'roomStatus': 0, 'liveStatus': 0, 'url': '', 'title': '', 'cover': '', 'online': 0, 'roomid': 0, 'roundStatus': 0, 'broadcast_type': 0}",
          "following": 1,
          "follower": 161553,
          "video": 2777
        },
        {
          "id": 2,
          "uid": 370342489,
          "name": "ChanneLLean",
          channel: "aerobics",
          "sex": "保密",
          "face": "https://rks.cool/newbrank-img/i2.hdslb.com/bfs/face/5f7e69594cafb04e08aa79b6f6317d3649ef827c.jpg",
          "sign": "健身美食相伴 唯一商务合作VX：wxmgc3",
          "level": 6,
          "birthday": "10-05",
          "fansBadge": "1",
          "official": "{'role': 1, 'title': 'bilibili 知名运动UP主', 'desc': '', 'type': 0}",
          "vip": "{'type': 1, 'status': 1, 'theme_type': 0, 'label': {'path': '', 'text': '大会员', 'label_theme': 'vip'}, 'avatar_subscript': 1, 'nickname_color': ''}",
          "nameplate": "{'nid': 9, 'name': '出道偶像', 'image': 'https://rks.cool/newbrank-img/i2.hdslb.com/bfs/face/3f2d64f048b39fb6c26f3db39df47e6080ec0f9c.png', 'image_small': 'https://rks.cool/newbrank-img/i2.hdslb.com/bfs/face/90c35d41d8a19b19474d6bac672394c17b444ce8.png', 'level': '高级勋章', 'condition': '所有自制视频总播放数>=50万'}",
          "topPhoto": "https://rks.cool/newbrank-img/i0.hdslb.com/bfs/space/e22f5b8e06ea3ee4de9e4da702ce8ef9a2958f5a.png",
          "liveRoom": "{'roomStatus': 1, 'liveStatus': 0, 'url': 'https://live.bilibili.com/21394728', 'title': 'ChanneLLean的投稿视频', 'cover': 'https://rks.cool/newbrank-img/i0.hdslb.com/bfs/live/user_cover/c9113596cdd65cb99b75530ce40f10981f5f9d4c.jpg', 'online': 0, 'roomid': 21394728, 'roundStatus': 1, 'broadcast_type': 0}",
          "following": 99,
          "follower": 262088,
          "video": 673
        }
      ],
      listLoading: false,
      tag: 'animation'
    }
  },
  created() {
    this.getUpListByChannel()
  },
  methods: {
    getUpListByChannel() {
      this.listLoading = true
      getUpListByChannel(this.tag).then(res => {
        this.up_list = res
      }).finally(() => {
        this.listLoading = false
      })
    }
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

.up-id-container {
  display: flex;
  align-items: center;

  .div-avatar {
    width: 64px;
    height: 64px;
    margin-right: 16px;
    position: relative;

    img.avatar {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      border: 1px solid #daeff5;
      box-sizing: border-box;
      vertical-align: middle;
    }
  }

  .up-id-scope {
    font-size: 14px;
    flex: 1 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    flex-basis: 0;

    // 链接样式
    text-decoration: none;

    .up-id-scope-title {
      display: flex;
      align-items: center;
      font-size: 12px;
      flex-wrap: wrap;

      .up-id-scope-name {
        font-size: 16px;
        color: #3e4040;
        margin-right: 8px;

        &:hover {
          color: #00a0d8;
        }
      }

      .up-id-scope-level {
        padding: 0 5px;
        border: 1px solid #00a0d8;
        background-color: rgba(24, 144, 255, .1);
        color: #00a0d8;
        margin-right: 8px;
        border-radius: 4px;
      }

      .up-id-scope-category {
        padding: 0 8px;
        color: #fb7299;
        background-color: rgba(251, 114, 153, .1);
        border: 1px solid rgba(251, 114, 153, .3);
        margin-right: 8px;
        border-radius: 11px;
      }
    }

    .up-id-scope-uid {
      color: #949999;
    }

    .up-id-scope-sign {
      color: #949999;
    }
  }

  .scope-ellipsis {
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    word-break: keep-all;
  }
}

.up-id-figures {
  font-size: 16px;
  font-weight: 500;
  color: #3e4040;
}
</style>