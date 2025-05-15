import re

def sanitize_topic(topic: str) -> str:
    # Remove URLs, mentions, hashtags and extra whitespace
    topic = re.sub(r"http\S+|@\S+|#\S+", "", topic)
    topic = topic.strip()
    return topic
