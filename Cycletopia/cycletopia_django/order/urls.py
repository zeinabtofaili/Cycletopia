from order import views
from django.urls import path

urlpatterns = [
    path('orders/', views.OrdersList.as_view()),  
    path('checkout/', views.checkout),
]