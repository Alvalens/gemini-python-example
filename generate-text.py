import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Use the correct model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate text
response = model.generate_content("Explain how AI works")
print(response.text)
