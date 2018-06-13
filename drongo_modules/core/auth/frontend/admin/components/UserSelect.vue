<template>
  <div class="form__control">
    <label>{{ label }}</label>
    <select>
      <option value="">None</option>
      <option v-for="user in userList" :value="user.username" :key="user.username">{{ user.username }}</option>
    </select>
  </div>
</template>

<script>
  import authService from '~auth/service'

  export default {
    props: ['label', 'value'],

    methods: {
      loadUsers () {
        authService.list().then((res) => {
          this.userList = res
        })
      }
    },

    mounted () {
      this.loadUsers()
    },

    data () {
      return {
        userList: []
      }
    }
  }
</script>
