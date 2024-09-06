import pytest
from flask import Flask
from flask_restx import Api
from unittest.mock import patch
from app.routes.seo_routes import seo_ns


@pytest.fixture
def app():
    app = Flask(__name__)
    api = Api(app)
    api.add_namespace(seo_ns, path="/seo")
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@patch(
    "app.services.seo_analysis_service.SEOAnalysisService.perform_local_seo_analysis"
)
@patch("app.services.perplexity_service.PerplexityService.query_perplexity")
def test_analyze_perplexity_success(mock_perplexity, mock_seo_analysis, client):
    mock_seo_analysis.return_value = {"seo_data": "mocked_data"}
    mock_perplexity.return_value = {"perplexity_analysis": "mocked_result"}

    response = client.post(
        "/seo/analyze/perplexity", json={"url": "http://example.com", "keyword": "test"}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "seo_data" in data
    assert "perplexity_analysis" in data


@patch(
    "app.services.seo_analysis_service.SEOAnalysisService.perform_local_seo_analysis"
)
def test_analyze_perplexity_missing_url(mock_seo_analysis, client):
    response = client.post("/seo/analyze/perplexity", json={"keyword": "test"})
    assert response.status_code == 400
    assert "error" in response.get_json()


@patch(
    "app.services.seo_analysis_service.SEOAnalysisService.perform_local_seo_analysis"
)
@patch("app.services.perplexity_service.PerplexityService.query_perplexity")
def test_analyze_perplexity_failure(mock_perplexity, mock_seo_analysis, client):
    mock_seo_analysis.return_value = {"seo_data": "mocked_data"}
    mock_perplexity.return_value = {
        "error": "Failed to get a response from Perplexity API"
    }

    response = client.post(
        "/seo/analyze/perplexity", json={"url": "http://example.com", "keyword": "test"}
    )
    assert response.status_code == 500
    assert "error" in response.get_json()
