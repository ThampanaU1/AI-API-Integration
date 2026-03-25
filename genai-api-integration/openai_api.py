import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()
print("DEBUG KEY:", os.getenv("OPENAI_API_KEY"))

try:
    # Get API key
    api_key = os.getenv("OPENAI_API_KEY")

    # Check if key exists
    if not api_key:
        raise ValueError("❌ API key not found. Check your .env file")

    # Create client
    client = OpenAI(api_key=api_key)

    # Take user input
    user_input = input("Enter your prompt: ")

    # Send request to OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    # Print output
    print("\n✅ Response:\n")
    print(response.choices[0].message.content)

except Exception as e:
    print("❌ Error:", e)