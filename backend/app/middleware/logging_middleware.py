import os
import logging
from logging.config import dictConfig
from logstash_formatter import LogstashFormatterV1


class LoggingMiddleware:
    def __init__(self, app):
        self.app = app
        self.logger = logging.getLogger(__name__)
        self.configure_logging()

    def __call__(self, environ, start_response):
        self.logger.info(f"Request: {environ['REQUEST_METHOD']} {environ['PATH_INFO']}")
        return self.app(environ, start_response)

    def configure_logging(self):
        """
        Configures logging to either local file or ELK (Logstash).
        """
        log_type = os.getenv(
            "LOG_TYPE", "local"
        )  # 'elk' for production, 'local' for development
        log_level = os.getenv("LOG_LEVEL", "INFO")

        if log_type == "elk":
            # Log to Logstash (ELK)
            logstash_host = os.getenv("LOGSTASH_HOST", "localhost")
            logstash_port = int(os.getenv("LOGSTASH_PORT", 5044))

            self.logger.setLevel(log_level)
            handler = logging.handlers.SocketHandler(logstash_host, logstash_port)
            handler.setFormatter(LogstashFormatterV1())
            self.logger.addHandler(handler)
        else:
            # Log locally to file
            dictConfig(
                {
                    "version": 1,
                    "formatters": {
                        "default": {
                            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        },
                    },
                    "handlers": {
                        "console": {
                            "class": "logging.StreamHandler",
                            "formatter": "default",
                        },
                        "file": {
                            "class": "logging.FileHandler",
                            "formatter": "default",
                            "filename": "app.log",
                        },
                    },
                    "root": {
                        "level": log_level,
                        "handlers": ["console", "file"],
                    },
                }
            )
