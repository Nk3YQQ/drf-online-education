import json
import stripe
from django.conf import settings
from django.core.mail import send_mail

from config.settings import PAYMENT_DATA_PATH


def convert_payment_to_data():
    with open(PAYMENT_DATA_PATH, 'r', encoding='utf-8') as data:
        return list({'pk': item['pk'], **item['fields']} for item in json.load(data))


def create_product(serializer):
    stripe.api_key = settings.API_KEY

    title = serializer.course.title if serializer.course else serializer.lesson.title

    return stripe.Product.create(
        name=title
    )


def create_price(amount):
    stripe.api_key = settings.API_KEY

    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        recurring={"interval": "month"},
        product_data={"name": "Subscription"},
    )


def create_session(price, email):
    stripe.api_key = settings.API_KEY

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="subscription",
        customer_email=email
    )

    send_mail(
        subject='Оплата продукта',
        message=f'Ссылка для оплаты приобретённого продукта: {session.get("url")}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )

    return session


def check_payment_status(session_id):
    stripe.api_key = settings.API_KEY
    session = stripe.checkout.Session.retrieve(session_id)
    return session.get("payment_status")
