import stripe
import os

stripe.api_key = os.getenv("STRIPE_API_KEY")

# Create a new customer

# Create a new charge for $20
charge = stripe.Charge.create(
  amount=2000, # amount is in cents
  currency='usd',
  customer=customer.id,
  description='Example charge'
)

print(charge)
