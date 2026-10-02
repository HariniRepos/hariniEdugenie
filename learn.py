from flask import Blueprint, request, jsonify
from services import gemini_service as gs

learn_bp = Blueprint("learn", __name__)


def _run(fn, *args):
    try:
        return jsonify({"result": fn(*args)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@learn_bp.post("/chat")
def chat():
    data = request.get_json(force=True)
    return _run(gs.chat, data.get("question", ""))


@learn_bp.post("/explain")
def explain():
    data = request.get_json(force=True)
    return _run(gs.explain, data.get("topic", ""), data.get("level", "Beginner"))


@learn_bp.post("/quiz")
def quiz():
    data = request.get_json(force=True)
    return _run(gs.generate_quiz, data.get("topic", ""), int(data.get("count", 5)))


@learn_bp.post("/summarize")
def summarize():
    data = request.get_json(force=True)
    return _run(gs.summarize, data.get("notes", ""))
