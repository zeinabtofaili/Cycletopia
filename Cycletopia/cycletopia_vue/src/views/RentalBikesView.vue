<template>
    <div class="jumbotron">
        <h1 class="text-center">Bikes For Rent</h1>
        <h6>Please login before viewing bikes deatils.</h6>
    </div>
    <div class="flexbox">
        <RentalBikeCard class="flex-item" v-for="bike in bikes" v-bind:key="bike.id"
            v-bind:bike="bike" />
    </div>

</template>

<script>
import axios from 'axios'
import RentalBikeCard from '@/components/RentalBikeCard'
export default {
    name: 'RentalBikesView',
    data() {
        return {
            bikes: []
        }
    },
    components: {
        RentalBikeCard,
    },
    mounted() {
        this.getRentalBikes()
        document.title = 'Rental Bikes | Cycletopia'
    },
    methods: {
        async getRentalBikes() {
            this.$store.commit('setIsLoading', true)
            await axios
                .get('/api/v1/rent-bike/')
                .then(response => {
                    this.bikes = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        }
    }

}
</script>

<style scoped>

</style>