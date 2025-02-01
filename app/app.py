import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
        
    # Validar y preprocesar los datos
    input_data = np.array(data, dtype=np.float32)
    if input_data.shape != (28, 28):
        return jsonify({"error": "Invalid input shape, expected (28, 28)."}), 400
    
    prediction = np.argmax(model.predict(input_data.reshape(1, 28, 28)), axis=1)
    return jsonify({"prediction": int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
