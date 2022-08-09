#!/usr/bin/env python3
import stripe
import os
stripe.api_key = os.environ.get('STRIPE_API_KEY')

endpoint = stripe.WebhookEndpoint.create(
  url='https://67bf-136-169-211-199.eu.ngrok.io/payment/webhook',
  # enabled_events=[
  #   'charge.failed',
  #   'charge.succeeded',
  # ],
  # enabled_events=[
  #   'checkout.session.completed',
  # ],
  enabled_events=[
    '*',
  ],
)

print(endpoint)
