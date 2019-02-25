import Vue from 'vue'
import Chat from 'vue-beautiful-chat'
import vmodal from 'vue-js-modal'
import App from './App.vue'
import router from './router'
import store from './store'

import './filters'

Vue.config.productionTip = false
Vue.use(vmodal, { dialog: true })
Vue.use(Chat, {})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
