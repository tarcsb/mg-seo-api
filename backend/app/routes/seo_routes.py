from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from app.services.perplexity_service import PerplexityService
from app.services.seo_analysis_service import SEOAnalysisService
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Create a namespace for SEO routes
seo_ns = Namespace("seo", description="SEO-related operations")
from flask import Blueprint

seo_routes = Blueprint("seo_routes", __name__)

# Define routes here

# Input models for Swagger documentation
seo_analysis_model = seo_ns.model(
    "SEOAnalysis",
    {
        "url": fields.String(required=True, description="The URL of the site"),
        "keyword": fields.String(
            required=True, description="Target keyword for analysis"
        ),
    },
)

competitor_comparison_model = seo_ns.model(
    "CompetitorComparison",
    {
        "url": fields.String(required=True, description="The URL of your site"),
        "competitor_url": fields.String(
            required=True, description="The URL of your competitor's site"
        ),
    },
)

local_seo_model = seo_ns.model(
    "LocalSEO",
    {
        "url": fields.String(required=True, description="The URL of the site"),
        "location": fields.String(
            required=True, description="Location to enhance local SEO"
        ),
    },
)

ecommerce_seo_model = seo_ns.model(
    "EcommerceSEO",
    {
        "url": fields.String(required=True, description="The URL of the product page"),
        "product_name": fields.String(
            required=True, description="The name of the product"
        ),
    },
)

content_gap_model = seo_ns.model(
    "ContentGap",
    {
        "url": fields.String(required=True, description="The URL to analyze"),
        "related_keywords": fields.List(
            fields.String, required=True, description="Related keywords"
        ),
    },
)

backlink_strategy_model = seo_ns.model(
    "BacklinkStrategy",
    {
        "url": fields.String(
            required=True, description="The URL to analyze for backlink strategy"
        )
    },
)

# Initialize services
seo_service = SEOAnalysisService()
perplexity_service = PerplexityService()


# Perplexity Analysis Route
@seo_ns.route("/analyze/perplexity")
class PerplexityAnalysis(Resource):
    @seo_ns.expect(seo_analysis_model)
    @seo_ns.response(200, "Success")
    @seo_ns.response(400, "Validation Error")
    @seo_ns.response(500, "Internal Server Error")
    def post(self):
        """
        Analyze SEO data using the Perplexity API.
        """
        try:
            data = request.json
            url = data.get("url")
            keyword = data.get("keyword")

            # Perform local SEO analysis
            seo_data = seo_service.perform_local_seo_analysis(url, keyword)
            if "error" in seo_data:
                logger.error(
                    f"SEO Analysis failed for URL: {url} with error: {seo_data['error']}"
                )
                return jsonify(seo_data), 400

            # Create the prompt and query Perplexity API
            prompt = perplexity_service.create_content_optimization_prompt(
                url, seo_data, keyword
            )
            perplexity_result = perplexity_service.query_perplexity(prompt)

            logger.info(
                f"Perplexity analysis completed for URL: {url} with keyword: {keyword}"
            )
            return jsonify(
                {"seo_data": seo_data, "perplexity_analysis": perplexity_result}
            )
        except Exception as e:
            logger.error(
                f"Error processing Perplexity analysis for URL: {url} - {str(e)}",
                exc_info=True,
            )
            return jsonify({"error": "Internal server error", "message": str(e)}), 500


# Content Optimization Route
@seo_ns.route("/analyze/content-optimization")
class ContentOptimizationAnalysis(Resource):
    @seo_ns.expect(seo_analysis_model)
    @seo_ns.response(200, "Success")
    @seo_ns.response(400, "Validation Error")
    @seo_ns.response(500, "Internal Server Error")
    def post(self):
        """
        Optimize content for SEO using Perplexity API.
        """
        try:
            data = request.json
            url = data.get("url")
            keyword = data.get("keyword")

            # Perform local SEO analysis
            seo_data = seo_service.perform_local_seo_analysis(url, keyword)
            if "error" in seo_data:
                logger.error(
                    f"SEO Analysis failed for content optimization on URL: {url}"
                )
                return jsonify(seo_data), 400

            # Create the content optimization prompt
            prompt = perplexity_service.create_content_optimization_prompt(
                url, seo_data, keyword
            )
            perplexity_result = perplexity_service.query_perplexity(prompt)

            logger.info(f"Content optimization analysis completed for URL: {url}")
            return jsonify(perplexity_result)
        except Exception as e:
            logger.error(
                f"Error optimizing content for URL: {url} - {str(e)}", exc_info=True
            )
            return jsonify({"error": "Internal server error", "message": str(e)}), 500


# Technical SEO Audit Route
@seo_ns.route("/analyze/technical-seo")
class TechnicalSEOAudit(Resource):
    @seo_ns.expect(
        seo_ns.model(
            "SEOAudit",
            {"url": fields.String(required=True, description="The URL to audit")},
        )
    )
    @seo_ns.response(200, "Success")
    @seo_ns.response(400, "Validation Error")
    @seo_ns.response(500, "Internal Server Error")
    def post(self):
        """
        Perform a technical SEO audit.
        """
        try:
            data = request.json
            url = data.get("url")

            # Perform local SEO analysis
            seo_data = seo_service.perform_local_seo_analysis(url)
            if "error" in seo_data:
                logger.error(f"Technical SEO audit failed for URL: {url}")
                return jsonify(seo_data), 400

            # Create the technical SEO audit prompt
            prompt = perplexity_service.create_technical_seo_audit_prompt(url, seo_data)
            perplexity_result = perplexity_service.query_perplexity(prompt)

            logger.info(f"Technical SEO audit completed for URL: {url}")
            return jsonify(perplexity_result)
        except Exception as e:
            logger.error(
                f"Error performing technical SEO audit for URL: {url} - {str(e)}",
                exc_info=True,
            )
            return jsonify({"error": "Internal server error", "message": str(e)}), 500


# Local SEO Enhancement Route
@seo_ns.route("/analyze/local-seo")
class LocalSEOEnhancement(Resource):
    @seo_ns.expect(local_seo_model)
    @seo_ns.response(200, "Success")
    @seo_ns.response(400, "Validation Error")
    @seo_ns.response(500, "Internal Server Error")
    def post(self):
        """
        Enhance local SEO for a given location.
        """
        try:
            data = request.json
            url = data.get("url")
            location = data.get("location")

            # Perform local SEO analysis
            seo_data = seo_service.perform_local_seo_analysis(url)
            if "error" in seo_data:
                logger.error(f"Local SEO enhancement failed for URL: {url}")
                return jsonify(seo_data), 400

            # Create the local SEO enhancement prompt
            prompt = perplexity_service.create_local_seo_enhancement_prompt(
                url, seo_data, location
            )
            perplexity_result = perplexity_service.query_perplexity(prompt)

            logger.info(
                f"Local SEO enhancement completed for URL: {url} in location: {location}"
            )
            return jsonify(perplexity_result)
        except Exception as e:
            logger.error(
                f"Error enhancing local SEO for URL: {url} - {str(e)}", exc_info=True
            )
            return jsonify({"error": "Internal server error", "message": str(e)}), 500


# Competitor Comparison Route
@seo_ns.route("/analyze/competitor-comparison")
class CompetitorComparison(Resource):
    @seo_ns.expect(competitor_comparison_model)
    @seo_ns.response(200, "Success")
    @seo_ns.response(400, "Validation Error")
    @seo_ns.response(500, "Internal Server Error")
    def post(self):
        """
        Compare your SEO with a competitor's site.
        """
        try:
            data = request.json
            url = data.get("url")
            competitor_url = data.get("competitor_url")

            # Perform local SEO analysis
            seo_data = seo_service.perform_local_seo_analysis(url)
            if "error" in seo_data:
                logger.error(f"Competitor comparison failed for URL: {url}")
                return jsonify(seo_data), 400

            # Create the competitor comparison prompt
            prompt = perplexity_service.create_competitor_comparison_prompt(
                url, seo_data, competitor_url
            )
            perplexity_result = perplexity_service.query_perplexity(prompt)

            logger.info(
                f"Competitor comparison completed for URL: {url} with competitor: {competitor_url}"
            )
            return jsonify(perplexity_result)
        except Exception as e:
            logger.error(
                f"Error comparing competitor for URL: {url} - {str(e)}", exc_info=True
            )
            return jsonify({"error": "Internal server error", "message": str(e)}), 500


# Ecommerce SEO Optimization Route
@seo_ns.route("/analyze/ecommerce-seo")
class EcommerceSEOOptimization(Resource):
    @seo_ns.expect(ecommerce_seo_model)
    @seo_ns.response(200, "Success")
    @seo_ns.response(400, "Validation Error")
    @seo_ns.response(500, "Internal Server Error")
    def post(self):
        """
        Optimize SEO for an eCommerce product page.
        """
        try:
            data = request.json
            url = data.get("url")
            product_name = data.get("product_name")

            # Perform local SEO analysis
            seo_data = seo_service.perform_local_seo_analysis(url)
            if "error" in seo_data:
                logger.error(f"Ecommerce SEO optimization failed for URL: {url}")
                return jsonify(seo_data), 400

            # Create the eCommerce SEO optimization prompt
            prompt = perplexity_service.create_ecommerce_seo_optimization_prompt(
                url, seo_data, product_name
            )
            perplexity_result = perplexity_service.query_perplexity(prompt)

            logger.info(f"Ecommerce SEO optimization completed for URL: {url}")
            return jsonify(perplexity_result)
        except Exception as e:
            logger.error(
                f"Error optimizing eCommerce SEO for URL: {url} - {str(e)}",
                exc_info=True,
            )
            return jsonify({"error": "Internal server error", "message": str(e)}), 500


# Content Gap Analysis Route
@seo_ns.route("/analyze/content-gap")
class ContentGapAnalysis(Resource):
    @seo_ns.expect(content_gap_model)
    @seo_ns.response(200, "Success")
    @seo_ns.response(400, "Validation Error")
    @seo_ns.response(500, "Internal Server Error")
    def post(self):
        """
        Analyze content gaps for a website.
        """
        try:
            data = request.json
            url = data.get("url")
            related_keywords = data.get("related_keywords")

            # Perform local SEO analysis
            seo_data = seo_service.perform_local_seo_analysis(url)
            if "error" in seo_data:
                logger.error(f"Content gap analysis failed for URL: {url}")
                return jsonify(seo_data), 400

            # Create the content gap analysis prompt
            prompt = perplexity_service.create_content_gap_analysis_prompt(
                url, seo_data, related_keywords
            )
            perplexity_result = perplexity_service.query_perplexity(prompt)

            logger.info(f"Content gap analysis completed for URL: {url}")
            return jsonify(perplexity_result)
        except Exception as e:
            logger.error(
                f"Error analyzing content gap for URL: {url} - {str(e)}", exc_info=True
            )
            return jsonify({"error": "Internal server error", "message": str(e)}), 500


# Backlink Strategy Route
@seo_ns.route("/analyze/backlink-strategy")
class BacklinkStrategy(Resource):
    @seo_ns.expect(backlink_strategy_model)
    @seo_ns.response(200, "Success")
    @seo_ns.response(400, "Validation Error")
    @seo_ns.response(500, "Internal Server Error")
    def post(self):
        """
        Generate a backlink strategy for a website.
        """
        try:
            data = request.json
            url = data.get("url")

            # Perform local SEO analysis
            seo_data = seo_service.perform_local_seo_analysis(url)
            if "error" in seo_data:
                logger.error(f"Backlink strategy generation failed for URL: {url}")
                return jsonify(seo_data), 400

            # Create the backlink strategy prompt
            prompt = perplexity_service.create_backlink_strategy_prompt(url, seo_data)
            perplexity_result = perplexity_service.query_perplexity(prompt)

            logger.info(f"Backlink strategy generation completed for URL: {url}")
            return jsonify(perplexity_result)
        except Exception as e:
            logger.error(
                f"Error generating backlink strategy for URL: {url} - {str(e)}",
                exc_info=True,
            )
            return jsonify({"error": "Internal server error", "message": str(e)}), 500


# Register the routes
def register_routes(app, api):
    api.add_namespace(seo_ns, path="/seo")
