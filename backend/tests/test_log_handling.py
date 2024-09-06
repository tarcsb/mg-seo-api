import logging


def test_logging_middleware(client, caplog):
    with caplog.at_level(logging.INFO):
        response = client.get("/example-endpoint")
        assert response.status_code == 200
        assert "GET /example-endpoint" in caplog.text
