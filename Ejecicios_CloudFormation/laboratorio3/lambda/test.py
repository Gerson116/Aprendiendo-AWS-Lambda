# Con API Key
import requests

headers = {
    'Authorization': 'Bearer tu-api-key-secreta-1',
    'Content-Type': 'application/json'
}

response = requests.get('https://tu-lambda-url.com', headers=headers)