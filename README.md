# 🤖 AI Personality Chatbot

An interactive AI chatbot built with **Streamlit** and **Groq LLMs**. Users can select different AI personalities and Groq models for real-time conversations. Each personality is restricted to its specific domain using prompt engineering.

---

## 🚀 Live Demo

🔗 **Live App:** https://ai-personality-chatbot-spiral-lab.streamlit.app/

---

## Features

- Interactive Streamlit chat interface
- Multiple Groq AI models
- Personality-based chatbot
- Domain-restricted responses
- Session memory
- Clear chat functionality
- Error handling
- Responsive UI

---

## Available Personalities

- ➕ Math Teacher
- 🩺 Doctor
- ✈️ Travel Guide
- 👨‍🍳 Chef
- 💻 Tech Support

---

## Tech Stack

- Python
- Streamlit
- Groq API

---

## Project Structure

AI-Agent-Chatbot/
├── app.py
├── groq_helper.py
├── prompts.py
├── requirements.txt
├── README.md

---

## Installation

```bash
git clone https://github.com/your-username/AI-Agent-Chatbot.git

cd AI-Agent-Chatbot

pip install -r requirements.txt

streamlit run app.py
```

---

## Environment Variables

Create:

```
.streamlit/secrets.toml
```

Add:

```toml
GROQ_API_KEY="your_api_key"
```

---

