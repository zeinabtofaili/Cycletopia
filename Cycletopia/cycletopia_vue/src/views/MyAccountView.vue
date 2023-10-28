<template>
    <h1 style="margin-bottom:2.5rem;">My account</h1>
    <hr>

    <div>
        <h2>My orders</h2>

        <OrderSummary v-for="order in orders" v-bind:key="order.id" v-bind:order="order" />
    </div>

    <div>
        <h2>My bikes</h2>
        <table class="table shadow p-3 mb-5 bg-body rounded">
            <thead class="bg-light">
                <tr>
                    <th class="ms-3">Image</th>
                    <th>Name</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <!-- <UserBikes v-for="bike in bikes" v-bind:key="bike.id" v-bind:bike="bike" /> -->
                <tr v-for="bike in bikes" v-bind:key="bike.id">
                    <td class="ms-3">
                        <img v-bind:src="bike.get_thumbnail" alt="" style="width: 45px; height: 45px" />
                    </td>
                    <td>
                        <div class="">
                            <p class="fw-bold mb-1">{{ bike.name }}</p>
                            <p class="text-muted mb-0">{{ bike.price }}</p>
                        </div>
                    </td>

                    <td>
                        <a class="text-danger" @click="changeBikeIdToDelete(bike.id)">
                            <i class="fas fa-trash fa-lg"></i>
                        </a>
                    </td>
                </tr>
            </tbody>
        </table>

    </div>
    <button @click="logout()" class="btn btn-danger">Log out</button>

    <Modal v-model="showModal" title="Delete Bike">
        <h5>Are you sure you want to delete this bike?</h5>
        <p>This action cannot be undone.</p>

        <br />
        <div>
            <button class="btn btn-danger" id="deleteButton" @click="deleteBike()">Delete</button>
            <button class="btn btn-secondary" id="cancelButton" @click="showModal = false">Cancel</button>
        </div>
        <br />
        <br />
    </Modal>

</template>

<script>
import axios from 'axios'
import OrderSummary from '@/components/OrderSummary.vue'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

import VueModal from '@kouts/vue-modal'
import '@kouts/vue-modal/dist/vue-modal.css'
export default {
    name: 'MyAccountView',
    components: {
        OrderSummary,
        'Modal': VueModal
    },
    setup() {
        const notify = () => {
            toast("Delete bike successful. Please refresh the page to view changes.", {
                autoClose: 2000,
                position: 'bottom-right',
                type: 'success',
            }); // ToastOptions
        }
        return { notify };
    },
    data() {
        return {
            orders: [],
            bikes: [],
            bikeIdtoDel: 0,
            showModal: false,
        }
    },
    mounted() {
        document.title = 'My account | Cycletopia'

        this.getMyOrders();
        this.getMyBikes();
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")
            localStorage.removeItem("userid")
            localStorage.removeItem("username")

            this.$store.commit('removeToken')

            this.$router.push('/')
        },
        async getMyOrders() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/orders/')
                .then(response => {
                    this.orders = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
        async getMyBikes() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/current-user-bikes/')
                .then(response => {
                    this.bikes = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
        async deleteBike() {
            this.$store.commit('setIsLoading', true)

            await axios.delete('/api/v1/delete-bike/' + this.bikeIdtoDel)
                .then(response => {
                    console.log("Delete successful.")
                    this.notify();
                })
                .catch(error => {
                    console.log(error)
                })
            this.showModal = false;
            this.$store.commit('setIsLoading', false)
        },
        changeBikeIdToDelete(id) {
            this.bikeIdtoDel = id;
            console.log(this.bikeIdtoDel);
            this.showModal = true;
        }

    }
}
</script>

<style scoped>
#cancelButton {
    margin-right: 20px;
    float: right;
}

#deleteButton {
    float: right;
}
</style>