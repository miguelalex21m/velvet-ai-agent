from dotenv import load_dotenv
import os

load_dotenv()

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Di hola")
print(response.text)
