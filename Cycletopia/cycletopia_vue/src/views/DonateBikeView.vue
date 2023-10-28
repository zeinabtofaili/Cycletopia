<template>
    <div>
        <div class="row g-3 shadow p-3 mb-5 bg-body rounded">
            <div class="col-md-6 d-none d-md-block position-relative">
                <img src="@/assets/kids_on_bike.png" class="img-fluid" style="min-height:100%;" />
                <p id="text-on-image" class="position-absolute top-50 start-0 translate-left">Your bike donations can help
                    someone get to work or school easier.</p>

            </div>

            <div class="col-md-6">
                <h2>Bike details</h2>
                <h6>We will pass by to get the donated bike after you submit the request.</h6>
                <div class="row">
                    <div class="form-floating col-md-12 my-2">
                        <input type="text" class="form-control" v-model="name" placeholder="Bike name">
                        <label class="form-label p-3">Bike name</label>
                    </div>

                </div>

                <br>
                <div class="d-grid gap-2 col-md-6 mx-auto">
                    <div class="input-group flex-nowraps">
                        <span class="input-group-text"><i class="fa-solid fa-image"></i></span>
                        <input class="form-control" type="file" accept="image/jpg, image/jpeg" id="imageInput"
                            v-on:change="onFileChange()">
                    </div>
                </div>

                <br>
                <div class="row">
                    <div class="form-floating col-md-4 my-2">
                        <input type="email" class="form-control" v-model="donatorEmail" placeholder="Email">
                        <label class="form-label p-3">Email</label>
                    </div>
                    <div class="form-floating col-md-4 my-2">
                        <input type="text" class="form-control" v-model="donatorPhoneNumber" placeholder="Phone">
                        <label class="form-label p-3">Phone</label>
                    </div>
                    <div class="form-floating col-md-4 my-2">
                        <input type="text" class="form-control" v-model="address" placeholder="Address">
                        <label class="form-label p-3">Address</label>
                    </div>
                </div>

                <div class="d-grid gap-2 col-md-6 mx-auto">
                    <button style="margin-top: 20px;" class="btn btn-dark" @click="submitData">Upload Bike For
                        Donation</button>

                </div>

            </div>
        </div>
        <div class="alert alert-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'DonateBikeUser',
    mounted() {
        document.title = 'Donate Your Bike | Cycletopia'
    },
    data() {
        return {
            donatorEmail: '',
            name: '',
            donatorPhoneNumber: '',
            address: '',
            productImage: undefined,
            slug: '',
            errors: []
        }
    },
    methods: {
        onFileChange(e) {
            let imageInput = document.getElementById("imageInput")
            this.productImage = imageInput.files[0]
        },
        submitData() {
            this.errors = []
            if (this.name === '') {
                this.errors.push('The name field is missing!')
            }
            if (this.donatorEmail === '') {
                this.errors.push('The email field is missing!')
            }
            if (this.donatorPhoneNumber === '') {
                this.errors.push('The phone field is missing!')
            }
            if (this.address === '') {
                this.errors.push('The address field is missing!')
            }
            if (!this.productImage) {
                this.errors.push('The image field is missing!')
            }
            if (!this.errors.length) {
                this.slug = this.name.toLowerCase().replace(/\s+/g, '-')
                const formData = {
                    donatorEmail: this.donatorEmail,
                    image: this.productImage,
                    name: this.name,
                    donatorPhoneNumber: this.donatorPhoneNumber,
                    address: this.address,
                    slug: this.slug,
                }
                const headers = { headers: { 'Content-Type': 'multipart/form-data' } }
                axios
                    .post("/api/v1/donate-bike/", formData, headers)
                    .then(response => {
                        // console.log(response)
                        this.$router.push('/donate-bike/success');

                    }).catch(error => {
                        console.log(error)

                    })
            }
        },
    },
}
</script>

<style scoped>
#text-on-image {
    font-size: 3vw;
    color: white;
    font-weight: bold;
    padding-left: 1rem;
    padding-right: 1rem;
    text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
}</style>