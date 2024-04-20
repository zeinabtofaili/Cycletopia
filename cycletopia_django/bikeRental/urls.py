from django.urls import path, include

from bikeRental import views

urlpatterns = [
    path('rent-bike/', views.RentalBikesList.as_view()),
    path('rent-bike/<slug:bike_slug>/', views.BikeDetail.as_view()),
    path('rent/', views.rentBike),
]