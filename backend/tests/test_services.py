import unittest
from unittest.mock import patch, Mock
from app.services.perplexity_service import PerplexityService
from app.services.seo_analysis_service import SEOAnalysisService
from bs4 import BeautifulSoup


class TestPerplexityService(unittest.TestCase):
    def setUp(self):
        self.perplexity_service = PerplexityService()

    @patch("requests.post")
    def test_query_perplexity_success(self, mock_post):
        # Mock a successful API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "Insight 1\n\nInsight 2"}}]
        }
        mock_post.return_value = mock_response

        prompt = "Test prompt"
        result = self.perplexity_service.query_perplexity(prompt)

        self.assertIn("actionable_insights", result)
        self.assertEqual(len(result["actionable_insights"]), 2)

    @patch("requests.post")
    def test_query_perplexity_no_choices(self, mock_post):
        # Mock a response with no choices
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"choices": []}
        mock_post.return_value = mock_response

        prompt = "Test prompt"
        result = self.perplexity_service.query_perplexity(prompt)

        self.assertEqual(
            result["error"], "No actionable insights were provided by Perplexity."
        )

    @patch("requests.post")
    def test_query_perplexity_error(self, mock_post):
        # Mock an HTTP error
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_post.return_value = mock_response

        prompt = "Test prompt"
        result = self.perplexity_service.query_perplexity(prompt)

        self.assertEqual(
            result["error"], "HTTP error occurred: 500 - Internal Server Error"
        )

    def test_create_content_optimization_prompt(self):
        url = "http://example.com"
        seo_data = {"Title": "Example Title"}
        keyword = "test"

        prompt = self.perplexity_service.create_content_optimization_prompt(
            url, seo_data, keyword
        )

        expected_prompt = (
            f"Analyze the content on the URL '{url}' for the keyword '{keyword}'. "
            f"Identify areas where the content could be better optimized for this keyword, including "
            f"improvements in keyword density, content structure, and relevance."
        )
        self.assertEqual(prompt, expected_prompt)


class TestSEOAnalysisService(unittest.TestCase):
    def setUp(self):
        self.seo_service = SEOAnalysisService()

    @patch("requests.get")
    def test_perform_local_seo_analysis_valid_url(self, mock_get):
        # Mock a successful request
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = """
        <html>
            <head><title>Test Title</title></head>
            <body><h1>Test H1</h1><meta name="description" content="Test description">
            </body>
        </html>
        """
        mock_get.return_value = mock_response

        result = self.seo_service.perform_local_seo_analysis(
            "http://example.com", "test"
        )

        self.assertEqual(result["Title"], "Test Title")
        self.assertEqual(result["Meta Description"], "Test description")
        self.assertEqual(result["H1 Tags"], ["Test H1"])

    @patch("requests.get")
    def test_perform_local_seo_analysis_invalid_url(self, mock_get):
        # Test URL validation failure
        result = self.seo_service.perform_local_seo_analysis("invalid-url")
        self.assertEqual(result["error"], "Invalid URL format")

    @patch("requests.get")
    def test_perform_local_seo_analysis_request_error(self, mock_get):
        # Mock a request error
        mock_get.side_effect = Exception("Request failed")

        result = self.seo_service.perform_local_seo_analysis("http://example.com")
        self.assertEqual(result["error"], "Request failed")

    def test_validate_url(self):
        self.assertTrue(self.seo_service.validate_url("http://example.com"))
        self.assertFalse(self.seo_service.validate_url("invalid-url"))

    def test_extract_seo_elements(self):
        # Test extracting SEO elements from HTML
        html_content = """
        <html>
            <head><title>Test Title</title><meta name="description" content="Test description"></head>
            <body><h1>Test H1</h1><h2>Test H2</h2></body>
        </html>
        """
        soup = BeautifulSoup(html_content, "html.parser")
        result = self.seo_service.extract_seo_elements(
            soup, "http://example.com", "test"
        )

        self.assertEqual(result["Title"], "Test Title")
        self.assertEqual(result["Meta Description"], "Test description")
        self.assertEqual(result["H1 Tags"], ["Test H1"])
        self.assertEqual(result["H2 Tags"], ["Test H2"])

    @patch("requests.get")
    def test_check_sitemap_exists(self, mock_get):
        # Mock sitemap found
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        result = self.seo_service._check_sitemap("http://example.com")
        self.assertEqual(result, "http://example.com/sitemap.xml")

    @patch("requests.get")
    def test_check_sitemap_not_found(self, mock_get):
        # Mock sitemap not found
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = self.seo_service._check_sitemap("http://example.com")
        self.assertTrue(result.startswith("No sitemap found"))

    @patch("requests.get")
    def test_check_robots_txt_exists(self, mock_get):
        # Mock robots.txt found
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        result = self.seo_service._check_robots_txt("http://example.com")
        self.assertEqual(result, "http://example.com/robots.txt")

    @patch("requests.get")
    def test_check_robots_txt_not_found(self, mock_get):
        # Mock robots.txt not found
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = self.seo_service._check_robots_txt("http://example.com")
        self.assertTrue(result.startswith("No robots.txt found"))

    def test_check_mobile_friendly(self):
        html_content_with_viewport = '<html><head><meta name="viewport" content="width=device-width"></head></html>'
        soup = BeautifulSoup(html_content_with_viewport, "html.parser")
        self.assertTrue(self.seo_service._check_mobile_friendly(soup))

        html_content_without_viewport = "<html><head></head></html>"
        soup = BeautifulSoup(html_content_without_viewport, "html.parser")
        self.assertFalse(self.seo_service._check_mobile_friendly(soup))

    def test_calculate_keyword_density(self):
        html_content = "<html><body>test keyword test keyword</body></html>"
        soup = BeautifulSoup(html_content, "html.parser")

        keyword_density = self.seo_service._calculate_keyword_density(soup, "keyword")
        self.assertEqual(keyword_density, 50.0)

        keyword_density_no_occurrences = self.seo_service._calculate_keyword_density(
            soup, "missing"
        )
        self.assertEqual(keyword_density_no_occurrences, 0.0)


if __name__ == "__main__":
    unittest.main()
