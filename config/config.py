import os
from dotenv import load_dotenv

load_dotenv()

SEARCH_QUERY=os.getenv("SEARCH_QUERY") or "You forgot to create SEARCH_QUERY param in .env :)"
SKIP_PERCENT=os.getenv("SKIP_PERCENT") or "12"