import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

gemini = os.getenv('GEMINI_API_KEY')

