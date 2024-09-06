from flask import Blueprint, url_for, session, redirect, jsonify
from authlib.integrations.flask_client import OAuth
from app.models import db, User

auth_bp = Blueprint('auth', __name__)
oauth = OAuth()

# Configure Google OAuth
google = oauth.register(
    name='google',
    client_id=app.config['OAUTH_CREDENTIALS']['google']['client_id'],
    client_secret=app.config['OAUTH_CREDENTIALS']['google']['client_secret'],
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri=url_for('auth.google_authorize', _external=True),
    client_kwargs={'scope': 'openid profile email'}
)

@auth_bp.route('/login')
def google_login():
    """Redirect to Google for authentication."""
    redirect_uri = url_for('auth.google_authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@auth_bp.route('/authorize')
def google_authorize():
    """Handle the response from Google and authenticate the user."""
    token = google.authorize_access_token()
    user_info = google.parse_id_token(token)
    
    # Check if the user exists in the database
    user = User.query.filter_by(email=user_info['email']).first()

    if user is None:
        # If the user doesn't exist, create a new one
        user = User(username=user_info['name'], email=user_info['email'])
        db.session.add(user)
        db.session.commit()

    # Log the user in by saving their information in the session
    session['user_id'] = user.id

    return jsonify(user_info)

