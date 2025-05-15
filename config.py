from dotenv import load_dotenv
import os
from datetime import datetime

class Config:
    """Handles configuration and environment variables."""
    
    def __init__(self):
        load_dotenv()
        self.news_api_key = os.getenv("NEWS_API_KEY")
        self.trends_base_url = "https://getdaytrends.com"
        self.news_api_base_url = "https://newsapi.org/v2/everything"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
    
    def get_current_timestamp(self) -> str:
        """Return the current timestamp in ISO format."""
        return datetime.now().isoformat()