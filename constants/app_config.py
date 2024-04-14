import os
from dotenv import load_dotenv

# Load environment variables from a .env file (optional)
load_dotenv()

HOST: str = os.getenv("HOST", "0.0.0.0")
PORT: int = int(os.getenv("PORT", 8000))