<template>
    <div class="container py-5">
        <div class="row">
            <div class="col-md-6">
                <img src="@/assets/bicycle2.jpg" class="img-fluid rounded">
            </div>
            <div class="col-md-6" style="display: flex; align-items: center;">
                <div class="card border-0 bg-transparent text-center">
                    <div class="card-body">
                        <h1 class="mb-4 text-center">We Are Here For You</h1>
                        <h3 class="mb-4 text-center"> Contact Us</h3>
                        <h6 class="mb-4 text-center">We can help. Our team of experts is on hand to answer your questions.
                        </h6>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="row">
        <div class="col-sm-6 mb-4">
            <div class="card shadow p-3 mb-5 rounded">
                <div class="card-body" style="display: flex; flex-direction: row;">
                    <div
                        style="display: flex; align-items: center; justify-content: center; width: 40%; margin-right: 10px;">
                        <i class="fa-solid fa-envelope fa-bounce fa-2xl"></i>
                    </div>
                    <div>
                        <h5 class="card-title">Email us</h5>
                        <p class="card-text">Send an email to contact-us@cycletopia.com and we will get in touch with you.
                        </p>
                    </div>

                </div>
            </div>
        </div>
        <div class="col-sm-6 mb-4">
            <div class="card shadow p-3 mb-5 rounded">
                <div class="card-body" style="display: flex; flex-direction: row;">
                    <div style="display: flex; align-items: center; justify-content: center; width: 40%;">
                        <i class="fa-solid fa-phone-volume fa-shake fa-2xl"></i>
                    </div>
                    <div>
                        <h5 class="card-title">Call us</h5>
                        <p class="card-text">Give us a ring at 01 234 432 to speak with an agent immediately.</p>
                    </div>

                </div>
            </div>
        </div>
    </div>
    <div class="card text-center shadow p-3 mb-5 rounded">
        <div class="card-body row">
            <div class="col-md-6">
                <img src="@/assets/contactUs.png" class="img-fluid rounded">
            </div>
            <div class="col-md-6" style="display: flex; align-items: center;">
                <div class="card border-0 bg-transparent text-center">
                    <div class="card-body">
                        <h1 class="mb-4 text-center">Follow us on social media!</h1>
                        <div>
                            <a class="btn btn-primary shadow mb-5 rounded" style="background-color: #3b5998; margin-right: 20px;" href="#" role="button"><i
                                    class="fab fa-facebook-f" style="margin-right: 5px;"></i> Facebook</a>
                            <a class="btn btn-primary shadow mb-5 rounded" style="background-color: #ac2bac;" href="#" role="button"><i
                                    class="fab fa-instagram" style="margin-right: 5px;"></i>Instagram</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ContactUsView',
    mounted() {
        document.title = 'Contact Us | Cycletopia'
    },
}
</script>

<style scoped></style>