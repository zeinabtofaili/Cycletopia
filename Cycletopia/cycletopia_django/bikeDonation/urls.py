from django.urls import path, include

from bikeDonation import views

urlpatterns = [
    path('donate-bike/', views.donateBike),
    path('current-user-donated-bikes/', views.UserSpecificDonatedBike.as_view()),
    path('all-donated-bikes/', views.AllDonatedBikes.as_view()),
]