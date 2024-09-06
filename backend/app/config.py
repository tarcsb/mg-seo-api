import os
from logging.config import dictConfig
from logstash_formatter import LogstashFormatterV1


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = False
    TESTING = False

    # Database Configuration (if needed)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///default.db")

    # Airtable Configuration
    AIRTABLE_PERSONAL_ACCESS_TOKEN = os.getenv("AIRTABLE_PERSONAL_ACCESS_TOKEN")
    AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
    AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")

    # Perplexity API Configuration
    PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

    # Stripe API Configuration
    STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY")
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")

    # Logging Configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_MODE = os.getenv("LOG_MODE", "console")  # 'console', 'file', or 'logstash'
    LOGSTASH_HOST = os.getenv("LOGSTASH_HOST", "localhost")
    LOGSTASH_PORT = int(os.getenv("LOGSTASH_PORT", 5044))

    @staticmethod
    def init_app(app):
        """Initialize logging and other configurations for the app."""
        log_mode = os.getenv("LOG_MODE", "console")

        handlers = ["console"]  # Default to console logging
        if log_mode == "file" or log_mode == "all":
            handlers.append("file")
        if log_mode == "logstash" or log_mode == "all":
            handlers.append("logstash")

        dictConfig(
            {
                "version": 1,
                "formatters": {
                    "default": {
                        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                    },
                    "logstash": {"()": LogstashFormatterV1},  # Logstash formatter
                },
                "handlers": {
                    "console": {
                        "class": "logging.StreamHandler",
                        "formatter": "default",
                        "level": Config.LOG_LEVEL,
                    },
                    "file": {
                        "class": "logging.FileHandler",
                        "formatter": "default",
                        "filename": "app.log",
                        "level": Config.LOG_LEVEL,
                    },
                    "logstash": {
                        "class": "logging.handlers.SocketHandler",
                        "formatter": "logstash",
                        "host": Config.LOGSTASH_HOST,
                        "port": Config.LOGSTASH_PORT,
                        "level": Config.LOG_LEVEL,
                    },
                },
                "root": {"level": Config.LOG_LEVEL, "handlers": handlers},
            }
        )


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///dev.db")


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///test.db")
    LOG_LEVEL = "DEBUG"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///prod.db")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING")

    @staticmethod
    def init_app(app):
        """Production-specific logging and configurations."""
        Config.init_app(app)
        # Additional production-specific initializations can go here.
