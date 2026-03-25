import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

try:
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("❌ GROQ API key not found. Check your .env file")

    client = Groq(api_key=api_key)

    user_input = input("\n👉 Enter your prompt: ")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",   # ✅ FIXED MODEL
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    print("\n✅ Response:\n")
    print(response.choices[0].message.content)

except Exception as e:
    print("❌ Error:", e)