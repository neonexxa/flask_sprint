<template>
	<nav class="navbar navbar-expand-lg navbar-dark bg-dark rounded">
		<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar1" aria-controls="navbar1" aria-expanded="false" aria-label="Toggle Navigation">
			<span class="navbar-toggler-icon"></span>
		</button>
		<div class="collapse navbar-collapse justify-md-center" id="navbar1">
			<ul class="navbar-nav">
				<li class="nav-item">
					<router-link class="nav-link" to="/">Home</router-link>
				</li>
				<li class="nav-item" v-if="auth==''">
					<router-link class="nav-link" to="/login">Login</router-link>
				</li>
				<li class="nav-item" v-if="auth==''">
					<router-link class="nav-link" to="/register">Register</router-link>
				</li>
				<li class="nav-item" v-if="auth=='loggedin'">
					<router-link class="nav-link" to="/profile">Profile</router-link>
				</li>
				<li class="nav-item" v-if="auth=='loggedin'">
					<a href="" class="nav-link" v-on:click="logout">Logout</a>
				</li>
			</ul>
		</div>
	</nav>
</template>

<script>
import EventBus from './EventBus'
/* eslint-disable indent */
/* eslint space-before-function-paren: ["error", "never"] */
EventBus.$on('logged-in', test => {
	console.log(test)
})

export default {
	data() {
		return {
			auth: '',
			user: ''
		}
	},
	methods: {
		logout() {
			localStorage.removeItem('usertoken')
		}
	},
	mounted() {
		EventBus.$on('logged-in', status => {
			this.auth = status
		})
	}
}
</script>
