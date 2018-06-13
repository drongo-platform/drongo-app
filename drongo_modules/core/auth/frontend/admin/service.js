import axios from 'axios'

export default {
  login ({username, password}) {
    return new Promise((resolve, reject) => {
      axios.post(
        `${process.env.apiUrl}/auth/users/operations/login`,
        {
          username: username,
          password: password
        }
      ).then((resp) => {
        if (resp.data.status === 'OK') {
          resolve({token: resp.data.payload.token})
        }
      }).catch((err) => {
        reject(err.response.data.errors)
      })
    })
  },

  logout () {
    return new Promise((resolve, reject) => {
      axios.get(
        `${process.env.apiUrl}/auth/users/operations/logout`
      ).then((resp) => {
        resolve('OK')
      }).catch((err) => {
        reject(err)
      })
    })
  },

  list () {
    return new Promise((resolve, reject) => {
      axios.get(
        `${process.env.apiUrl}/auth/users`
      ).then((resp) => {
        resolve(resp.data.payload)
      }).catch((err) => {
        reject(err)
      })
    })
  }
}
