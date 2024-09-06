import stripe
from models import User, Subscription, db

stripe.api_key = 'your_stripe_secret_key'

# Create new Stripe customer
def create_stripe_customer(email):
    return stripe.Customer.create(email=email)

# Subscribe user to a plan
def subscribe_to_plan(user_id, plan_id):
    user = User.query.get(user_id)
    subscription = stripe.Subscription.create(
        customer=user.stripe_customer_id,
        items=[{'plan': plan_id}],
    )
    user.subscription_plan = plan_id
    db.session.commit()
    return subscription

# Handle plan upgrade/downgrade
def update_subscription(user_id, new_plan_id):
    user = User.query.get(user_id)
    current_subscription = stripe.Subscription.retrieve(user.subscription.stripe_subscription_id)
    stripe.Subscription.modify(
        current_subscription.id,
        cancel_at_period_end=False,
        items=[{'id': current_subscription['items']['data'][0].id, 'plan': new_plan_id}],
    )
    user.subscription_plan = new_plan_id
    db.session.commit()

# Cancel subscription
def cancel_subscription(user_id):
    user = User.query.get(user_id)
    stripe.Subscription.delete(user.subscription.stripe_subscription_id)
    user.subscription_plan = None
    db.session.commit()
