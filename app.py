from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    score = result["score"]
    if score > 0.90:
        level = "High"
    elif score > 0.70:
        level = "Moderate"
    else:
        level = "Low"

    return {
        "sentiment": result["label"],
        "confidence_score": round(score, 4),
        "confidence_percentage": f"{round(score * 100, 2)}%",
        "confidence_level": level
    }

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "service": "feedback-analyzer"}), 200

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    if not data or "feedback" not in data:
        return jsonify({"error": "Please provide 'feedback' text in JSON body"}), 400
    feedback_text = data["feedback"]
    if not isinstance(feedback_text, str) or not feedback_text.strip():
        return jsonify({"error": "Feedback must be a non-empty string"}), 400
    result = analyze_sentiment(feedback_text)
    return jsonify({
        "feedback": feedback_text,
        "sentiment": result["sentiment"],
        "confidence_score": result["confidence_score"],
        "confidence_percentage": result["confidence_percentage"],
        "confidence_level": result["confidence_level"]
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
