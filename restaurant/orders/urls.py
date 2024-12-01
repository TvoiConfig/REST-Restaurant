from django.urls import path
from orders.views import DishesView


urlpatterns = [
    path('dishes/', DishesView.as_view(), name='dishes'),
    path('dishes/<int:pk>/', DishesView.as_view(), name='dishes-detail'),
]

