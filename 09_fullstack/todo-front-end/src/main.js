import Vue from 'vue'
import App from './App.vue'
import router from './router'  // from './router/index.js'

Vue.config.productionTip = false

new Vue({
  router,  // router/index.js 에서 악수 하고, 본격적으로 일을 시작.
  render: h => h(App)
}).$mount('#app')
