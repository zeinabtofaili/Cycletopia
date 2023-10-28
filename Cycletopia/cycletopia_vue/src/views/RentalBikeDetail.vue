<template>
    <ul class="nav nav-pills mb-3" role="tablist">
        <li class="nav-item">
            <a class="nav-link active" id="tab-1" data-toggle="pill" href="#specifications" role="tab"
                aria-controls="specifications"> <i class="fa-solid fa-gear"></i> Bike Specifications</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" id="tab-2" data-toggle="pill" href="#location" role="tab" aria-controls="location"><i
                    class="fas fa-map-marker-alt" style="margin-right: 4px;"></i>Location</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" id="tab-3" data-toggle="pill" href="#rent" role="tab" aria-controls="rent"><i
                    class="fas fa-money-check-alt" style="margin-right: 4px;"></i>Rent Bike</a>
        </li>

    </ul>

    <div class="tab-content">
        <div class="tab-pane fade show active" id="specifications" role="tabpanel" aria-labelledby="tab-1">
            <div class="col-md card p-3 ml-4 mb-5 bg-body rounded">
                <div class="row">
                    <div class="col-md-6">
                        <div class="images p-3">
                            <div class="text-center p-4"> <img v-bind:src="product.get_image" id="product-image" />
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="product p-4">
                            
                            <div class="mt-4 mb-3">
                                <h5 class="text-uppercase">{{ product.name }}</h5>

                            </div>
                            <p class="about">{{ product.description }}
                            </p>
                            <div class="sizes mt-5">
                                <h6 class="text-uppercase">Size: {{ product.size }}</h6>
                            </div>
                            <div class="sizes mt-5">
                                <h6 class="text-uppercase" v-if="product.grouping !== null">Category: {{
                                    product.grouping
                                }}</h6>
                            </div>
                            <div class="sizes mt-5">
                                <h6 class="text-uppercase" v-if="product.color !== null">Color: <i
                                        class="fa-solid fa-circle fa-border" id="circle"></i> {{
                                            product.color
                                        }}</h6>
                            </div>

                        </div>
                    </div>
                </div>

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
                        <iframe v-bind:src="product.map_url" width="80%" height="350" allowfullscreen
                            loading="lazy"></iframe>
                    </div>
                </div>
            </div>
        </div>
        <div class="tab-pane fade" id="rent" role="tabpanel" aria-labelledby="tab-3">
            <div
                class="col-md card p-3 ml-4 mb-5 bg-body rounded d-flex align-items-center flex-column justify-content-center">
                <div class="d-flex justify-content-center text-center" style="width: 100%;">
                    <h5>Choose plan:</h5>
                </div>

                <div class="price d-flex flex-row align-items-center">
                    <section class="pricing py-3" style="width: 100%;">
                        <div class="container d-flex align-items-center justify-content-center ">
                            <div class="row" v-for="entry in pricing" style="margin-left: 2.5px;margin-right:2.5px;">
                                <div>
                                    <div class="card mb-5 mb-lg-0">
                                        <div class="card-body">
                                            <h5 class="card-title text-muted text-uppercase text-center">
                                                {{ entry.duration }}</h5>
                                            <h6 class="card-price text-center">${{ entry.price }}</h6>
                                            <hr>

                                            <div class="d-grid">
                                                <button class="btn btn-primary text-uppercase plan"
                                                    @click="setPriceAndDuration(entry.price, entry.duration), changetextAndBackground($event)">Choose
                                                    plan</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                            </div>
                        </div>
                    </section>
                </div>

                <p class="text-secondary mb-4">* All fields are required</p>

                <div class="row g-3">

                    <div class="col-md-6">
                        <label class="form-label">Email address*</label>
                        <input type="email" class="form-control" v-model="renter_email">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">Valid ID number*</label>
                        <input type="text" class="form-control" v-model="renter_id">
                    </div>
                    <p class="text-secondary mt-4 mb-4">You will need to show your ID when you take the bike.</p>

                    <div class="alert alert-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
                    <hr>

                    <div id="card-element" class="mb-2"></div>
                    <hr>
                </div>


                <div class="cart mt-4 align-items-center">
                    <div class="input-group mb-3">
                        <button class="btn btn-dark text-uppercase mr-2 px-4" @click="submitForm">Rent bike</button>

                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'BikeRentalDetail',
    data() {
        return {
            product: {},
            pricing: [],
            amount_paid: 0,
            return_date: new Date(),
            rented_date: new Date(),
            renter_id: "",
            renter_email: "",
            stripe: {},
            card: {},
            errors: [],
        }
    },

    mounted() {
        this.getProduct();
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
        this.stripe = Stripe('pk_test_51MOe4BG04ADJG9CuiGwsIqQTORFw3OIZ1OX2H75ZhemEQ0SqcoxDE76D4L2E9oWmsOIdtOI1GR8QXwBMzMN0uIWP00BhTqeZr4')
        const elements = this.stripe.elements();
        this.card = elements.create('card', { hidePostalCode: true })

        this.card.mount('#card-element')
    },
    methods: {
        changetextAndBackground(event) {
            var plans = document.getElementsByClassName("plan");
            for (var i = 0; i < plans.length; i++) {
                plans[i].innerHTML = "Choose plan";
                if (!plans[i].classList.contains("btn-primary")) {
                    plans[i].classList.add("btn-primary");
                }
                if (plans[i].classList.contains("btn-success")) {
                    plans[i].classList.remove("btn-success");
                }
            }
            event.target.innerHTML = "Selected";

            event.target.classList.remove("btn-primary");
            event.target.classList.add("btn-success")
        },
        setPriceAndDuration(price, duration) {
            this.amount_paid = price;
            this.rented_date = new Date();
            if (duration == "One month") {
                this.return_date = new Date();
                this.return_date = new Date(this.return_date.getFullYear(), this.return_date.getMonth() + 1, this.return_date.getDate());
            } else if (duration == "One year") {
                this.return_date = new Date();
                this.return_date.setFullYear(this.rented_date.getFullYear() + 1);
            } else if (duration == "One week") {
                this.return_date = new Date();
                this.return_date.setDate(this.return_date.getDate() + 7);
            }
        },
        async getProduct() {
            this.$store.commit('setIsLoading', true)

            const bike_slug = this.$route.params.bike_slug

            await axios
                .get(`/api/v1/rent-bike/${bike_slug}`)
                .then(response => {
                    this.product = response.data
                    document.title = this.product.name + ' | Cycletopia'

                    let pricing = this.product.rent_duration_and_price;
                    let entries = Object.entries(JSON.parse(pricing));
                    let transformed = entries.map(([duration, price]) => ({ duration, price }));
                    this.pricing = transformed
                    if (this.product.color != null) {
                        document.getElementById('circle').style.color = this.product.color;
                        if (document.getElementById('circle').style.color.toLowerCase() != this.product.color.toLowerCase()) {
                            document.getElementById('circle').style.display = 'none';
                        }
                    }
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
        submitForm() {
            this.errors = []
            if (this.renter_email === '') {
                this.errors.push('The email field is missing!')
            }
            if (this.renter_id === '') {
                this.errors.push('The ID field is missing!')
            }
            if (this.amount_paid === 0) {
                this.errors.push('Please choose a plan before proceeding!')
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
            const data = {
                'renter_email': this.renter_email,
                'renter_id': this.renter_id,
                'amount_paid': this.amount_paid,
                'stripe_token': token.id,
                'return_date': this.return_date.toISOString().substring(0, 10),
                'rented_date': this.rented_date.toISOString().substring(0, 10),
                'name': this.product.name,
                'rent_duration_and_price': this.product.rent_duration_and_price,
            }
            await axios
                .patch('/api/v1/rent/', data)
                .then(response => {
                    console.log("bike rental success!")
                    this.$router.push('/rent-bike/${bike_slug}/success')
                })
                .catch(error => {
                    if(error.response.data == "Bike already rented!"){
                        this.errors.push('Bike already rented!')
                    }
                    else{
                        this.errors.push('Something went wrong. Please try again')
                    }
                })
            this.$store.commit('setIsLoading', false)
        }
    }
}

</script>
<style scoped>
.nav-item {
    margin-right: 2%;
}

.nav-pills .nav-link.active {
    color: #285192;
    background-color: #e3ebf7;
}

#product-image {
    width: 100%;
}

.nav-link {
    color: grey;
}

.pricing .card {
    border: none;
    border-radius: 1rem;
    transition: all 0.2s;
    box-shadow: 0 0.5rem 1rem 0 rgba(0, 0, 0, 0.1);
}

.pricing hr {
    margin: 1.5rem 0;
}

.pricing .card-title {
    margin: 0.5rem 0;
    font-size: 0.8rem;
    letter-spacing: .1rem;
    font-weight: bold;
}

.pricing .card-price {
    font-size: 2rem;
    margin: 0;
}


.pricing ul li {
    margin-bottom: 0.5rem;
}

.pricing .text-muted {
    opacity: 0.7;
}

.pricing .btn {
    font-size: 80%;
    border-radius: 5rem;
    letter-spacing: .1rem;
    font-weight: bold;
    padding: 0.5rem;
    opacity: 0.7;
    transition: all 0.2s;
}

/* Hover Effects on Card */

@media (min-width: 992px) {
    .pricing .card:hover {
        margin-top: -.25rem;
        margin-bottom: .25rem;
        box-shadow: 0 0.5rem 1rem 0 rgba(0, 0, 0, 0.3);
    }

    .pricing .card:hover .btn {
        opacity: 1;
    }

    .container {
        flex-wrap: wrap;
    }
}

@media (max-width: 500px) {
    .container {
        flex-direction: column;
    }
}
</style>