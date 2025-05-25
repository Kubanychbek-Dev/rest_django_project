from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import User
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer, UserTokenObtainPairSerializer


class UserListAPIView(ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserCreateAPIView(CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserCreateSerializer
  permission_classes = (AllowAny,)


class UserRetrieveAPIView(RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = (AllowAny,)


class UserUpdateAPIView(UpdateAPIView):
  queryset = User.objects.all()
  serializer_class = UserUpdateSerializer
  permission_classes = (AllowAny,)


class UserDestroyAPIView(DestroyAPIView):
  queryset = User.objects.all()
  permission_classes = (AllowAny,)


class UserTokenObtainPairView(TokenObtainPairView):
  serializer_class = UserTokenObtainPairSerializer