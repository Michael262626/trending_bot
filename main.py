from scraper import TrendScraper
from image_fetcher import NewsAPIClient
from utils import ResultsManager, setup_logging
from config import Config
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

def main():
    """Run the Nigeria Trending Topics Bot."""
    # Setup logging
    setup_logging()
    
    # Load configuration
    config = Config()
    if not config.news_api_key:
        logger.error("NEWS_API_KEY not set in .env file")
        return
    
    # Initialize components
    scraper = TrendScraper(base_url=config.trends_base_url, headers=config.headers)
    news_client = NewsAPIClient(api_key=config.news_api_key, base_url=config.news_api_base_url)
    results_manager = ResultsManager(output_dir="output")
    
    # Fetch trending topics
    logger.info("Starting to fetch trending topics")
    trends = scraper.get_trending_topics(limit=5)
    
    if not trends:
        logger.warning("No trends found. Exiting.")
        return
    
    # Fetch images for each topic
    trends_data: List[Dict[str, Any]] = []
    for topic in trends:
        images = news_client.get_news_images(topic, max_results=3)
        trends_data.append({
            "topic": topic,
            "images": images,
            "timestamp": config.get_current_timestamp()
        })
    
    # Save results
    results_manager.save_results(trends_data)

if __name__ == "__main__":
    main()