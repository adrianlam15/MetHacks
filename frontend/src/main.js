import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import VueSmoothScroll from 'vue3-smooth-scroll'
import VueKinesis from 'vue-kinesis'

import './assets/base.css'

const app = createApp(App)

app.use(router)
// app.use(VueSmoothScroll)
app.use(VueKinesis)
app.mount('#app')
