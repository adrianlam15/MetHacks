from dotenv import load_dotenv
import os
import cohere

load_dotenv()

COHERE_API = os.getenv("COHERE_API")
print(COHERE_API)
