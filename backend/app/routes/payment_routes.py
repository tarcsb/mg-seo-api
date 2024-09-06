import stripe
from flask import Blueprint, request, jsonify, current_app
from app.models import db, User, Role

stripe.api_key = current_app.config['STRIPE_SECRET_KEY']

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    try:
        data = request.json
        plan = data.get('plan', 'basic')  # The plan could be 'basic', 'premium', or 'enterprise'
        
        # You can define pricing here based on plan
        amount = 1000 if plan == 'premium' else 2000

        # Create a PaymentIntent with the correct amount and currency
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            payment_method_types=['card'],
        )
        
        return jsonify({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@payments_bp.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')
    webhook_secret = current_app.config['STRIPE_WEBHOOK_SECRET']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
    except ValueError as e:
        return jsonify({'error': 'Invalid payload'}), 400
    except stripe.error.SignatureVerificationError as e:
        return jsonify({'error': 'Invalid signature'}), 400

    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        handle_payment_intent_succeeded(payment_intent)

    return jsonify({'status': 'success'})

def handle_payment_intent_succeeded(payment_intent):
    # Here, mark the user as upgraded in the database
    user_id = payment_intent['metadata']['user_id']
    user = User.query.get(user_id)
    
    if user:
        # Update the user's subscription or role here
        premium_role = Role.query.filter_by(name='Premium').first()
        user.role = premium_role
        db.session.commit()
