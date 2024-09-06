import logging
from flask import jsonify


class ErrorHandlingMiddleware:
    def __init__(self, app):
        self.app = app
        self.logger = logging.getLogger(__name__)

    def __call__(self, environ, start_response):
        try:
            return self.app(environ, start_response)
        except Exception as e:
            self.logger.error(f"Error: {str(e)}", exc_info=True)
            res = jsonify({"error": "An unexpected error occurred", "message": str(e)})
            start_response(
                "500 INTERNAL SERVER ERROR", [("Content-Type", "application/json")]
            )
            return [res.data]
