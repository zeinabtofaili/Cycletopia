<template>
    <section>
        <h1 class="text-center" style="margin-top: 2.5rem; margin-bottom: 2.5rem;">Login to Cycletopia</h1>
        <div class="container-fluid h-custom" style=" margin-bottom: 2.5rem;">
            <div class="row d-flex justify-content-center align-items-center">
                <div class="col-md-9 col-lg-6 col-xl-5">
                    <img src="@/assets/cycletopiaLogo.png" class="img-fluid" alt="Cycletopia logo"
                        style="margin-bottom: 2.5rem;">
                </div>
                <div class="col-md-8 col-lg-6 col-xl-4 offset-xl-1">
                    <form @submit.prevent="submitForm">

                        <div class="form-outline mb-4">
                            <input type="text" class="form-control form-control-lg" placeholder="Username"
                                v-model="username" />
                        </div>

                        <div class="form-outline mb-3">
                            <input type="password" class="form-control form-control-lg" placeholder="Password"
                                v-model="password" />
                        </div>
                        <div class="alert alert-danger" v-if="errors.length">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>

                        <div class="text-center text-lg-start mt-4 pt-2">
                            <button class="btn btn-primary ">Login</button>
                            <p class="small fw-bold mt-2 pt-1 mb-0">Don't have an account? <a
                                    href="/sign-up">Register</a></p>
                        </div>

                    </form>
                </div>
            </div>
        </div>
    </section>

</template>
<script>
import axios from 'axios'
export default {
    name: 'LoginView',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Login | Cycletopia'
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            const formData = {
                username: this.username,
                password: this.password
            }
            await axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)

                    axios.defaults.headers.common["Authorization"] = "Token " + token
                    localStorage.setItem("token", token)
                    const toPath = this.$route.query.to || '/'
                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')

                        console.log(JSON.stringify(error))
                    }
                })
        }
    }
}
</script>
<style scoped>

.h-custom {
    height: calc(100% - 73px);
}

@media (max-width: 450px) {
    .h-custom {
        height: 100%;
    }
}
</style>