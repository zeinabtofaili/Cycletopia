<template>
    <div class="jumbotron">
        <h1 class="text-center">{{ category.name }}</h1>
    </div>
    <div class="flexbox">
        <ProductCard class="flex-item" v-for="product in category.products" v-bind:key="product.id"
            v-bind:product="product" />
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import ProductCard from '@/components/ProductCard'

export default {
    name: 'CategoryView',
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
            category: {
                products: []
            }
        }
    },
    mounted() {
        this.getCategory()
    },
    watch: {
        $route(to, from) {
            if (to.name === 'Category') {
                this.getCategory()
            }
        }
    },
    methods: {
        async getCategory() {
            const categorySlug = this.$route.params.category_slug
            this.$store.commit('setIsLoading', true)

            axios
                .get(`/api/v1/products/${categorySlug}/`)
                .then(response => {
                    this.category = response.data

                    document.title = this.category.name + ' | Cycletopia'
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