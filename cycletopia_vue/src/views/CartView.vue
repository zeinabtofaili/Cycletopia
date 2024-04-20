<template>

    <div class="d-flex justify-content-between align-items-center mb-4">
        <h2 class="fw-normal mb-0 text-black">Shopping Cart</h2>
    </div>

    <table class="table shadow p-3 mb-5 bg-body rounded" v-if="cartTotalLength">
        <thead class="table-light">
            <tr>
                <th scope="col">Product</th>
                <th scope="col">Price</th>
                <th scope="col">Quantity</th>
                <th scope="col">Total</th>
                <th scope="col"></th>
            </tr>
        </thead>
        <tbody>
            <CartItem v-for="item in cart.items" v-bind:key="item.product.id" v-bind:initialItem="item"
                v-on:removeFromCart="removeFromCart" />
        </tbody>
    </table>
    <p v-else>You don't have any products in your cart...</p>

    <div class="mb-4 shadow p-3 mb-5 bg-body rounded">
        <h3 class="fw-normal mb-0 text-black">Summary</h3>

        <strong>${{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items

        <hr>

        <router-link to="/cart/checkout" class="btn btn-dark">Proceed to checkout</router-link>
    </div>
</template>

<script>
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'
export default {
    name: 'CartView',
    components: {
        CartItem
    },
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
        document.title = 'Cart | Cycletopia'
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
    }
}
</script>