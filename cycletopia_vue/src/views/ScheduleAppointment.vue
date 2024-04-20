<template>
    <div>
        <div class="row g-3 shadow p-3 mb-5 bg-body rounded">
            <div class="col-md-6 d-none d-md-block position-relative">
                <img src="@/assets/cyclists.jpg" class="img-fluid rounded shadow-lg" style="height:100%;" />

            </div>

            <div class="col-md-6">
                <h2>Request Training</h2>
                <p style="margin-top: 15px;">Please fill the following form to book a training session. The session will take place in our training center in Beirut. Payment will be made on-site.</p>

                <br>
                <div class="row">
                    <div class="form-floating col-md-6 my-2">
                        <input type="email" class="form-control" v-model="email" placeholder="Email">
                        <label class="form-label p-3">Email</label>
                    </div>
                    <div class="form-floating col-md-6 my-2">
                        <input type="number" class="form-control" v-model="phone" placeholder="Phone">
                        <label class="form-label p-3">Phone</label>
                    </div>
                    <div class="form-floating col-md-4 my-2">
                        <input type="date" class="form-control" v-model="date" placeholder="Date"
                            v-on:change="changeDateSelected()" id="myDate" min="" max="">
                        <label class="form-label p-3">Date</label>
                    </div>
                    <div class="form-floating col-md-4 my-2">
                        <select class="form-select" v-model="time" id="time-select"></select>
                        <label class="form-label p-3">Time</label>
                    </div>
                    <div class="form-floating col-md-4 my-2">
                        <select class="form-select" v-model="bike_type">
                            <option>Road</option>
                            <option>Mountain</option>
                            <option>Electric</option>

                        </select>
                        <label class="form-label p-3">Bike type (select one):</label>
                    </div>
                </div>

                <div class="d-grid gap-2 col-md-6 mx-auto">
                    <button style="margin-top: 20px;" class="btn btn-dark" @click="submitData">Submit</button>

                </div>

            </div>
        </div>
        <div class="alert alert-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    name: 'ScheduleAppointment',

    data() {
        return {
            email: '',
            phone: '',
            bike_type: '',
            time: '',
            date: '',
            availableTimes: [],
            errors: []
        };
    },
    mounted() {
        document.title = 'Request Training | Cycletopia'

        const today = new Date().toISOString().split('T')[0];
        const tomorrow = new Date(new Date(today).setDate(new Date(today).getDate() + 1)).toISOString().split('T')[0];
        const maxDate = new Date(new Date(today).setDate(new Date(today).getDate() + 7)).toISOString().split('T')[0];

        document.getElementById("myDate").setAttribute("min", tomorrow);
        document.getElementById("myDate").setAttribute("max", maxDate);

    },

    methods: {
        submitData() {
            this.errors = []
            if (this.email === '') {
                this.errors.push('The email field is missing!')
            }
            if (this.phone === '') {
                this.errors.push('The phone field is missing!')
            }
            if (this.bike_type === '') {
                this.errors.push('The bike type field is missing!')
            }
            if (this.time === '') {
                this.errors.push('The time field is missing!')
            }
            if (this.date === '') {
                this.errors.push('The date field is missing!')
            }
            if (!this.errors.length) {
                const formData = {
                    email: this.email,
                    phone: this.phone,
                    bike_type: this.bike_type,
                    date: this.date,
                    time: this.time,
                }
                console.log(formData)
                axios
                    .post("/api/v1/make-appointment/", formData)
                    .then(response => {
                        this.$router.push('/request-training/success');

                    }).catch(error => {
                        console.log(error)
                    })
            }
        },
        async getAvailableTimes() {
            this.availableTimes = [];
            const selectElement = document.getElementById('time-select');
            selectElement.innerHTML = '';
            await axios.get('/api/v1/get-times/' + this.date + '/')
                .then(response => {
                    this.availableTimes = response.data.available_times
                    for (const time of this.availableTimes) {
                        const optionElement = document.createElement('option');
                        optionElement.value = time;
                        optionElement.text = time;
                        selectElement.appendChild(optionElement);
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        },
        changeDateSelected() {
            this.availableTimes = [];
            const dateObj = new Date(this.date);
            const year = dateObj.getFullYear();
            const month = ('0' + (dateObj.getMonth() + 1)).slice(-2);
            const day = ('0' + dateObj.getDate()).slice(-2);
            const formattedDate = `${year}-${month}-${day}`;
            this.date = formattedDate
            this.time = ''
            this.getAvailableTimes()
        }

    },
};
</script>

<style scoped></style>
  