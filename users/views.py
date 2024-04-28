from rest_framework import generics

from users.models import User
from users.serializers import UsersSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UsersSerializer


class UserListAPIView(generics.ListAPIView):
    serializer_class = UsersSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UsersSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UsersSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UsersSerializer
    queryset = User.objects.all()
