import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProductView from '../views/ProductView.vue'
import CategoryView from '../views/CategoryDetail.vue'
import SearchView from '../views/SearchView.vue'
import CartView from '../views/CartView.vue'
import MyAccountView from '../views/MyAccountView.vue'
import SignupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import store from '../store'
import CyclingPlacesView from '../views/CyclingPlacesView.vue'
import CheckoutView from '../views/CheckoutView.vue'
import SuccessView from '../views/SuccessView.vue'
import PlaceView from '../views/PlaceView.vue'
import RentalBikesView from '../views/RentalBikesView.vue'
import RentalBikeDetail from '../views/RentalBikeDetail.vue'
import RentSuccessView from '../views/RentSuccessView.vue'
import SellBikeUser from '../views/SellBikeUser.vue'
import UploadBikeSuccessView from '../views/uploadBikeSuccess.vue'
import AllUserBikesView from '../views/UserBikesView.vue'
import UserBikeDetail from '../views/UserBikeDetail.vue'
import DonateBikeUser from '../views/DonateBikeView.vue'
import DonateBikeSuccessView from '../views/DonateBikeSuccess.vue'
import ContactUsView from '../views/ContactUsView.vue'
import ScheduleAppointment from '../views/ScheduleAppointment.vue'
import ScheduleAppointmentSuccessView from '../views/ScheduleAppointmentSuccess.vue'
import CyclingEventsView from '../views/CyclingEventsView.vue'
import EventView from '../views/EventView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/contact-us',
    name: 'contact',
    component: ContactUsView
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'Product',
    component: ProductView
  },
  {
    path: '/:category_slug',
    name: 'Category',
    component: CategoryView
  },
  {
    path: '/user-bike/:bike_slug',
    name: 'UserBikeDetail',
    component: UserBikeDetail
  },
  {
    path: '/buy-user-bike',
    name: 'UserBikesView',
    component: AllUserBikesView
  },
  {
    path: '/search',
    name: 'Search',
    component: SearchView
  },
  {
    path: '/cart',
    name: 'Cart',
    component: CartView
  },
  {
    path: '/cycling-places',
    name: 'CyclingPlaces',
    component: CyclingPlacesView
  },
  {
    path: '/cycling-events',
    name: 'CyclingEvents',
    component: CyclingEventsView
  },
  {
    path: '/rent-bike',
    name: 'RentalBikes',
    component: RentalBikesView
  },
  {
    path: '/cycling-places/:place_slug',
    name: 'Place',
    component: PlaceView
  },
  {
    path: '/cycling-events/:event_slug',
    name: 'Event',
    component: EventView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/rent-bike/:bike_slug',
    name: 'BikeRent',
    component: RentalBikeDetail,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/sell-bike',
    name: 'SellBike',
    component: SellBikeUser,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/donate-bike',
    name: 'DonateBike',
    component: DonateBikeUser,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/cart/success',
    name: 'SuccessCart',
    component: SuccessView
  },
  {
    path: '/sell-bike/success',
    name: 'Success',
    component: UploadBikeSuccessView
  },
  {
    path: '/donate-bike/success',
    name: 'DonationSuccess',
    component: DonateBikeSuccessView
  },
  {
    path: '/rent-bike/:bike_slug/success',
    name: 'RentSuccess',
    component: RentSuccessView
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignupView
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LoginView
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccountView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: CheckoutView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/request-training',
    name: 'ScheduleAppointment',
    component: ScheduleAppointment,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/request-training/success',
    name: 'ScheduleAppointmentSuccessView',
    component: ScheduleAppointmentSuccessView
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    // always scroll to top
    return { top: 0 }
  },
})
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
