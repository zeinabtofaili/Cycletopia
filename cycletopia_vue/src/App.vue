<template>
  <div id="wrapper">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand mb-0 h1" href="/" style="margin-left: 10px;">Cycletopia</a>
        <button class="navbar-toggler" type="button" :class="visible ? null : 'collapsed'" data-bs-toggle="collapse"
          data-bs-target="#navContent" aria-controls="navContent" :aria-expanded="visible ? 'true' : 'false'"
          @click="visible = !visible" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse flex-grow-1 text-right" id="navContent">
          <div class="col-xs-3" style="margin-left:5px; margin-right:5px;">
            <form class="form-inline my-2 my-lg-0 input-group" method="get" action="/search">
              <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search" name="query">
              <button class="btn btn-success" ><span class="icon">
                  <i class="fas fa-search"></i>
                </span></button>
            </form>
          </div>
          <div class="ms-auto flex-nowrap">

            <ul class="navbar-nav">
              <li class="nav-item active">
                <router-link to="/bikes" class="nav-link" style="margin-left:5px;">Bike Store</router-link>
              </li>
              <li class="nav-item active">
                <router-link to="/clothes" class="nav-link" style="margin-left:5px;">Clothes Store</router-link>
              </li>
              <li class="nav-item">
                <router-link to="/components" class="nav-link" style="margin-left:5px;">Bike
                  Components</router-link>
              </li>
              <li class="nav-item dropdown">
                <div class="nav-link dropdown-toggle" id="navbarDropdown" role="button" data-bs-toggle="dropdown"
                  aria-haspopup="true" aria-expanded="false" style="margin-left:5px;">
                  More
                </div>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown" style="margin-left:5px;">
                  <a class="dropdown-item" href="/cycling-events">Cycling events</a>
                  <a class="dropdown-item" href="/cycling-places">Cycling places</a>
                  <div class="dropdown-divider"></div>
                  <a class="dropdown-item" href="/donate-bike">Donate your bike</a>
                  <a class="dropdown-item" href="/sell-bike">Sell your bike</a>
                  <a class="dropdown-item" href="/buy-user-bike">Buy a user bike</a>
                  <a class="dropdown-item" href="/rent-bike">Rent a bike</a>
                  <div class="dropdown-divider"></div>
                  <a class="dropdown-item" href="/request-training">Request training</a>

                </div>
              </li>
              <router-link v-if="$store.state.isAuthenticated" to="/my-account" class="btn btn-light my-sm-0 my-2" style="margin-left:5px;">
                <span class="icon"><i style="margin-right:3px;" class="fa fa-user"></i></span>
                <span>My Account</span>
              </router-link>
              <router-link v-else to="/log-in" class="btn btn-light my-sm-0 my-2" style="margin-left:5px;">
                <span class="icon"><i style="margin-right:3px;" class="fa fa-sign-in"></i></span>
                <span>Login</span>
              </router-link>

              <router-link to="/cart" class="btn btn-success my-sm-0 my-2" style="margin-left:5px;">
                <span class="icon"><i style="margin-right:3px;" class="fas fa-shopping-cart"></i></span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link>
            </ul>
          </div>
        </div>
      </div>
    </nav>

    <div class="d-flex justify-content-center m-5" v-if="$store.state.isLoading">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
    <section class="container">
      <router-view />
    </section>

    <footer class="text-center text-lg-start bg-light text-muted">
      <section class="d-flex justify-content-center justify-content-lg-between p-4 border-bottom">
        <div class="me-5 d-none d-lg-block">
          <span>Get connected with us on social networks:</span>
        </div>

        <div>
          <a href="" class="me-4 text-reset">
            <i class="fab fa-facebook-f"></i>
          </a>
          <a href="" class="me-4 text-reset">
            <i class="fab fa-instagram"></i>
          </a>
        </div>
      </section>

      <section>
        <div class="container text-center text-md-start mt-5">
          <div class="row mt-3">
            <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
              <h6 class="text-uppercase fw-bold mb-4">
                <i class="fa-solid fa-bicycle" style="margin-right: 3px;"></i>Cycletopia
              </h6>
              <p>
                Zero emissions, Zero excuses
              </p>
            </div>

            <div class="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4">
              <h6 class="text-uppercase fw-bold mb-4">
                Useful links
              </h6>
              <p>
                <a href="/about" class="text-reset">About</a>
              </p>
              <p>
                <a href="/contact-us" class="text-reset">Contact</a>
              </p>

            </div>
          </div>
        </div>
      </section>

      <div class="text-center p-4" style="background-color: rgba(0, 0, 0, 0.05);">
        Copyright 2023 ©
        <a class="text-reset fw-bold" href="/">Cycletopia</a>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue';
const visible = ref(false);
</script>
<script>
import axios from 'axios'

export default {
  data() {
    return {
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0
      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }
      return totalLength;
    }
  }
}
</script>

<style lang="scss">
.container {
  margin-top: 4%;
  margin-bottom: 4%;
}

.flexbox {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

.flex-item {
  margin-right: calc(1.5rem * 0.5);
  margin-left: calc(1.5rem * 0.5);
  margin-top: 1.5rem;
}

</style>
