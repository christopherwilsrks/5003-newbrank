<template>
  <div class="navbar">
    <el-row style="height: 100%" type="flex" justify="space-between">
      <el-col :span="16" :xs="0">

        <!-- logo部分 -->
        <div class="left-menu">
          <router-link to="/">
            <img class="logo logo-left" src="@/assets/logo/logo.png" alt="logo" />
            <img class="logo" src="@/assets/logo/logo_text.png" alt="logo"/>
          </router-link>
        </div>
      </el-col>
      <el-col :xs="10" :md="0">

        <!-- logo部分 -->
        <div class="left-menu">
          <router-link to="/">
            <img class="logo" src="@/assets/logo/logo_text.png" alt="logo"/>
          </router-link>
        </div>
      </el-col>
      <el-col :span="8">
        <!-- 登录、登出以及用户头像 -->
        <div class="right-menu">
          <el-dropdown trigger="click" class="international" @command="handleSetLanguage">
            <div style="cursor: pointer">
              • • •
            </div>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item :disabled="language==='zh'" command="zh">
                中文
              </el-dropdown-item>
              <el-dropdown-item :disabled="language==='en'" command="en">
                English
              </el-dropdown-item>
              <el-dropdown-item :disabled="false" command="relation">
                {{$t('relation_chart')}}
              </el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  computed: {
    language() {
      return this.$store.getters.language
    }
  },
  methods: {
    handleSetLanguage(lang) {
      if (lang === 'relation') {
        this.$router.push('/' + lang + '/animation')
        return
      }
      this.$i18n.locale = lang
      this.$store.dispatch('app/setLanguage', lang)
      this.$message({
        message: this.$t('message.lang_switch_success'),
        type: 'success'
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.navbar {
  height: 50px;
  overflow: hidden;
  position: relative;
  background: #fff;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);
  border-bottom: 5px solid #fa6486;
  margin-bottom: 20px;

  .left-menu {
    float: left;
    height: 50px;

    .logo {
      //width: 100%;
      height: 100%;
    }
    .logo.logo-left{
      margin-left: 20px;
    }
  }

  .hamburger-container {
    line-height: 46px;
    height: 100%;
    float: left;
    cursor: pointer;
    transition: background 0.3s;
    -webkit-tap-highlight-color: transparent;

    &:hover {
      background: rgba(0, 0, 0, 0.025);
    }
  }

  .breadcrumb-container {
    float: left;
  }

  .errLog-container {
    display: inline-block;
    vertical-align: top;
  }

  .right-menu {
    margin-right: 3em;
    float: right;
    height: 100%;
    line-height: 50px;

    i.command {
      &:hover {
        cursor: pointer;
      }
    }
    a {
      text-decoration: none;
    }

    &:focus {
      outline: none;
    }

    .right-menu-item {
      // display: inline-block;
      padding: 0 8px;
      height: 100%;
      font-size: 18px;
      // color: #5a5e66;
      vertical-align: text-bottom;

      &.hover-effect {
        cursor: pointer;
        transition: background 0.3s;

        &:hover {
          background: rgba(0, 0, 0, 0.025);
        }
      }
    }

    .avatar-container {
      margin-right: 30px;

      .avatar-wrapper {
        margin-top: 5px;
        position: relative;

        .user-avatar {
          cursor: pointer;
          width: 40px;
          height: 40px;
          border-radius: 10px;
        }

        .el-icon-caret-bottom {
          cursor: pointer;
          position: absolute;
          right: -20px;
          top: 25px;
          font-size: 12px;
        }
      }
    }
  }
}
</style>