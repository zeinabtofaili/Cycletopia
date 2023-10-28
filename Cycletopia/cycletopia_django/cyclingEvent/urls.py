from django.urls import path, include

from cyclingEvent import views

urlpatterns = [
    path('cycling-events/', views.CyclingEventsList.as_view()),
    path('cycling-events/<slug:event_slug>/', views.EventDetail.as_view()),
    path('register-in-event/', views.registerInEvent)
]