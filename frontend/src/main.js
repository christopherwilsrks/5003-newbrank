import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import i18n from "@/lang";

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import './styles/index.less'

import ECharts from 'vue-echarts'

Vue.config.productionTip = false

Vue.use(ElementUI, {
  i18n: (key, value) => i18n.t(key, value)
})

Vue.component('v-chart', ECharts)

new Vue({
  el: '#app',
  router,
  store,
  i18n,
  render: h => h(App)
})
