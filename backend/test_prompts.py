import os
import requests
import json
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class PerplexityService:
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
        response = requests.post(self.api_url, headers=self.headers, data=json.dumps(data))

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"HTTP error occurred: {response.status_code} - {response.text}"}

    def run_prompts(self, prompts):
        """
        Run all prompts and store responses in a DataFrame.
        """
        results = []
        for idx, prompt in enumerate(prompts):
            print(f"Running prompt {idx + 1}/{len(prompts)}: {prompt}")
            response = self.query_perplexity(prompt)
            results.append({"prompt": prompt, "response": response})
        
        # Convert results to a DataFrame for easy analysis
        df = pd.DataFrame(results)
        return df


# Expanded list of SEO-related prompts with more real-world URLs and keywords
prompts = [
    # SEO Analysis Prompts
    "Analyze the SEO structure of the site at https://example.com. Provide specific recommendations to improve the title tags and meta descriptions.",
    "Evaluate the use of internal linking on https://example.com. Suggest strategies to improve SEO through better linking practices.",
    "Analyze the mobile-friendliness of https://example.com. How can the site be optimized for better performance on mobile devices?",
    "Evaluate the use of alt text for images on https://example.com. Suggest ways to improve image SEO for the keyword 'eco-friendly fashion'.",
    "What are the most important SEO elements that https://example.com should improve to rank higher for the keyword 'sustainable products'?",
    "Perform a technical SEO audit on https://example.com. Suggest optimizations for the site's structure, speed, and crawlability.",
    "How can https://example.com optimize its category pages for better search engine rankings?",

    # Competitor Analysis Prompts
    "Compare the backlink profile of https://example.com and https://zara.com. Suggest ways to acquire high-quality backlinks that can improve rankings for https://example.com.",
    "Evaluate the content marketing strategies of https://example.com and https://zara.com. Suggest improvements for https://example.com to better compete.",
    "How does the keyword usage of https://example.com compare to https://hm.com for the keyword 'sustainable fashion'?",
    "Perform a backlink analysis of https://example.com compared to https://hm.com. What backlinks are most valuable to acquire?",
    "Analyze the on-page SEO differences between https://example.com and https://zara.com. Suggest actionable improvements for https://example.com to rank higher.",

    # Keyword Research Prompts
    "What are the long-tail keywords related to 'eco-friendly clothing' that https://example.com should target to improve search rankings?",
    "Suggest a list of low-competition, high-traffic keywords for https://example.com to target in the sustainable fashion niche.",
    "Perform keyword gap analysis between https://example.com and https://patagonia.com. What keywords should https://example.com focus on?",
    "How can https://example.com optimize for the keyword 'organic clothing brands'? Suggest related keywords and phrases.",
    "What are the best keyword opportunities for https://example.com to improve organic search traffic in the sustainable fashion category?",
    "Evaluate the top-performing keywords for https://nike.com. How can https://example.com rank higher for related keywords in the sportswear market?",

    # Backlink Strategy Prompts
    "Analyze the quality of backlinks to https://example.com. What are the best strategies to acquire new, high-authority backlinks?",
    "How can https://example.com improve its domain authority through backlinks? Suggest relevant sites and link-building opportunities.",
    "What are the most valuable backlinks that https://example.com has? How can it leverage these backlinks for further link-building?",
    "Compare the backlink diversity between https://example.com and https://adidas.com. Suggest ways to improve backlink diversity for https://example.com.",
    "How can https://example.com increase its backlink profile for the keyword 'sustainable fashion'?",
    "Evaluate the effectiveness of the link-building strategy of https://example.com and suggest ways to improve.",

    # Local SEO Prompts
    "How can https://example.com improve its local search rankings in 'New York City' for the keyword 'eco-friendly clothing stores'?",
    "What improvements can be made to the local business schema on https://example.com to improve local search visibility?",
    "Evaluate the consistency of Name, Address, and Phone (NAP) information on https://example.com across various platforms.",
    "What are the best local SEO strategies for https://example.com to improve rankings for 'organic clothing' in Los Angeles?",
    "How can https://example.com optimize its Google My Business profile for better local SEO performance?",
    "Perform a competitor analysis for local SEO between https://example.com and https://hm.com in the city 'Los Angeles'.",

    # Content Gap Analysis Prompts
    "Perform a content gap analysis for https://example.com compared to https://patagonia.com. What content is missing on https://example.com?",
    "What are the most valuable content topics that https://example.com should target to improve search rankings?",
    "How can https://example.com improve its blog content to cover more relevant topics in sustainable fashion?",
    "What are the content gaps between https://example.com and https://zara.com for the keyword 'sustainable fashion'?",
    "Evaluate the blog content of https://example.com. Suggest content ideas that can drive more traffic in the eco-friendly clothing niche.",
    "What are the top content topics in the sustainable fashion industry that https://example.com is missing?",
    
    # E-commerce SEO Optimization Prompts
    "How can https://example.com improve its e-commerce product pages for better search engine rankings?",
    "Evaluate the product descriptions on https://example.com. Suggest ways to optimize for the keyword 'eco-friendly shoes'.",
    "How can https://example.com improve the SEO of its category pages to rank better for 'sustainable fashion'?",
    "Compare the product page SEO of https://example.com with https://nike.com. What improvements can be made to product titles and descriptions?",
    "Analyze the image SEO on https://example.com. Suggest ways to optimize alt text and file names for better rankings.",
    "What are the best practices for e-commerce SEO that https://example.com can implement to increase sales and traffic?",

    # Technical SEO Audit Prompts
    "What are the top technical SEO issues affecting https://example.com’s performance, and how can they be resolved?",
    "Analyze the structured data implementation on https://example.com. Suggest improvements for rich snippet eligibility.",
    "Evaluate the mobile performance of https://example.com. How can the site be improved for better rankings on mobile searches?",
    "What optimizations can be made to https://example.com’s page speed to improve user experience and SEO?",
    "Evaluate the SSL setup and security settings of https://example.com. How can HTTPS implementation be optimized for better SEO?",
    "Analyze the internal linking structure of https://example.com. Suggest ways to improve crawlability and link equity.",

    # Performance and Visual SEO Analysis
    "Analyze the color contrast on https://example.com for accessibility compliance. Suggest improvements that will enhance SEO and user experience.",
    "Evaluate the fonts used on https://example.com. How can they be optimized for better readability and SEO performance?",
    "How can the visual layout of https://example.com be improved for better engagement and rankings?",
    "Evaluate the mobile design of https://example.com. Suggest improvements to enhance user experience and SEO performance.",
    "What are the best visual optimization practices for https://example.com to improve its performance on search engines?",
]

# Initialize the service and run the prompts
perplexity_service = PerplexityService()
response_df = perplexity_service.run_prompts(prompts)

# Save the results to a CSV file for further analysis
output_file = "perplexity_prompts_responses.csv"
response_df.to_csv(output_file, index=False)

print(f"Results saved to {output_file}")
