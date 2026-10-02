from google import genai
import config

_client = None


def _get_client():
    global _client
    if _client is None:
        if not config.GEMINI_API_KEY:
            raise RuntimeError("GEMINI_API_KEY is not set. Add it to your .env file.")
        _client = genai.Client(api_key=config.GEMINI_API_KEY)
    return _client


def ask_gemini(prompt: str) -> str:
    response = _get_client().models.generate_content(
        model=config.GEMINI_MODEL, contents=prompt
    )
    return response.text


def chat(question: str) -> str:
    return ask_gemini(
        "You are EduGenie, a friendly and clear tutor. Answer the student's "
        f"question simply with examples.\n\nQuestion: {question}"
    )


def explain(topic: str, level: str = "Beginner") -> str:
    return ask_gemini(
        f"Explain '{topic}' for a {level} level student. Use simple language, "
        "an analogy, and a short example."
    )


def generate_quiz(topic: str, count: int = 5) -> str:
    return ask_gemini(
        f"Create {count} multiple-choice questions on '{topic}'. For each give "
        "4 options (A-D) and mark the correct answer with a short explanation."
    )


def summarize(notes: str) -> str:
    return ask_gemini(
        f"Summarize these study notes into concise bullet points:\n\n{notes}"
    )
