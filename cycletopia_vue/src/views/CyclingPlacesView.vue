<template>
    <div class="jumbotron">
        <h1 class="text-center">Cycling Places</h1>
    </div>
    <div class="flexbox">
        <PlaceCard class="flex-item" v-for="place in cyclingPlaces" v-bind:key="place.id"
            v-bind:place="place" />
    </div>

</template>

<script>
import axios from 'axios'
import PlaceCard from '@/components/CyclingPlaceCard'
export default {
    name: 'CyclingPlacesView',
    data() {
        return {
            cyclingPlaces: []
        }
    },
    components: {
        PlaceCard,
    },
    mounted() {
        this.getCyclingPlaces()
        document.title = 'Cycling Places | Cycletopia'
    },
    methods: {
        async getCyclingPlaces() {
            this.$store.commit('setIsLoading', true)
            await axios
                .get('/api/v1/cycling-places/')
                .then(response => {
                    this.cyclingPlaces = response.data
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