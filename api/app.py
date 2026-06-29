import os
import torch
from flask import Flask, request, jsonify
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

app = Flask(__name__)

# -------------------------------
# Load model
# -------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = DistilBertTokenizer.from_pretrained(MODEL_DIR)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_DIR)

model.to(device)
model.eval()

# -------------------------------
# Home Route
# -------------------------------

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Prompt Security API is running!"
    })

# -------------------------------
# Prediction Route
# -------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({
            "error": "Please provide 'text' in JSON body."
        }), 400

    text = data["text"]

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    # Convert logits to probabilities
    probs = torch.softmax(outputs.logits, dim=1)

    # Get prediction
    pred = torch.argmax(probs, dim=1).item()

    # Confidence score
    confidence = probs[0][pred].item()

    # Educational context check
    educational_keywords = [
        "example",
        "tutorial",
        "explain",
        "for educational purposes",
        "demonstration",
        "research",
        "analysis",
        "sample",
        "warning"
    ]

    is_educational = any(
        keyword in text.lower()
        for keyword in educational_keywords
    )

    result = "harmful" if pred == 1 else "safe"

    # Optional: soften warning for educational content
    if result == "harmful" and is_educational:
        result = "potentially harmful (educational context detected)"

    return jsonify({
        "text": text,
        "label": pred,
        "result": result,
        "confidence": round(confidence * 100, 2),
        "educational_context": is_educational
    })

# -------------------------------
# Run Flask
# -------------------------------

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)