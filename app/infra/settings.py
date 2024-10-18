import os
from dotenv import load_dotenv

load_dotenv()


ENVIRONMENT: str = os.getenv("ENVIRONMENT", "LOCAL")

HOST: str = os.getenv("HOST", "127.0.0.1")

PORT: int = os.getenv("PORT", 8000)

API_AUTH_TOKEN: str = os.getenv("API_AUTH_TOKEN", "")

DEBUG: bool = os.getenv("DEBUG", False)

FIREBASE_URL: str = os.getenv("FIREBASE_URL", "")

FIREBASE_API_KEY: str = os.getenv("FIREBASE_API_KEY", "")

ENCRYPTATION_KEY: str = os.getenv("ENCRYPTATION_KEY", "")
