<template>
    <div class="container mt-5 mb-5">
        <div class="row d-flex justify-content-center">
            <div class="col-md-10">
                <div class="card">
                    <div class="row">
                        <div class="col-md-6">
                            <div class="images p-3">
                                <div class="text-center p-4"> <img v-bind:src="product.get_image" id="product-image" /> </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="product p-4">
                                <div class="mt-4 mb-3">
                                    <h5 class="text-uppercase">{{ product.name }}</h5>
                                    <div class="price d-flex flex-row align-items-center"> <span class="act-price">{{
                                        product.price
                                    }}</span>

                                    </div>
                                </div>
                                <p class="about">{{ product.description }}
                                </p>
                                <div class="sizes mt-5">
                                    <h6 class="text-uppercase">Size: {{ product.size }}</h6>
                                </div>
                                <div class="sizes mt-5">
                                    <h6 class="text-uppercase">Category: {{
                                        product.grouping
                                    }}</h6>
                                </div>
                                <div class="sizes mt-5">
                                    <h6 class="text-uppercase">Color:<i
                                            class="fa-solid fa-circle fa-border" id="circle"></i> {{
                                                product.color
                                            }}</h6>
                                </div>
                                <div class="sizes mt-5">
                                    <h6 ><span class="text-uppercase">Address: </span>{{ product.address }}</h6>
                                </div>
                                <hr>
                                <div class="sizes mt-3">
                                    <h5>Contact Seller:</h5>
                                    <h6 class="sizes mt-3"><i class="fa fa-envelope" aria-hidden="true" style="margin-right: 5px;"></i>By email: <a :href="'mailto:' +  product.sellerEmail">{{ product.sellerEmail }}</a></h6>
                                    <h6 class="sizes mt-3"><i class="fa-solid fa-phone" aria-hidden="true" style="margin-right: 5px;"></i>By phone: {{ product.sellerPhoneNumber}}</h6>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

export default {
    name: 'UserBike',
    data() {
        return {
            product: {},
        }
    },
    mounted() {
        this.getProduct()
    },
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)

            const product_slug = this.$route.params.bike_slug
            console.log(product_slug)
            await axios
                .get(`/api/v1/user-bike/${product_slug}/`)
                .then(response => {
                    this.product = response.data

                    document.title = this.product.name + ' | Cycletopia'
                    if (this.product.color != null) {
                        document.getElementById('circle').style.color = this.product.color;
                        if (document.getElementById('circle').style.color.toLowerCase() != this.product.color.toLowerCase()) {
                            document.getElementById('circle').style.display = 'none';
                        }
                    }
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
    }
}
</script>
<style scoped>
#product-image {
    width: 100%;
}
</style>