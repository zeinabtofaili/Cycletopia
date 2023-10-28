<template>
    <div class="card shadow p-3 mb-5 bg-white rounded" style="width: 15rem;">
        <div class="alert alert-danger d-flex align-items-center" role="alert" v-if="bike.is_rented">
            <i class="fa-solid fa-triangle-exclamation fa-fade" style="margin-right: 4px;"></i>
            <div>
                Currently rented.
            </div>
        </div>
        <img v-bind:src="bike.get_thumbnail" class="card-img-top">
        <div class="card-body">
            <h5 class="card-title">{{ bike.name }}</h5>
            <router-link v-bind:to="bike.get_absolute_url" class="btn btn-primary" v-if="!bike.is_rented">View details</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'RentalBikeCard',
    props: {
        bike: Object
    }
}
</script>