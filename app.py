from flask import Flask, request, jsonify
import numpy as np
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS is applied only once and correctly

# Load saved model, scaler, and label encoder
model = joblib.load("random_forest_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

@app.route("/")
def home():
    return "Emotion Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Validate input
        if "features" not in data:
            return jsonify({"error": "Missing 'features' in request"}), 400

        features = np.array(data["features"]).reshape(1, -1)
        features_scaled = scaler.transform(features)

        prediction = model.predict(features_scaled)[0]
        emotion_label = label_encoder.inverse_transform([prediction])[0]

        return jsonify({"predicted_emotion": emotion_label})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
