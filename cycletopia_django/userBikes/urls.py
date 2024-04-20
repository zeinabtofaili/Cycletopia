from django.urls import path, include

from userBikes import views

urlpatterns = [
    path('sell-bike/', views.sellBike),
    path('current-user-bikes/', views.UserSpecificBike.as_view()),
    path('all-user-bikes/', views.AllBikes.as_view()),  
    path('user-bike/<slug:product_slug>/', views.BikeDetail.as_view()),
    path('delete-bike/<int:bike_id>/', views.delete_bike),

]