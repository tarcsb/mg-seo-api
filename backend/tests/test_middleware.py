import pytest
from flask import Flask
from app.middleware.error_handling_middleware import ErrorHandlingMiddleware


@pytest.fixture
def app():
    app = Flask(__name__)
    app.wsgi_app = ErrorHandlingMiddleware(app.wsgi_app)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_error_handling_middleware(client):
    @client.application.route("/error")
    def error_route():
        raise ValueError("Intentional error")

    response = client.get("/error")
    assert response.status_code == 500
    assert response.get_json() == {
        "error": "An unexpected error occurred",
        "message": "Intentional error",
    }


def test_404_handling_middleware(client):
    response = client.get("/non-existent-route")
    assert response.status_code == 404
