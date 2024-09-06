import os
from flask import Flask
from app.config import DevelopmentConfig, ProductionConfig
from flask_restx import Api
from app.middleware.error_handling_middleware import ErrorHandlingMiddleware
from app.routes.seo_routes import register_routes
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def create_app(config_class=None):
    # Initialize the Flask app
    app = Flask(__name__)

    # Load configuration based on the environment
    if not config_class:
        config_class = (
            DevelopmentConfig
            if os.getenv("FLASK_ENV") == "development"
            else ProductionConfig
        )
    app.config.from_object(config_class)

    # Initialize logging and error handling
    config_class.init_app(app)

    # Add middleware for error handling
    app.wsgi_app = ErrorHandlingMiddleware(app.wsgi_app)

    # Initialize API using Flask-RESTX
    api = Api(
        app,
        version="1.0",
        title="SEO Analysis API",
        description="A RESTful API for SEO Analysis and Optimizations",
    )

    # Register routes
    register_routes(app, api)

    return app


if __name__ == "__main__":
    # Initialize Flask app and run
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
