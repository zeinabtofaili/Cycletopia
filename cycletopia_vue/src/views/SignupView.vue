<template>
    <section>
        <h1 class="text-center" style="margin-top: 2.5rem; margin-bottom: 2.5rem;">Sigup to Cycletopia</h1>

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
                        <div class="form-outline mb-3">
                            <input type="password" class="form-control form-control-lg" placeholder="Repeat password"
                                v-model="password2" />
                        </div>

                        <div class="alert alert-danger" v-if="errors.length">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>

                        <div class="text-center text-lg-start mt-4 pt-2">
                            <button class="btn btn-primary ">Signup</button>
                            <p class="small fw-bold mt-2 pt-1 mb-0">Already have an account? <a href="/log-in">Login</a>
                            </p>
                        </div>

                    </form>
                </div>
            </div>
        </div>
    </section>

</template>
<script>
import axios from 'axios'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
export default {
    name: 'SignupView',
    mounted() {
        document.title = 'Signup | Cycletopia'
    },
    data() {
        return {
            username: '',
            password: '',
            password2: '',
            errors: []
        }
    },
    setup() {
        const notify = () => {
            toast("Account created, please log in!", {
                autoClose: 2000,
                position: 'bottom-right',
                type: 'success',
            }); // ToastOptions
        }
        return { notify };
    },
    methods: {
        submitForm() {
            this.errors = []
            if (this.username === '') {
                this.errors.push('The username is missing.')
            }
            if (this.password === '') {
                this.errors.push('The password is too short.')
            }
            if (this.password !== this.password2) {
                this.errors.push('The passwords don\'t match.')
            }
            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }
                axios
                    .post("/api/v1/users/", formData)
                    .then(response => {
                        this.notify();
                        this.$router.push('/log-in')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')

                            console.log(JSON.stringify(error))
                        }
                    })
            }
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