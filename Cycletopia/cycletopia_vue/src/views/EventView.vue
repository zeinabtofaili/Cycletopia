<template>
    <div class="container">
        <!-- Pills navs -->
        <ul class="nav nav-pills mb-3" role="tablist">
            <li class="nav-item">
                <a class="nav-link active" id="tab-1" data-toggle="pill" href="#specifications" role="tab"
                    aria-controls="specifications"> <i class="fa-solid fa-info-circle" style="margin-right: 4px;"></i>Event
                    Details</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" id="tab-2" data-toggle="pill" href="#location" role="tab" aria-controls="location"><i
                        class="fas fa-map-marker-alt" style="margin-right: 4px;"></i>Location</a>
            </li>
            
        </ul>
        <!-- Pills navs -->

        <!-- Pills content -->
        <div class="tab-content">
            <div class="tab-pane fade show active" id="specifications" role="tabpanel" aria-labelledby="tab-1">
                <div class="col-md card p-3 ml-4 mb-5 bg-body rounded">
                    <div class="row">
                        <div class="col-md-6">
                            <div class="images p-3">
                                <div class="text-center p-4"> <img v-bind:src="event.get_image" id="event-image" />
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="product p-4">
                                <div class="mt-4 mb-3">
                                    <h5 class="text-uppercase">{{ event.name }}</h5>
                                </div>
                            </div>
                            <p class="about">{{ event.description }}</p>
                            <div class="product">
                                <div class="mt-4 mb-3">
                                    <h6 class="text-uppercase">When?</h6>
                                    <p>{{ event.date_and_time }}</p>
                                </div>
                            </div>
                            <div class="product">
                                <div class="mt-4 mb-3">
                                    <button class="btn btn-dark text-uppercase mr-2 px-4" @click="submitForm">Register</button>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="alert alert-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
            </div>
            <div class="tab-pane fade" id="location" role="tabpanel" aria-labelledby="tab-2">
                <div
                    class="col-md card p-3 ml-4 mb-5 bg-body rounded d-flex align-items-center flex-column justify-content-center">
                    <div class="d-flex justify-content-center text-center" style="width: 100%;">
                        <h4>Location on map:</h4>
                    </div>
                    <div class="d-flex align-items-center" style="margin-top:2%; width: 100%;">
                        <div class="d-flex justify-content-center" style="width: 100%;">
                            <iframe v-bind:src="event.map_url" width="80%" height="350" allowfullscreen
                                loading="lazy"></iframe>
                        </div>
                    </div>
                </div>
                
            </div>

        </div>
        <!-- Pills content -->
    </div>

    <Modal v-model="showModal" title="Register Successful">
        <h5>You have been registered successfully!</h5>
        <br />
        <div>
            <button class="btn btn-success" id="DismissButton" @click="showModal = false">Dismiss</button>
        </div>
        <br />
        <br />
    </Modal>
</template>

<script>
import axios from 'axios'
import VueModal from '@kouts/vue-modal'
import '@kouts/vue-modal/dist/vue-modal.css'

export default {
    name: 'EventView',
    data() {
        return {
            event: {},
            errors: [],
            showModal: false,
        }
    },
    components: {
        'Modal': VueModal
    },
    mounted() {
        this.getEvent();
        const pillsLinks = document.querySelectorAll(".nav-link");
        const pillsContent = document.querySelectorAll(".tab-pane");

        pillsLinks.forEach(link => {
            link.addEventListener("click", e => {
                e.preventDefault();
                pillsLinks.forEach(link => link.classList.remove("active"));
                link.classList.add("active");
                const tabContent = document.getElementById(link.getAttribute("href").slice(1));
                pillsContent.forEach(content => content.classList.remove("show", "active"));
                tabContent.classList.add("show", "active");
            });
        });
    },
    methods: {
        async getEvent() {
            this.$store.commit('setIsLoading', true)
            const event_slug = this.$route.params.event_slug
            await axios
                .get(`/api/v1/cycling-events/${event_slug}`)
                .then(response => {
                    this.event = response.data
                    document.title = this.event.name + ' | Cycletopia'
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)

        },
        async submitForm(){
            const data = {
                'name': this.event.name,
                'attendees': this.event.attendees,
            }
            await axios
                .patch('/api/v1/register-in-event/', data)
                .then(response => {
                    this.showModal = true;

                    console.log("Register success!")
                    // this.$router.push('/rent-bike/${bike_slug}/success')
                })
                .catch(error => {
                    if(error.response.data == "User Already Registered!"){
                        this.errors.push('User Already Registered!')
                    }
                    else{
                        this.errors.push('Something went wrong. Please try again')
                    }
                }) 
        }
    }

}

</script>
<style scoped>
@media (min-width: 768px) {
    #mapBox {
        margin-left: 1.5rem !important;
    }
}

.nav-item {
    margin-right: 2%;
}

.nav-pills .nav-link.active {
    color: #285192;
    background-color: #e3ebf7;
}

#event-image {
    width: 100%;
}

.nav-link {
    color: grey;
}

#DismissButton {
    float: right;
}
</style>