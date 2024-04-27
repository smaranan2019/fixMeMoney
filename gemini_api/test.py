import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel('gemini-pro')


response = model.generate_content("Write a story about a magic backpack.")
print(response.text)