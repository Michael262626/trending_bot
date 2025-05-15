import requests
import logging
from config import ZENSERP_API_KEY, ZENSERP_ENDPOINT

logger = logging.getLogger(__name__)

def fetch_trending_topics(limit: int = 5) -> list[str]:
    params = {
        "q": "site:twitter.com trending Nigeria",
        "location": "Nigeria",
        "tbm": "nws",
        "num": limit,
        "apikey": ZENSERP_API_KEY
    }
    try:
        response = requests.get(ZENSERP_ENDPOINT, params=params)
        response.raise_for_status()
        data = response.json()

        return [item["title"] for item in data.get("news_results", [])][:limit]
    except Exception as e:
        logger.error(f"Error fetching trending topics: {e}")
        return []
