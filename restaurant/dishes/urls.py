from django.urls import path
from dishes.views import DishesView


urlpatterns = [
    path('', DishesView.as_view(), name='dishes'),
    path('<int:pk>/', DishesView.as_view(), name='dishes-detail'),
]

