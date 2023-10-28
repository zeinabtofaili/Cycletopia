<template>

    <h1 class="title">Checkout</h1>

    <div>
        <table class="table shadow p-3 mb-5 bg-body rounded">
            <thead class="table-light">
                <tr>
                    <th scope="col">Product</th>
                    <th scope="col">Price</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Total</th>
                </tr>
            </thead>

            <tbody>
                <tr v-for="item in cart.items" v-bind:key="item.product.id">
                    <td>{{ item.product.name }}</td>
                    <td>${{ item.product.price }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>${{ getItemTotal(item).toFixed(2) }}</td>
                </tr>
            </tbody>

            <tfoot>
                <tr>
                    <td colspan="2">Total</td>
                    <td>{{ cartTotalLength }}</td>
                    <td>${{ cartTotalPrice.toFixed(2) }}</td>
                </tr>
            </tfoot>
        </table>
    </div>

    <div>
        <div class="shadow p-3 mb-5 bg-body rounded">
            <h2>Shipping details</h2>

            <p class="text-secondary mb-4">* All fields are required</p>

            <div class="row g-3">
                <div class="col-md-6">
                    <label class="form-label">First name*</label>
                    <input type="text" class="form-control" v-model="first_name">
                </div>
                <div class="col-md-6">
                    <label class="form-label">Last name*</label>
                    <input type="text" class="form-control" v-model="last_name">
                </div>
                <div class="col-md-6">
                    <label class="form-label">Email*</label>
                    <input type="email" class="form-control" v-model="email">
                </div>
                <div class="col-md-6">
                    <label class="form-label">Phone*</label>
                    <input type="text" class="form-control" v-model="phone">
                </div>
                <div class="col-12">
                    <label class="form-label">Address*</label>
                    <input type="text" class="form-control" v-model="address">
                </div>
                <div class="col-md-6">
                    <label class="form-label">Zip code*</label>
                    <input type="text" class="form-control" v-model="zipcode">
                </div>
                <div class="col-md-6">
                    <label class="form-label">Place*</label>
                    <input type="text" class="form-control" v-model="place">
                </div>

                <div class="alert alert-danger" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

            </div>
            <hr>

            <div id="card-element" class="mb-2"></div>

            <template v-if="cartTotalLength">
                <hr>

                <button class="btn btn-dark" @click="submitForm">Pay with Stripe</button>
            </template>
        </div>

    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'CheckoutView',
    data() {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            zipcode: '',
            place: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Checkout | Cycletopia'

        this.cart = this.$store.state.cart

        if (this.cartTotalLength > 0) {
            this.stripe = Stripe('pk_test_51MOe4BG04ADJG9CuiGwsIqQTORFw3OIZ1OX2H75ZhemEQ0SqcoxDE76D4L2E9oWmsOIdtOI1GR8QXwBMzMN0uIWP00BhTqeZr4')
            const elements = this.stripe.elements();
            this.card = elements.create('card', { hidePostalCode: true })

            this.card.mount('#card-element')
        }
    },
    methods:{
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        submitForm() {
            this.errors = []
            if (this.first_name === '') {
                this.errors.push('The first name field is missing!')
            }
            if (this.last_name === '') {
                this.errors.push('The last name field is missing!')
            }
            if (this.email === '') {
                this.errors.push('The email field is missing!')
            }
            if (this.phone === '') {
                this.errors.push('The phone field is missing!')
            }
            if (this.address === '') {
                this.errors.push('The address field is missing!')
            }
            if (this.zipcode === '') {
                this.errors.push('The zip code field is missing!')
            }
            if (this.place === '') {
                this.errors.push('The place field is missing!')
            }
            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)
                this.stripe.createToken(this.card).then(result => {                    
                    if (result.error) {
                        this.$store.commit('setIsLoading', false)
                        this.errors.push('Something went wrong with Stripe. Please try again')
                        console.log(result.error.message)
                    } else {
                        this.stripeTokenHandler(result.token)
                    }
                })
            }
        },
        async stripeTokenHandler(token) {
            const items = []
            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                    product: item.product.id,
                    quantity: item.quantity,
                    price: item.product.price * item.quantity
                }
                items.push(obj)
            }
            const data = {
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'address': this.address,
                'zipcode': this.zipcode,
                'place': this.place,
                'phone': this.phone,
                'items': items,
                'stripe_token': token.id
            }
            await axios
                .post('/api/v1/checkout/', data)
                .then(response => {
                    this.$store.commit('clearCart')
                    this.$router.push('/cart/success')
                })
                .catch(error => {
                    this.errors.push('Something went wrong. Please try again')
                    console.log(error)
                    
                })
                this.$store.commit('setIsLoading', false)
        }
    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        }
    }
}
</script>