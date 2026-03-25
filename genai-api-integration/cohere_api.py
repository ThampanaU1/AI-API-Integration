import os
import cohere
from dotenv import load_dotenv

load_dotenv()

try:
    api_key = os.getenv("COHERE_API_KEY")

    if not api_key:
        raise ValueError("❌ Cohere API key not found")

    co = cohere.Client(api_key)

    user_input = input("\n👉 Enter your prompt: ")

    # ✅ NEW CHAT API
    response = co.chat(
        model="command-a-vision-07-2025",
        message=user_input
    )

    print("\n✅ Response:\n")
    print(response.text)

except Exception as e:
    print("❌ Error:", e)