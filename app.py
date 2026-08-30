from flask import Flask, request, jsonify

app = Flask(__name__)

def analyze_sentiment(text):
    # Basic logic placeholder: replace with your ML model or AWS Comprehend call
    text_lower = text.lower()
    if any(word in text_lower for word in ['great', 'good', 'awesome', 'love', 'excellent']):
        return 'POSITIVE'
    elif any(word in text_lower for word in ['bad', 'poor', 'terrible', 'hate', 'horrible']):
        return 'NEGATIVE'
    return 'NEUTRAL'

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "feedback-analyzer"}), 200

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'feedback' not in data:
        return jsonify({"error": "Please provide 'feedback' text in JSON body"}), 400
    
    feedback_text = data['feedback']
    sentiment = analyze_sentiment(feedback_text)
    
    return jsonify({
        "feedback": feedback_text,
        "sentiment": sentiment
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
