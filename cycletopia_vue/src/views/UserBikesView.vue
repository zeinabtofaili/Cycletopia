<template>
    <div class="jumbotron">
        <h1 class="text-center">Choose a bike to buy</h1>
    </div>
    <div class="flexbox">
        <ProductCard class="flex-item" v-for="product in this.products" v-bind:key="product.id"
            v-bind:product="product" />
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import ProductCard from '@/components/UserBikeCard'

export default {
    name: 'AllUserBikesView',
    components: {
        ProductCard
    },
    setup() {
        const notify = () => {
            toast("Something went wrong. Please try again.", {
                autoClose: 1000,
                position: 'bottom-right',
                type: 'error',
            }); // ToastOptions
        }
        return { notify };
    },
    data() {
        return {
            products: []
            
        }
    },
    mounted() {
        document.title = ' User Bikes | Cycletopia'
        this.getBikes();
    },
    methods: {
        async getBikes() {
            this.$store.commit('setIsLoading', true)

            axios
                .get(`/api/v1/all-user-bikes/`)
                .then(response => {
                    this.products = response.data

                })
                .catch(error => {
                    console.log(error);

                    this.notify();
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>