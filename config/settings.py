import os
from dotenv import load_dotenv
from config.logger import get_logger

logger = get_logger(__name__)
load_dotenv()

class Settings:
    def load_api_key(self):
        logger.info("Loading API key")
        return os.getenv("GOOGLE_API_KEY")
