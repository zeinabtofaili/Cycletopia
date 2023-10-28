<template>
    <div>
        <div class="row g-3 shadow p-3 mb-5 bg-body rounded">
            <div class="col-md-6 d-none d-md-block position-relative">
                <img src="@/assets/sell.png" class="img-fluid" style="min-height:100%;" />
                <p style="font-size: 2.5em; color: white; font-weight: bold; padding-left: 1rem;" class="position-absolute top-50 start-0 translate-left">It's easy to sell <br> your bike with us.</p>

            </div>

            <div class="col-md-6">
                <h2>Bike details</h2>
                <div class="row">
                    <div class="form-floating col-md-4 my-2">
                        <input type="text" class="form-control" v-model="name" placeholder="Bike name">
                        <label class="form-label p-3">Bike name</label>
                    </div>
                    <div class="form-floating col-md-4 my-2">
                        <input type="text" class="form-control" v-model="price" placeholder="Price">
                        <label class="form-label p-3">Price</label>
                    </div>
                    <div class="form-floating col-md-4 my-2">
                        <input type="text" class="form-control" v-model="color" placeholder="Color">

                        <label class="form-label p-3">Color</label>
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
                <div class="form-floating col-md-12">
                    <input type="text" class="form-control" v-model="description" placeholder="Description">
                    <label class="form-label p-3">Description</label>
                </div>
                <br>
                <div class="row justify-content-center">

                    <div class="form-floating col-md-4 my-2">
                        <select class="form-select" v-model="grouping">
                            <option>Road</option>
                            <option>Mountain</option>
                            <option>Electric</option>

                        </select>
                        <label class="form-label p-3">Bike type (select one):</label>
                    </div>
                    <div class="form-floating col-md-4 my-2">
                        <select class="form-select" v-model="size">
                            <option>XLarge</option>
                            <option>Large</option>
                            <option>Medium</option>
                            <option>Small</option>
                        </select>
                        <label class="form-label p-3">Bike size (select one):</label>
                    </div>
                </div>
                <br>
                <div class="row">
                    <div class="form-floating col-md-4 my-2">
                        <input type="email" class="form-control" v-model="sellerEmail" placeholder="Email">
                        <label class="form-label p-3">Email</label>
                    </div>
                    <div class="form-floating col-md-4 my-2">
                        <input type="text" class="form-control" v-model="sellerPhoneNumber" placeholder="Phone">
                        <label class="form-label p-3">Phone</label>
                    </div>
                    <div class="form-floating col-md-4 my-2">
                        <input type="text" class="form-control" v-model="address" placeholder="Address">
                        <label class="form-label p-3">Address</label>
                    </div>
                </div>
                
                <div class="d-grid gap-2 col-md-6 mx-auto">
                    <button style="margin-top: 10px;" class="btn btn-dark" @click="submitData">Upload Bike For Sale</button>

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
    name: 'SellBikeUser',
    mounted() {
        document.title = 'Sell Your Bike | Cycletopia'
    },
    data() {
        return {
            sellerEmail: '',
            name: '',
            description: '',
            grouping: '',
            size: '',
            color: '',
            price: '',
            sellerPhoneNumber: '',
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
            if (this.description === '') {
                this.errors.push('The description field is missing!')
            }
            if (this.sellerEmail === '') {
                this.errors.push('The email field is missing!')
            }
            if (this.sellerPhoneNumber === '') {
                this.errors.push('The phone field is missing!')
            }
            if (this.address === '') {
                this.errors.push('The address field is missing!')
            }
            if (this.grouping === '') {
                this.errors.push('The type field is missing!')
            }
            if (this.size === '') {
                this.errors.push('The size field is missing!')
            }
            if (this.price === '') {
                this.errors.push('The price field is missing!')
            }
            if (this.color === '') {
                this.errors.push('The color field is missing!')
            }
            if (!this.productImage) {
                this.errors.push('The image field is missing!')
            }
            if (!this.errors.length) {
                this.slug = this.name.toLowerCase().replace(/\s+/g, '-')
                const formData = {
                    sellerEmail: this.sellerEmail,
                    image: this.productImage,
                    name: this.name,
                    description: this.description,
                    grouping: this.grouping,
                    size: this.size,
                    color: this.color,
                    price: this.price,
                    sellerPhoneNumber: this.sellerPhoneNumber,
                    sold: false,
                    address: this.address,
                    slug: this.slug,
                }
                const headers = { headers: { 'Content-Type': 'multipart/form-data' } }
                axios
                    .post("/api/v1/sell-bike/", formData, headers)
                    .then(response => {
                        // console.log(response)
                        this.$router.push('/sell-bike/success');

                    }).catch(error => {
                        console.log(error)

                    })
            }
        },
    },
}
</script>