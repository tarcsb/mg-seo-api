import os
import requests
import json


class PerplexityService:
    """
    Service for interacting with the Perplexity API and generating prompts.
    """

    def __init__(self):
        self.api_key = os.getenv("PERPLEXITY_API_KEY")
        self.api_url = "https://api.perplexity.ai/chat/completions"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def query_perplexity(self, prompt):
        """
        Send a prompt to the Perplexity API and return the parsed response.
        """
        data = {
            "model": "mistral-7b-instruct",
            "messages": [{"role": "user", "content": prompt}],
        }
        response = requests.post(
            self.api_url, headers=self.headers, data=json.dumps(data)
        )

        if response.status_code == 200:
            return self.parse_perplexity_response(response.json())
        else:
            return {
                "error": f"HTTP error occurred: {response.status_code} - {response.text}"
            }

    def parse_perplexity_response(self, perplexity_response):
        """
        Parse the response from Perplexity and extract actionable insights.
        """
        choices = perplexity_response.get("choices", [])
        if not choices:
            return {"error": "No actionable insights were provided by Perplexity."}

        content = choices[0].get("message", {}).get("content", "")
        insights = content.split("\n\n")

        actionable_items = [
            {"insight": insight.strip()} for insight in insights if insight.strip()
        ]
        return {"actionable_insights": actionable_items}

    # Prompts for various SEO use cases

    def create_content_optimization_prompt(self, url, seo_data, keyword):
        """
        Generate a prompt for content optimization analysis.
        """
        prompt = (
            f"Analyze the content on the URL '{url}' for the keyword '{keyword}'. "
            f"Identify areas where the content could be better optimized for this keyword, including "
            f"improvements in keyword density, content structure, and relevance."
        )
        return prompt

    def create_technical_seo_audit_prompt(self, url, seo_data):
        """
        Generate a prompt for technical SEO audit.
        """
        prompt = (
            f"Perform a technical SEO audit of the URL '{url}'. "
            f"Evaluate the website's performance, mobile-friendliness, SSL configuration, sitemap, "
            f"robots.txt, and schema markup. Identify any issues that prevent search engines from properly crawling the site."
        )
        return prompt

    def create_local_seo_enhancement_prompt(self, url, seo_data, location):
        """
        Generate a prompt for local SEO enhancement.
        """
        prompt = (
            f"Analyze the URL '{url}' for local SEO optimization in the area '{location}'. "
            f"Evaluate the presence of local business schemas, Google My Business integration, "
            f"NAP (Name, Address, Phone Number) consistency, and local keyword usage."
        )
        return prompt

    def create_competitor_comparison_prompt(self, url, seo_data, competitor_url):
        """
        Generate a prompt for competitor comparison analysis.
        """
        prompt = (
            f"Compare the SEO elements of the URL '{url}' with the competitor site '{competitor_url}'. "
            f"Analyze differences in keyword usage, content structure, and backlink profiles."
        )
        return prompt

    def create_ecommerce_seo_optimization_prompt(self, url, seo_data, product_name):
        """
        Generate a prompt for eCommerce SEO optimization.
        """
        prompt = (
            f"Analyze the product page at URL '{url}' for the product '{product_name}'. "
            f"Evaluate the page's SEO elements including title tags, meta descriptions, product descriptions, "
            f"alt texts for images, and schema markup. Provide recommendations for optimizing the page for search visibility."
        )
        return prompt

    def create_content_gap_analysis_prompt(self, url, seo_data, related_keywords):
        """
        Generate a prompt for content gap analysis.
        """
        prompt = (
            f"Perform a content gap analysis for the URL '{url}' with respect to the related keywords '{', '.join(related_keywords)}'. "
            f"Identify areas where the existing content lacks coverage on important topics or keywords."
        )
        return prompt

    def create_backlink_strategy_prompt(self, url, seo_data):
        """
        Generate a prompt for backlink strategy.
        """
        prompt = (
            f"Analyze the URL '{url}' and suggest a backlink strategy to improve the site's authority and search rankings. "
            f"Consider the current backlink profile and opportunities for acquiring new high-quality backlinks."
        )
        return prompt
