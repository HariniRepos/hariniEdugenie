# EduGenie: Google Gemini Powered Learning Assistant

EduGenie is a Flask web app that uses Google Gemini to explain topics, answer
doubts, generate quizzes and summarize study notes.

## Features
- Ask doubts / chat with the AI tutor
- Explain any topic at Beginner, Intermediate or Advanced level
- Auto-generate multiple-choice quizzes
- Summarize study notes

## Setup
1. `python -m venv venv && source venv/bin/activate` (Windows: `venv\Scripts\activate`)
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your Gemini API key
   (get one at https://aistudio.google.com/apikey)
4. `python app.py`
5. Open http://127.0.0.1:5000

## Folder Structure
```
EduGenie/
├── app.py
├── config.py
├── requirements.txt
├── .env.example
├── routes/         # API endpoints
├── services/       # Gemini integration
├── templates/      # HTML pages
├── static/         # CSS and JS
├── docs/           # Documentation
└── tests/          # Tests
```
