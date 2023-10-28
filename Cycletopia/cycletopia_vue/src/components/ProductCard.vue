<template>
    <div class="card shadow p-3 mb-5 bg-white rounded" style="width: 15rem;">
        <img v-bind:src="product.get_thumbnail" class="card-img-top">
        <div class="card-body">
            <h5 class="card-title">{{ product.name }}</h5>
            <p class="card-text">${{ product.price }}</p>
            <router-link v-bind:to="product.get_absolute_url" class="btn btn-primary">View details</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ProductBox',
    props: {
        product: Object
    }
}
</script>