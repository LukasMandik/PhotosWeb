# payments.py
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_payment_intent(amount, currency):
    return stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        payment_method_types=['card'],
    )


def confirm_payment_intent(payment_intent_id):
    return stripe.PaymentIntent.confirm(payment_intent_id)


def cancel_payment_intent(payment_intent_id):
    return stripe.PaymentIntent.cancel(payment_intent_id)
