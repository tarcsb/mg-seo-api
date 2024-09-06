import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json

class SEOAnalysisService:
    """
    Service for performing SEO analysis on a given URL and returning structured data.
    """

    def perform_local_seo_analysis(self, url, keyword=None):
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
            seo_elements = self.extract_seo_elements(soup, url, keyword)
            return seo_elements
        except Exception as e:
            return {"error": str(e)}

    def validate_url(self, url):
        """
        Validate a given URL string.
        """
        parsed = urlparse(url)
        return all([parsed.scheme, parsed.netloc])

    def extract_seo_elements(self, soup, url, keyword=None):
        """
        Extract various SEO elements from the soup object.
        """
        title = soup.title.string if soup.title else "No title found"
        meta_description_tag = soup.find("meta", attrs={"name": "description"})
        meta_description = (
            meta_description_tag["content"]
            if meta_description_tag and meta_description_tag.get("content")
            else "No meta description found"
        )
        h1_tags = [h1.get_text() for h1 in soup.find_all("h1")]
        h2_tags = [h2.get_text() for h2 in soup.find_all("h2")]
        alt_texts_and_image_info = [
            {"alt": img.get("alt", ""), "src": img.get("src", "")}
            for img in soup.find_all("img")
        ]
        local_business_schemas = self._extract_local_business_schemas(soup)
        sitemap = self._check_sitemap(url)
        robots_txt = self._check_robots_txt(url)
        mobile_friendly = self._check_mobile_friendly(soup)
        ssl = url.startswith("https://")
        social_media_links = self._extract_social_media_links(soup)
        keyword_density = (
            self._calculate_keyword_density(soup, keyword) if keyword else "N/A"
        )
        blog = self._check_blog(soup)
        google_maps_embed = self._check_google_maps_embed(soup)

        # Combine all extracted SEO elements into a structured dictionary
        return {
            "Title": title,
            "Meta Description": meta_description,
            "H1 Tags": h1_tags,
            "H2 Tags": h2_tags,
            "Alt Texts and Image Info": alt_texts_and_image_info,
            "Local Business Schemas": local_business_schemas,
            "Sitemap": sitemap,
            "Robots.txt": robots_txt,
            "Mobile Friendly": mobile_friendly,
            "SSL": ssl,
            "Social Media Links": social_media_links,
            "Keyword Density": keyword_density,
            "Blog": blog,
            "Google Maps Embed": google_maps_embed,
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
                elif isinstance(json_content, list):
                    for item in json_content:
                        if item.get("@type") == "LocalBusiness":
                            schemas.append(item)
            except Exception as e:
                return {"error": f"Error parsing LocalBusiness schema: {e}"}
        return schemas

    def _check_sitemap(self, url):
        """
        Check if the sitemap exists.
        """
        sitemap_url = f"{url}/sitemap.xml"
        try:
            response = requests.get(sitemap_url)
            if response.status_code == 200:
                return sitemap_url
        except Exception as e:
            return f"No sitemap found: {e}"

    def _check_robots_txt(self, url):
        """
        Check if robots.txt exists.
        """
        robots_url = f"{url}/robots.txt"
        try:
            response = requests.get(robots_url)
            if response.status_code == 200:
                return robots_url
        except Exception as e:
            return f"No robots.txt found: {e}"

    def _check_mobile_friendly(self, soup):
        """
        Check if the website is mobile-friendly.
        """
        viewport_meta = soup.find("meta", attrs={"name": "viewport"})
        return bool(viewport_meta)

    def _extract_social_media_links(self, soup):
        """
        Extract social media links.
        """
        social_media_links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if any(
                platform in href
                for platform in [
                    "facebook.com",
                    "twitter.com",
                    "instagram.com",
                    "linkedin.com",
                ]
            ):
                social_media_links.append(href)
        return social_media_links

    def _calculate_keyword_density(self, soup, keyword):
        """
        Calculate keyword density.
        """
        text = soup.get_text().lower()
        word_count = len(text.split())
        keyword_count = text.count(keyword.lower())
        if word_count == 0:
            return 0
        return round((keyword_count / word_count) * 100, 2)

    def _check_blog(self, soup):
        """
        Check if a blog section exists.
        """
        blog_section = soup.find("section", id="blog") or soup.find(
            "div", class_="blog"
        )
        return bool(blog_section)

    def _check_google_maps_embed(self, soup):
        """
        Check if Google Maps is embedded.
        """
        google_maps_iframe = soup.find(
            "iframe", src=lambda src: src and "google.com/maps" in src
        )
        return bool(google_maps_iframe)

# Example of usage
seo_service = SEOAnalysisService()
url = 'https://example.com'
seo_data = seo_service.perform_local_seo_analysis(url, keyword='sustainable fashion')
print(seo_data)
