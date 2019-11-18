import Vue from 'vue';
import App from './App';  // App.vue 를 알아서 확장자 버리고 읽음

new Vue({
    render: h => h(App),  // 유일하게 method 인데 Arrow Function
}).$mount('#app')  // el: '#app' 와 같다.