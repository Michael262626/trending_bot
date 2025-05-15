import requests
from typing import List, Dict, Any
from retrying import retry
import logging

logger = logging.getLogger(__name__)

class NewsAPIClient:
    """Handles fetching news images via NewsAPI."""
    
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
    
    @retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000, wait_exponential_max=10000)
    def get_news_images(self, topic: str, max_results: int = 3) -> List[Dict[str, Any]]:
        """Fetch news articles with images for a topic."""
        params = {
            "q": f"{topic} Nigeria",
            "apiKey": self.api_key,
            "language": "en",
            "sortBy": "relevancy",
            "pageSize": max_results
        }
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            images = []
            for article in data.get("articles", []):
                if article.get("urlToImage"):
                    images.append({
                        "image_url": article["urlToImage"],
                        "article_title": article.get("title", ""),
                        "source": article.get("source", {}).get("name", ""),
                        "article_url": article.get("url", "")
                    })
            
            logger.info(f"Fetched {len(images)} images for topic: {topic}")
            return images
        except requests.RequestException as e:
            logger.error(f"Failed to fetch news for {topic}: {e}")
            return []