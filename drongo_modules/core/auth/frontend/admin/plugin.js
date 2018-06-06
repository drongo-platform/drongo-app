// Register Auth components
import Vue from 'vue'

import Login from '~auth/components/Login'
import Register from '~auth/components/Register'
import LoginInfo from '~auth/components/LoginInfo'

Vue.component('d-auth-login', Login)
Vue.component('d-auth-register', Register)
Vue.component('d-auth-logininfo', LoginInfo)

// Register the auth store
const files = require.context('~auth/store', true, /^\.\/(?!-)[^.]+\.(js)$/)
export default ({store}) => {
  store.registerModule('auth', {
    ...files('./index.js'),
    namespaced: true
  })
}
