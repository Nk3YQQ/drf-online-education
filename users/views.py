from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from users.models import User, Payment
from users.serializers import UsersSerializer, PaymentSerializer


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


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'method')
    ordering_fields = ('date',)
