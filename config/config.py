import os
from dotenv import load_dotenv

load_dotenv()

SEARCH_QUERY=os.getenv("SEARCH_QUERY")
SKIP_PERCENT=os.getenv("SKIP_PERCENT")