import requests

import requests
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-small"

headers = {
    "Authorization": "Bearer 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", 
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print("Status Code:", response.status_code)
    print("Raw response:", response.text)
    return response.json()

output = query({
    "inputs": "Today is a very nice",
    "parameters": {"max_new_tokens": 10}})