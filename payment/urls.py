from django.urls import path

from payment.apps import PaymentConfig
from payment.views import PaymentCreateAPIView, PaymentListAPIView, PaymentRetrieveAPIView

app_name = PaymentConfig.name

urlpatterns = [
    path('create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('', PaymentListAPIView.as_view(), name='payment_list'),
    path('<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_retrieve')
]
