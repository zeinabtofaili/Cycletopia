<template>
    <div class="col-md-3 mt-5">
        <div class="card text-center">
            <img class="card-img-top" v-bind:src="event.get_image" alt="Cycling event image">
            <div class="card-body">
                <h5 class="card-title">{{ event.name }}</h5>
                <hr>
                <iframe 
                    v-bind:src="event.map_url"
                    width="100%" height="200" frameborder="0" style="border:0" allowfullscreen></iframe>
                </div>
            <div class="card-footer text-muted">
                <div class="row">
                    <div class="col">
                        <router-link v-bind:to="event.get_absolute_url" class="btn btn-primary">View details</router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'EventCard',
    props: {
        event: Object
    }
}
</script>