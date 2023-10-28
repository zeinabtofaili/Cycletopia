from django.urls import path, include

from cyclingPlace import views

urlpatterns = [
    path('cycling-places/', views.CyclingPlacesList.as_view()),
    path('cycling-places/<slug:place_slug>/', views.PlaceDetail.as_view()),
]