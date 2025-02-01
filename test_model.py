import requests
import numpy as np

# URL de la API desplegada en Google Cloud Run (reemplázala con tu URL real)
CLOUD_RUN_URL = "https://ci-cd-ia-xxxxx-uc.a.run.app/predict"

# Generar un número aleatorio simulando un dígito del dataset MNIST (28x28)
dummy_data = np.random.rand(28, 28).tolist()

# Crear payload con la imagen como JSON
payload = {"data": dummy_data}

# Realizar la petición POST a la API
response = requests.post(CLOUD_RUN_URL, json=payload)

# Imprimir respuesta de la API
if response.status_code == 200:
    print("Predicción del modelo:", response.json())
else:
    print("Error en la petición:", response.status_code, response.text)
