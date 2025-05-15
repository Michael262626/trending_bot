import requests
import logging
from typing import Optional
from config import UNSPLASH_ACCESS_KEY, UNSPLASH_ENDPOINT

logger = logging.getLogger(__name__)

def fetch_image_for_topic(topic: str) -> Optional[str]:
    headers = {
        "Accept-Version": "v1",
        "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
    }
    params = {
        "query": topic,
        "per_page": 1,
        "orientation": "landscape"
    }
    try:
        response = requests.get(UNSPLASH_ENDPOINT, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])
        if results:
            image_url = results[0]["urls"]["regular"]
            return image_url
        else:
            logger.warning(f"No image found for topic: {topic}")
            return None
    except Exception as e:
        logger.error(f"Error fetching image for topic '{topic}': {e}")
        return None
