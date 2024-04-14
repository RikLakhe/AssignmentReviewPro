import os
from dotenv import load_dotenv

# Load environment variables from a .env file (optional)
load_dotenv()

DB_HOST: str = os.getenv("DB_HOST", "0.0.0.0")
DB_PORT: int = int(os.getenv("DB_PORT", 8000))
DB_NAME: str = os.getenv("DB_NAME", "boiler")
DB_USER: str = os.getenv("DB_USER", "user")
DB_PASSWORD: str = os.getenv('DB_PASSWORD', 'pass')
