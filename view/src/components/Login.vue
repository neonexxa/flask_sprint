<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6 mt-5 mx-auto">
        <form v-on:submit.prevent="login">
          <h1 class="h3 mb-3 font-weight-normal">Please Sign In</h1>
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" v-model="email" class="form-control" placeholder="Enter email">
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" v-model="password" class="form-control" placeholder="*********">
          </div>
          <button class="btn btn-lg btn-primary btn-block">Sign In</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router'
import EventBus from './EventBus'
/* eslint-disable indent */
/* eslint space-before-function-paren: ["error", "never"] */
export default {
	data() {
		return {
			email: '',
			password: ''
		}
	},
	methods: {
		login() {
			axios.post('user/login', {
				email: this.email,
				password: this.password
			}).then(res => {
				localStorage.setItem('usertoken', res.data.token)
				this.email = ''
				this.password = ''
				router.push({name: 'Profile'})
			}).catch(err => {
				console.log(err)
			})
			this.emitMethod()
		},
		emitMethod() {
			EventBus.$emit('logged-in', 'loggedin')
		}
	}
}

</script>
