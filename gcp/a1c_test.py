import requests

url = 'https://python-gcp-561326745061.europe-west1.run.app'

body = {
    "a1c": 5.6
}

response = requests.post(url, json=body)

print(response.text)
