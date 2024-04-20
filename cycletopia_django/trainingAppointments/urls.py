from django.urls import path, include

from trainingAppointments import views

urlpatterns = [
    path('make-appointment/', views.makeAppointment),
    path('get-times/<str:date>/', views.GetTimesInADate.as_view()),
]