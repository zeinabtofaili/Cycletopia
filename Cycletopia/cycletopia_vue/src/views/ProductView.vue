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
                                    <div class="price d-flex flex-row align-items-center"> <span class="act-price">${{
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
                                    <h6 class="text-uppercase" v-if="product.grouping !== null">Category: {{
                                        product.grouping
                                    }}</h6>
                                </div>
                                <div class="sizes mt-5">
                                    <h6 class="text-uppercase" v-if="product.gender !== null">Gender: {{
                                        product.gender
                                    }}</h6>
                                </div>
                                <div class="sizes mt-5">
                                    <h6 class="text-uppercase" v-if="product.color !== null">Color: <i
                                            class="fa-solid fa-circle fa-border" id="circle"></i> {{
                                                product.color
                                            }}</h6>
                                </div>
                                <div class="cart mt-4 align-items-center">
                                    <div class="input-group mb-3">
                                        <input type="number" class="form-control" min="1" v-model="quantity">
                                        <button class="btn btn-dark text-uppercase mr-2 px-4" @click="addToCart(); notify();">Add to
                                            cart</button>

                                    </div>
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
    name: 'Product',
    setup() {
        const notify = () => {
            toast("The product was added to the cart!", {
                autoClose: 1000,
                position: 'bottom-right',
                type: 'success',
            }); // ToastOptions
        }
        return { notify };
    },
    data() {
        return {
            product: {},
            quantity: 1
        }
    },
    mounted() {
        this.getProduct()
    },
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)

            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/products/${category_slug}/${product_slug}`)
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
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)

        }
    }
}
</script>
<style scoped>
#product-image {
    width: 100%;
}
</style>