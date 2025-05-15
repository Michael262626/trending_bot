from scraper import fetch_trending_topics
from image_fetcher import fetch_image_for_topic
from utils import sanitize_topic
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Fetching trending topics...")
    topics = fetch_trending_topics()

    results = []
    for topic in topics:
        cleaned = sanitize_topic(topic)
        logger.info(f"Fetching image for: {cleaned}")
        image_url = fetch_image_for_topic(cleaned)
        results.append({
            "topic": topic,
            "image_url": image_url
        })

    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
