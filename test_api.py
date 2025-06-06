import requests

url = "http://127.0.0.1:5000/predict"
payload = {
    "sequence": [
        [23.0, 60.1, 30.0, 1, 0, 0],
        [23.6, 60.2, 30.1, 1, 0, 0],
        [23.7, 60.3, 30.2, 1, 0, 0],
        [23.8, 60.2, 30.1, 1, 0, 0],
        [23.9, 60.1, 30.0, 1, 0, 0],
        [24.0, 60.0, 29.9, 1, 0, 0],
        [24.1, 59.9, 29.8, 1, 0, 0],
        [24.2, 59.8, 29.7, 1, 0, 0],
        [24.3, 59.7, 29.6, 1, 0, 0],
        [24.4, 59.6, 29.5, 1, 0, 0],
        [24.5, 59.5, 29.4, 1, 0, 0],
        [24.6, 59.4, 29.3, 1, 0, 0],
        [24.7, 59.3, 29.2, 1, 0, 0],
        [24.8, 59.2, 29.1, 1, 0, 0],
        [24.9, 59.1, 29.0, 1, 0, 0],
        [25.0, 59.0, 28.9, 1, 0, 0],
        [25.1, 58.9, 28.8, 1, 0, 0],
        [25.2, 58.8, 28.7, 1, 0, 0],
        [25.3, 58.7, 28.6, 1, 0, 0],
        [25.4, 58.6, 28.5, 1, 0, 0],
        [25.5, 58.5, 28.4, 1, 0, 0],
        [25.6, 58.4, 28.3, 1, 0, 0],
        [25.7, 58.3, 28.2, 1, 0, 0],
        [25.8, 58.2, 28.1, 1, 0, 0]
    ]
}

response = requests.post(url, json=payload)
print(response.json())


