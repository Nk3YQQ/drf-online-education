from rest_framework import serializers

from users.models import User, Payment
from users.services import check_payment_status


class UsersRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    passwordConfirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'passwordConfirm')

    def validate(self, attrs):
        password = attrs.get('password')
        passwordConfirm = attrs.get('passwordConfirm')

        if password != passwordConfirm:
            raise serializers.ValidationError('Пароли не совпадают')

        return attrs

    def create(self, validated_data):
        validated_data.pop('passwordConfirm')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'email',)


class PaymentSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = '__all__'

    @staticmethod
    def get_status(instance):
        session_id = instance.session_id
        if session_id:
            return check_payment_status(session_id)
