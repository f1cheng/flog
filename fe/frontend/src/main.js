// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import {mavonEditor} from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
//import axios from 'axios'
import axios from "./axios/interceptor"
import Vuex from 'vuex'
import store from './store'

import hljs from 'highlight.js';
import 'highlight.js/styles/atom-one-dark.css'
 
//create v-highlight global instruction
Vue.directive('highlight',function (el) {
  let blocks = el.querySelectorAll('pre code');
  blocks.forEach((block)=>{
    hljs.highlightBlock(block)
  })
})

Vue.use(Vuex)
Vue.use(ElementUI)
Vue.use(mavonEditor)
Vue.config.productionTip = false
axios.defaults.baseURL = 'http://111.230.243.15:9000/'
Vue.prototype.$axios = axios
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
