from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from payment.models import Payment
from payment.serializers import PaymentSerializer
from payment.services import create_price, create_session


class PaymentCreateAPIView(generics.CreateAPIView):
    """ Создание оплаты """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        course = serializer.validated_data.get('course')

        if not course:
            raise serializer.ValidationError('Поле "курс" обязательно для заполнения')

        user = self.request.user
        payment = serializer.save()
        payment.user = user

        if payment.method == 'card':
            email = user.email

            price = create_price(payment.amount)
            session = create_session(price, email)

            payment.session_id = session.get('id')
            payment.link = session.get('url')

            payment.save()


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    """ Чтение одной оплаты """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]


class PaymentListAPIView(generics.ListAPIView):
    """ Чтение всех оплат """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('course', 'lesson', 'method')
    ordering_fields = ('date',)
