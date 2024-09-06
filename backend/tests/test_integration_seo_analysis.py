import pytest
from app.services.seo_analysis_service import SEOAnalysisService
from unittest.mock import patch


@pytest.fixture
def seo_service():
    return SEOAnalysisService()


@patch("requests.get")
def test_perform_local_seo_analysis_success(mock_get, seo_service):
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = """
        <html>
            <head><title>Test Title</title></head>
            <body><h1>Header 1</h1></body>
        </html>
    """
    result = seo_service.perform_local_seo_analysis("http://example.com")
    assert "Title" in result
    assert result["Title"] == "Test Title"


@patch("requests.get")
def test_perform_local_seo_analysis_failure(mock_get, seo_service):
    mock_get.side_effect = Exception("Failed to fetch data")
    result = seo_service.perform_local_seo_analysis("http://example.com")
    assert "error" in result
