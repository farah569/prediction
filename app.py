# from flask import Flask, request, jsonify
# import numpy as np
# import joblib
# import pandas as pd
# from keras.models import load_model

# app = Flask(__name__)

# # Load model and scaler
# model = load_model("greenhouse_lstm_model.h5", compile=False)
# scaler = joblib.load("scaler.save")

# # Feature list (match the order used in training!)
# features = ['temperature', 'humidity', 'moisture', 
#             'crop_type_cucumber', 'crop_type_tomato']  # Update based on your data

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         data = request.json['sequence']  # 24xN data
#         X_input = np.expand_dims(np.array(data), axis=0)

#         # Predict
#         scaled_pred = model.predict(X_input)[0]

#         # Convert back to original scale
#         dummy_row = np.zeros(len(features))
#         dummy_row[:3] = scaled_pred
#         original = scaler.inverse_transform([dummy_row])[0]
        
#         return jsonify({
#             "temperature": round(original[0], 2),
#             "humidity": round(original[1], 2),
#             "moisture": round(original[2], 2)
#         })
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from keras.models import load_model
import joblib

# Load model and scaler
model = load_model("greenhouse_lstm_model.h5", compile=False)
scaler = joblib.load("scaler.save")

# Expected feature order during training
FEATURES = ['temperature', 'humidity', 'moisture', 'crop_type_x', 'crop_type_y', 'crop_type_z']
NUM_TIMESTEPS = 24
NUM_FEATURES = len(FEATURES)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        sequence = data.get("sequence")

        # Validate shape
        if not sequence or len(sequence) != NUM_TIMESTEPS:
            return jsonify({"error": f"Expected 24 rows in sequence"}), 400
        if any(len(row) != NUM_FEATURES for row in sequence):
            return jsonify({"error": f"Each row must contain {NUM_FEATURES} features: {FEATURES}"}), 400

        # Convert and normalize
        sequence_np = np.array(sequence, dtype=np.float32)
        sequence_scaled = scaler.transform(sequence_np)
        sequence_scaled = np.expand_dims(sequence_scaled, axis=0)  # Shape: (1, 24, 6)

        # Predict
        prediction_scaled = model.predict(sequence_scaled)
        
        # Create a dummy row with predicted values + dummy crop one-hot for inverse transform
        dummy_row = np.zeros((1, NUM_FEATURES))
        dummy_row[0, :3] = prediction_scaled[0]  # temp, humidity, moisture
        # Copy crop type one-hot from last input row
        dummy_row[0, 3:] = sequence_np[-1, 3:]

        # Inverse transform to get real-world values
        prediction_real = scaler.inverse_transform(dummy_row)[0, :3]

        return jsonify({
            "predicted_temperature": round(float(prediction_real[0]), 2),
            "predicted_humidity": round(float(prediction_real[1]), 2),
            "predicted_moisture": round(float(prediction_real[2]), 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

