import axios from 'axios';
import Vue from 'vue'
import { InertiaApp } from '@inertiajs/inertia-vue'

// register django csrf token for Inertia.post posts
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.config.productionTip = false;

Vue.use(InertiaApp)

const app = document.getElementById('app')
const page = JSON.parse(document.getElementById('page').textContent)

new Vue({
  render: h => h(InertiaApp, {
    props: {
      initialPage: page,
      resolveComponent: (component) => {
        return import(`@/pages/${component}`).then(module => module.default)
      },
    },
  }),
}).$mount(app)
