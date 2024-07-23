from django.contrib import admin

from payment.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """ Админка для платежа """

    list_display = ('course', 'lesson', 'amount', 'method', 'user')
