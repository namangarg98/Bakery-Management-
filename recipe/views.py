from datetime import datetime, date

from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count

from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets

from .models import *
from .serializers import *


@api_view(['GET'])
def api_overview(request):
    IngredientDict = {
        'To get list of Ingrdients  REQUEST-TYPE = GET              ':                '/recipe/ingredientsapi/',
        'Adding an Ingredient  REQUEST-TYPE = POST                  ':                '/recipe/ingredientsapi/',
        'Detail of single Ingrdient  REQUEST-TYPE = GET             ':                '/recipe/ingredientsapi/<int:id>/',
        'Deleting an Ingredient  REQUEST-TYPE = DELETE              ':                '/recipe/ingredientsapi/<int:id>/',
    }
    MenuDict = {
        'To get list of DISHES  REQUEST-TYPE = GET                  ':                '/recipe/dishesapi/',
        'Adding a DISH  REQUEST-TYPE = POST                         ':                '/recipe/dishesapi/',
        'Detail of single DISH  REQUEST-TYPE = GET                  ':                '/recipe/dishesapi/<int:id>/',
        'Deleting a DISH  REQUEST-TYPE = DELETE                     ':                '/recipe/dishesapi/<int:id>/',
    }
    OrderDict = {
        'To get list of ORDERS  REQUEST-TYPE = GET                  ':                '/recipe/orderapi/',
        'Adding an ORDER  REQUEST-TYPE = POST                       ':                '/recipe/orderapi/',
        'Detail of single ORDER  REQUEST-TYPE = GET                 ':                '/recipe/orderapi/<int:id>/',
        'Deleting an ORDER  REQUEST-TYPE = DELETE                   ':                '/recipe/orderapi/<int:id>/',
        'To get ORDER History of single USER REQUEST-TYPE = GET     ':                '/recipe/customerdishapi',
    }

    url_list = {

        'ADMIN PANEL                                                    ':                 '/admin/',
        'REGISTER                                                       ':                 '/accounts/regsiter/',
        'LOGIN                                                          ':                 '/accounts/login/',
        'ENDPOINTS FOR INGREDIENT                                       ':                 IngredientDict,
        'ENDPOINTS FOR MENU                                             ':                 MenuDict,
        'ENDPOINTS FOR ORDERS                                           ':                 OrderDict,

    }
    return Response(url_list)


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
