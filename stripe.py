import stripe
import os

stripe.api_key = os.getenv("STRIPE_API_KEY")

# Create a new customer

# Create a new charge for $20
import stripe

stripe.api_key = 'your_api_key'

def create_customer(email, ssn, description):
    try:
        customer = stripe.Customer.create(
            email=email,
            description=description
            social_security_number=ssn
        )
        return customer
    except Exception as e:
        print("An error occurred: %s" % str(e))

# Usage
customer = create_customer("customer@example.com", "Example Customer", "222-04-9888")
print(customer)
