<template>
  <div class="home">
    <div class="d-flex h-100 text-center">
      <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">

        <main class="px-3">
          <h1 style="margin-bottom: 2rem;">Welcome to Cycletopia</h1>
          <p class="lead">Zero emissions, Zero excuses.</p>
          <p>
            <img src="@/assets/bicycle.jpg" style="width: -webkit-fill-available;">
          </p>
        </main>

        <div class="column is-12">
          <h2 class="is-size-2 has-text-centered" style="margin-bottom: 2rem;">Latest products</h2>
        </div>

      </div>
    </div>

    <div class="flexbox">
      <ProductCard class="flex-item" v-for="product in latestProducts" v-bind:key="product.id"
        v-bind:product="product" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ProductCard from '@/components/ProductCard'
export default {
  name: 'HomeView',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {
    ProductCard
  },
  mounted() {
    this.getLatestProducts()
    document.title = 'Home | Cycletopia'
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)
      await axios
        .get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

