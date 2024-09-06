import os
from app import create_app

# Create Flask application
config_name = os.getenv('FLASK_ENV', 'development')  # Default to development
app = create_app(config_name)

if __name__ == '__main__':
    # Run the application
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
