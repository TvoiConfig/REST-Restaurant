
from dishes.views import DishesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('dishes', DishesViewSet, basename='dishes')

urlpatterns = [

]
urlpatterns += router.urls
