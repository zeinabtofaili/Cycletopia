<template>
    <div class="jumbotron">
        <h1 class="text-center">Cycling Events</h1>
        <p class="text-center">You must be logged in to view cycling events and register in them.</p>
    </div>
    <div class="flexbox">
        <EventCard class="flex-item" v-for="event in cyclingEvents" v-bind:key="event.id"
            v-bind:event="event" />
    </div>

</template>

<script>
import axios from 'axios'
import EventCard from '@/components/CyclingEventCard'
export default {
    name: 'CyclingEventsView',
    data() {
        return {
            cyclingEvents: []
        }
    },
    components: {
        EventCard,
    },
    mounted() {
        this.getCyclingEvents()
        document.title = 'Cycling Events | Cycletopia'
    },
    methods: {
        async getCyclingEvents() {
            this.$store.commit('setIsLoading', true)
            await axios
                .get('/api/v1/cycling-events/')
                .then(response => {
                    this.cyclingEvents = response.data
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