import requests
from bs4 import BeautifulSoup
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)

class TrendScraper:
    """Handles scraping of trending topics from getdaytrends.com."""
    
    def __init__(self, base_url: str, headers: Dict[str, str]):
        self.base_url = base_url
        self.headers = headers
    
    def get_trending_topics(self, limit: int = 5) -> List[str]:
        """Scrape top trending topics from Nigeria."""
        url = f"{self.base_url}/nigeria/"
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            
            trends = []
            trend_rows = soup.select("table tbody tr")[:limit]
            for row in trend_rows:
                topic_cell = row.select_one("td:nth-child(2) a")
                if topic_cell:
                    trends.append(topic_cell.text.strip())
            
            logger.info(f"Successfully fetched {len(trends)} trending topics")
            return trends
        except requests.RequestException as e:
            logger.error(f"Failed to fetch trends: {e}")
            return []