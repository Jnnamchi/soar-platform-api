#!/usr/bin/env python3
import stripe
import os
stripe.api_key = os.environ.get('STRIPE_API_KEY')

l = stripe.WebhookEndpoint.list(limit=30)

print(l)