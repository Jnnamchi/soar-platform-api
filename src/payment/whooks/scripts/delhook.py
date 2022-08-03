#!/usr/bin/env python3
import stripe
import os
stripe.api_key = os.environ.get('STRIPE_API_KEY')

stripe.WebhookEndpoint.delete(
  "we_1LJ6l2BNlIemTroOhaSLvXQJ",
)

