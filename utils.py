import logging
from pathlib import Path
from typing import List, Dict, Any
import json
from datetime import datetime

def setup_logging() -> None:
    """Configure logging for the bot."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('trending_bot.log'),
            logging.StreamHandler()
        ]
    )

class ResultsManager:
    """Handles saving results to JSON files."""
    
    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def save_results(self, trends_data: List[Dict[str, Any]]) -> str:
        """Save trending topics and images to a JSON file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.output_dir / f"trending_nigeria_{timestamp}.json"
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(trends_data, f, indent=4, ensure_ascii=False)
        
        logging.getLogger(__name__).info(f"Results saved to {filename}")
        return str(filename)