import time
import google.generativeai as genai

from config import GEMINI_API_KEY, DEFAULT_MODEL, MAX_RETRIES, RETRY_DELAY
from utils import get_logger

logger = get_logger(__name__)


import os

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:

    raise ValueError(" GEMINI_API_KEY not found in .env file!")

genai.configure(api_key=GEMINI_API_KEY)


class LLMClient:
    """Wrapper for Google Generative AI (Gemini) model."""
    
    def __init__(self, model_name = "gemini-3.1-flash-lite"):
        self.model = genai.GenerativeModel(model_name)

    def generate(self, prompt: str) -> str:
        """Generate content using the Gemini model."""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating response: {e}")
            raise

    def __call__(self, prompt: str) -> str:
        """Alias for backward compatibility with old code."""
        return self.generate(prompt)