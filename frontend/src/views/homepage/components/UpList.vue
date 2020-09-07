<template>
  <div class="up-list-container">
    <el-table
        :data="up_list"
        highlight-current-row
        ref="multipleTable"
        style="width: 100%"
        v-loading.body="listLoading"
    >
      <!-- up主号 -->
      <el-table-column label="up主号" min-width="200px">
        <template slot-scope="scope">
          <div class="up-id-container">
            <div class="div-avatar">
              <img class="avatar" :src="scope.row.avatar_url" alt="avatar">
            </div>
<!--            <div class="up-id-scope">-->
              <router-link class="up-id-scope scope-ellipsis" :to="`/up/${scope.row.uid}`">
              <div class="up-id-scope-title">
                <span class="up-id-scope-name">{{scope.row.name}}</span>
                <span class="up-id-scope-level">lv{{scope.row.level}}</span>
                <span class="up-id-scope-category">{{scope.row.category}}</span>
              </div>
              <span class="up-id-scope-uid">Uid: {{scope.row.uid}}</span>
              <span class="up-id-scope-sign scope-ellipsis">个性签名：{{scope.row.signature}}</span>
              </router-link>
<!--            </div>-->
          </div>
        </template>
      </el-table-column>
      <!-- 作品数 -->
      <el-table-column align="left" label="作品数">
        <template slot-scope="scope">
          <span>{{scope.row.works_count}}</span>
        </template>
      </el-table-column>
      <!-- 获赞数 -->
      <el-table-column align="center" label="获赞数">
        <template slot-scope="scope">
          <span>{{scope.row.likes_count}}</span>
        </template>
      </el-table-column>
      <!-- 充电人数 -->
      <el-table-column align="center" label="充电人数">
        <template slot-scope="scope">
          <span>{{scope.row.charges_count}}</span>
        </template>
      </el-table-column>
      <!-- 粉丝数 -->
      <el-table-column align="center" label="粉丝数">
        <template slot-scope="scope">
          <span>{{scope.row.fans_count}}</span>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "UpList",
  data() {
    return {
      up_list: [
        {
          name: '老番茄',
          uid: '546195',
          level: 6,
          category: '动画',
          signature: '新浪微博：_老番茄_',
          works_count: '348',
          likes_count: '6591.04w',
          charges_count: '3.55w',
          fans_count: '1291.61w',
          avatar_url: '//i2.hdslb.com/bfs/face/bc5ca101313d4db223c395d64779e76eb3482d60.jpg_64x64.jpg'
        },
        {
          name: '罗翔说刑法',
          uid: '517327498',
          category: '知识',
          level: 6,
          signature: '个性签名：厚大法考刑法独家授课老师',
          works_count: '95',
          likes_count: '2690.58w',
          charges_count: '--',
          fans_count: '931.80w',
          avatar_url: 'http://i0.hdslb.com/bfs/face/4e5d0a51273fe3f8fabc700b6a71bb8a38c9e21e.jpg@100w_100h_100Q_1c.webp'
        }
      ],
      listLoading: false
    }
  }
}
</script>

<style lang="scss" scoped>
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
        background-color: rgba(24,144,255,.1);
        color: #00a0d8;
        margin-right: 8px;
        border-radius: 4px;
      }
      .up-id-scope-category {
        padding: 0 8px;
        color: #fb7299;
        background-color: rgba(251,114,153,.1);
        border: 1px solid rgba(251,114,153,.3);
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
</style>