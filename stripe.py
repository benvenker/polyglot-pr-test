import stripe
import os

stripe.api_key = os.getenv("STRIPE_API_KEY")

# Create a new customer

# Create a new charge for $20


print(charge)
