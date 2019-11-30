import Vue from 'vue'
import App from './App.vue'
import router from './router'  // from './router/index.js'
import VueSession from 'vue-session'  // 발급받은 Token 을 SessionStorage 에 저장하는걸 도와줌.

Vue.config.productionTip = false;
Vue.use(VueSession);  // Vue 에게 VueSession 이라는 Middleware 등록 

new Vue({
  router,  // router/index.js 에서 악수 하고, 본격적으로 일을 시작.
  render: h => h(App)
}).$mount('#app');
