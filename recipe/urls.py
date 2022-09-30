from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('ingredientsapi', IngredientAPIModelViewSet,
                basename='ingredients')

router.register('customerdishapi', CustomerDishAPIModelViewSet,
                basename='ingredients')

router.register('dishesapi', DishAPIModelViewSet,
                basename='ingredients')

router.register('orderapi', OrderAPIModelViewSet,
                basename='ingredients')
urlpatterns = [
    path('', api_overview),
    path('', include(router.urls)),

]
