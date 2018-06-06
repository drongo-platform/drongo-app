// Register Auth components
import Vue from 'vue'

import ImagePicker from '~media/components/ImagePicker'

Vue.component('d-media-imagepicker', ImagePicker)

// Register the media store
// const files = require.context('~auth/store', true, /^\.\/(?!-)[^.]+\.(js)$/)
// export default ({store}) => {
//   store.registerModule('auth', {
//     ...files('./index.js'),
//     namespaced: true
//   })
// }
