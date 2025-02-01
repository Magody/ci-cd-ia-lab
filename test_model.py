import requests
import numpy as np

# URL de la API desplegada en Google Cloud Run (reemplázala con tu URL real)
# https://ci-cd-ia-410479778764.us-central1.run.app
CLOUD_RUN_URL = "http://127.0.0.1:8080/predict"

# Generar un número aleatorio simulando un dígito del dataset MNIST (28x28)
dummy_data = np.random.rand(28, 28).tolist()  # Simula una imagen de 28x28

# Enviar datos en el formato correcto
payload = {"data": dummy_data}
response = requests.post(CLOUD_RUN_URL, json=payload)
# Imprimir respuesta de la API
if response.status_code == 200:
    print("Predicción del modelo:", response.json())
else:
    print("Error en la petición:", response.status_code, response.text)
