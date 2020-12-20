<template>
  <el-card :body-style="{ padding: '20px' }" class="container" shadow="hover">

    <el-row class="header header1" :gutter="10" justify="space-between" align="center" type="flex">
      <el-col :span="6">
        <a :href="bili_uper_url + id" target="_blank">
          <img class="avatar" :src="uperInfo.face" alt="avatar"/>
        </a>
      </el-col>
      <el-col :span="12"><span class="fan-key">{{$t('upinfo.fans')}}</span> <span class="fan-value">{{ uperInfo.follower }}</span>
      </el-col>
    </el-row>

    <div class="header header2">
      <span class="name">{{ uperInfo.name }}</span>
      <span class="category">{{ $t('channels.' + uperInfo.channel) }}</span>
    </div>

    <div class="header header3">
      <span class="key">uid: </span>
      <span class="value">{{ uperInfo.uid }}</span>
    </div>

  </el-card>
</template>

<script>

export default {
  name: "UpInfo",
  props: ["id", "uperInfo"],
  data() {
    return {
      bili_uper_url: 'https://space.bilibili.com/',
    }
  }
}
</script>

<style lang="scss" scoped>
.header {
  margin-bottom: 10px;
  color: #949999;
}
.header1 {
  align-items: center;

  img.avatar {
    width: 68px;
    height: 68px;
    border-radius: 50%;
    border: 1px solid #daeff5;
    box-sizing: border-box;
    vertical-align: middle;
  }

  .fan-key {
    margin-right: 4px;
    color: #babfbf;
    font-size: 12px;
  }

  .fan-value {
    color: #00a0d8;
    font-size: 20px;
    font-weight: 500;
    margin-left: 4px;
  }
}

.header2 {
  .name {
    font-size: 20px;
    color: #3e4040;
    font-weight: 700;
    margin-right: 8px;
  }

  .category {
    padding: 0 8px;
    color: #fb7299;
    background-color: rgba(251, 114, 153, .1);
    border: 1px solid rgba(251, 114, 153, .3);
    margin-right: 8px;
    border-radius: 11px;
  }
}

.header3 .value {
  color: #636666;
}
</style>