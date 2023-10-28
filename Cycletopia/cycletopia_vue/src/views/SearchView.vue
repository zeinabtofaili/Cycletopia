<template>
    <div class="jumbotron">
        <h1>Search</h1>

        <h3 class="text-secondary">Search term: "{{ query }}"</h3>
    </div>

    <div class="flexbox">
        <ProductCard class="flex-item" v-for="product in products" v-bind:key="product.id" v-bind:product="product" />

    </div>
</template>

<script>
import axios from 'axios'
import ProductCard from '@/components/ProductCard.vue'

export default {
    name: 'Search',
    components: {
        ProductCard
    },
    data() {
        return {
            products: [],
            query: ''
        }
    },
    mounted() {
        document.title = 'Search | Cycletopia'

        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')

            this.performSearch()
        }
    },
    methods: {
        async performSearch() {
            this.$store.commit('setIsLoading', true)

            await axios
                .post('/api/v1/products/search/', { 'query': this.query })
                .then(response => {
                    this.products = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>