from transformers import pipeline

try:
    print("Loading model...")

    generator = pipeline(
        "text-generation",
        model="gpt2"
    )

    user_input = input("\n👉 Enter your prompt: ")

    # ✅ Better prompt format
    prompt = f"Answer the question clearly:\n{user_input}\nAnswer:"

    result = generator(
        prompt,
        max_new_tokens=50,
        pad_token_id=50256
    )

    print("\n✅ Output:\n")
    print(result[0]["generated_text"])

except Exception as e:
    print("❌ Error:", e)