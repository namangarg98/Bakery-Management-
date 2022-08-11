from datetime import datetime, date

from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count

from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets

from .models import *
from .serializers import *


class IngredientAPIModelViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = [IsAdminUser]


class DishAPIModelViewSet(viewsets.ModelViewSet):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()
    permission_classes = [IsAdminUser]


class CustomerDishAPIModelViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerDishSerializer
    queryset = Dish.objects.all()
    permission_classes = [IsAuthenticated]


class OrderAPIModelViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
