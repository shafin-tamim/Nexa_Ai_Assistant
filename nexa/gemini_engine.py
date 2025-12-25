import google.generativeai as genai
from config.logger import get_logger

logger = get_logger(__name__)

class GeminiEngine:
    def __init__(self, api_key):
        logger.info("Initializing Gemini engine")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate(self, prompt):
        logger.info("Generating AI response")
        response = self.model.generate_content(prompt)
        return response.text
