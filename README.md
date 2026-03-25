# AI-API-Integration

# AI API Integration Project

## 📌 Description

This project demonstrates the integration of multiple Generative AI APIs using Python. Each program accepts user input, sends it to an AI service, and displays the generated response.

The project helps understand API usage, environment variables, and error handling in real-world AI applications.

---

## 🚀 APIs Implemented

* **OpenAI**

  * Code implemented successfully
  * Execution requires billing (quota limitation)

* **Groq** ✅

  * Fully working
  * Uses LLaMA-based models

* **Hugging Face** ✅

  * Implemented using Transformers (local inference)
  * Uses GPT-2 / FLAN-T5 models

* **Cohere** ✅

  * Fully working using Chat API

* **Ollama** (Optional)

  * Local model execution (optional feature)

---

## ⚙️ Features

* Accepts dynamic user input
* Sends request to AI APIs
* Displays generated responses
* Implements error handling
* Uses `.env` for secure API key storage

---

## 🛠️ Technologies Used

* Python
* Requests
* Transformers
* Cohere SDK
* dotenv

---

## 📂 Project Structure

```
AI-API-Integration/
│
├── openai_api.py
├── groq_api.py
├── huggingface_api.py
├── cohere_api.py
├── gemini_api.py (optional)
├── requirements.txt
├── README.md
├── screenshots/
│   ├── groq.png
│   ├── huggingface.png
│   ├── cohere.png
│
└── .env (not uploaded)
```

---

## ▶️ How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Create a `.env` file and add your API keys:

```
OPENAI_API_KEY=your_key
GROQ_API_KEY=your_key
HUGGINGFACE_API_KEY=your_key
COHERE_API_KEY=your_key
```

3. Run individual programs:

```
python groq_api.py
python huggingface_api.py
python cohere_api.py
python openai_api.py
```

---

## 📸 Screenshots of Output

Screenshots of each API output are included in the `screenshots/` folder.

---

## 🧪 Testing

All programs were tested successfully:

* Groq API → Working
* Hugging Face → Working
* Cohere API → Working
* OpenAI → Implemented (quota limitation)

---

## ⚠️ Notes

* OpenAI API requires billing credits to run
* Hugging Face API limitations handled using local inference
* Some models may change over time due to API updates

---

## 📌 Conclusion

This project successfully integrates multiple AI APIs and demonstrates practical usage of generative AI services in Python.

---

## 🔗 Submission

GitHub Repository Link: *(Add your GitHub link here before submitting on LMS)*
