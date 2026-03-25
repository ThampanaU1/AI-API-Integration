import requests

try:
    user_input = input("\n👉 Enter your prompt: ")

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": user_input,
            "stream": False
        }
    )

    result = response.json()

    print("\n✅ Response:\n")
    print(result["response"])

except Exception as e:
    print("❌ Error:", e)