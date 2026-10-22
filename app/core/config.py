from dotenv import load_dotenv
import os

load_dotenv()
class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

settings = Settings()