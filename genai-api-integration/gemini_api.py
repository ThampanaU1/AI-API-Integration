import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

try:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("❌ Gemini API key not found")

    genai.configure(api_key=api_key)

    # ✅ Use correct model format
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    user_input = input("\n👉 Enter your prompt: ")

    response = model.generate_content(user_input)

    print("\n✅ Response:\n")
    print(response.text)

except Exception as e:
    print("❌ Error:", e)