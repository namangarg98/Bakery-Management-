from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('register', RegisterAPIModelViewSet,
                basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginAPI.as_view()),
    path('logout/', user_logout),

]
