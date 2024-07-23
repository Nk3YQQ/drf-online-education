from rest_framework import serializers

from payment.models import Payment
from payment.services import check_payment_status


class PaymentSerializer(serializers.ModelSerializer):
    """ Сериализатор для платежа """

    status = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = '__all__'

    @staticmethod
    def get_status(instance):
        session_id = instance.session_id
        if session_id:
            return check_payment_status(session_id)
