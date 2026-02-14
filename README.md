# Ai-Career-Roadmap-Generator
A web-based AI-powered application that generates personalized career roadmaps using Groq LLMs and Gradio.  This project helps users plan their learning journey with clear timelines, skills, tools, projects, and career guidance.
## 📌 Features

* ✅ AI-generated career roadmaps
* ✅ Month-wise learning plans
* ✅ Skills, tools, and resources
* ✅ Project suggestions
* ✅ Job roles & salary estimates
* ✅ Download roadmap as a text file
* ✅ Clean and modern UI (Gradio)

## 🛠️ Tech Stack

* Python 3.9+
* Gradio (Frontend UI)
* Groq API (LLM Backend)
* Hugging Face Spaces (Deployment)

---

## 📂 Project Structure

```
├── app.py              # Main application file
├── requirements.txt    # Dependencies
├── README.md           # Documentation
```

---

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone the Repository


### 2️⃣ Create Virtual Environment (Optional)

### 3️⃣ Install Dependencies

## 🔑 API Key Setup (Important)

This project uses the Groq API.
#### Google Colab

```python
import os
os.environ["GROQ_API_KEY"] = "your_api_key_here"
```
#### Hugging Face Spaces (Secrets)

Add a secret:
```
Name: GROQ_API_KEY
Value: your_api_key_here
```
## 🌐 Deploy on Hugging Face Spaces

### 1️⃣ Create New Space

* Go to Hugging Face
* Click "New Space"
* Select: Gradio

## 🐛 Common Errors & Solutions

### ❌ Error: model_decommissioned

**Reason:** Using old model name

**Fix:**

```python
model="llama-3.3-70b-versatile

### ❌ APIConnectionError

**Reasons:**

* Missing API key
* Wrong secret name
* Network issue

**Fix:**

* Ensure `GROQ_API_KEY` is set
* Restart runtime
* Check internet

---

### ❌ App Not Loading on HF

**Fix:**

* Check logs
* Verify requirements.txt
* Restart space

---

## 🧪 Testing

Before deployment, test locally:

```bash
python app.py
```

Try generating a roadmap with sample input.

---

## 🚀 Future Improvements

* PDF export
* User accounts
* Roadmap history
* Multiple languages
* More AI models

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create new branch
3. Make changes
4. Submit pull request

---

If you like this project, please ⭐ star the repository on GitHub!
