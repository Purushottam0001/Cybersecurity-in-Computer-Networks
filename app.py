"""
app.py
Minimal Flask API to accept a JSON sample and return prediction (0=normal,1=attack).
"""
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.joblib")

if not os.path.exists(MODEL_PATH):
    raise RuntimeError("model.joblib not found. Run train_model.py to create it.")

data = joblib.load(MODEL_PATH)
model = data['model']

@app.route("/predict", methods=['POST'])
def predict():
    payload = request.get_json()
    try:
        df = pd.DataFrame([payload])
        pred = model.predict(df)[0]
        prob = model.predict_proba(df)[0].tolist()
        return jsonify({"prediction": int(pred), "probabilities": prob})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
