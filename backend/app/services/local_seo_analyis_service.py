import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json

class LocalSEOAnalysisService:
    """
    Service for performing Local SEO analysis on a given URL.
    """

    def perform_local_seo_analysis(self, url, location, keyword=None):
        """
        Perform a local SEO analysis on the given URL.
        """
        if not self.validate_url(url):
            return {"error": "Invalid URL format"}

        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            # Extract SEO elements
            seo_elements = self.extract_local_seo_elements(soup, url, location, keyword)
            return seo_elements
        except Exception as e:
            return {"error": str(e)}

    def validate_url(self, url):
        """
        Validate a given URL string.
        """
        parsed = urlparse(url)
        return all([parsed.scheme, parsed.netloc])

    def extract_local_seo_elements(self, soup, url, location, keyword=None):
        """
        Extract various local SEO elements from the soup object.
        """
        title = soup.title.string if soup.title else "No title found"
        meta_description_tag = soup.find("meta", attrs={"name": "description"})
        meta_description = (
            meta_description_tag["content"]
            if meta_description_tag and meta_description_tag.get("content")
            else "No meta description found"
        )
        
        # Extract local business schema, maps, and Google My Business integration
        local_business_schemas = self._extract_local_business_schemas(soup)
        google_maps_embed = self._check_google_maps_embed(soup)

        # NAP consistency could come from various online platforms, but we'll simplify for now.
        nap_consistency = self._check_nap_consistency(url)

        return {
            "Title": title,
            "Meta Description": meta_description,
            "Location": location,
            "NAP Consistency": nap_consistency,
            "Local Business Schemas": local_business_schemas,
            "Google Maps Embed": google_maps_embed
        }

    def _extract_local_business_schemas(self, soup):
        """
        Extract LocalBusiness schemas from the HTML.
        """
        schemas = []
        for script in soup.find_all("script", type="application/ld+json"):
            try:
                json_content = json.loads(script.string)
                if (
                    isinstance(json_content, dict)
                    and json_content.get("@type") == "LocalBusiness"
                ):
                    schemas.append(json_content)
            except Exception as e:
                return {"error": f"Error parsing LocalBusiness schema: {e}"}
        return schemas

    def _check_google_maps_embed(self, soup):
        """
        Check if Google Maps is embedded.
        """
        google_maps_iframe = soup.find(
            "iframe", src=lambda src: src and "google.com/maps" in src
        )
        return bool(google_maps_iframe)

    def _check_nap_consistency(self, url):
        """
        Simulate checking NAP (Name, Address, Phone) consistency for now.
        """
        # In a real-world scenario, you'd want to check platforms like Google My Business, Yelp, and more.
        # For simplicity, we'll return a dummy value here.
        return "Consistent across platforms"
