from django.shortcuts import render
from user.serializers import CustomerRegister, UserLoginSerializer
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from .models import *
from rest_framework import mixins
# Create your views here.


# class CustomerRegisterAPI(generics.CreateAPIView):
#     serializer_class = CustomerRegister
#     permission_classes = (AllowAny,)

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(is_staff=False, is_active=True)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

class RegisterAPIModelViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = CustomerRegister
    queryset = Customer.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(is_staff=False, is_active=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPI(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print(request.user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_logout(request):
    auth.logout(request)
    data = {'success': 'Sucessfully logged out'}
    return Response(data=data, status=status.HTTP_200_OK)
