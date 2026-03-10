import requests

url = "https://catfact.ninja/fact"

try:
    response = requests.get(url, timeout=10)
    print("Status code:", response.status_code)
    print("Response content:", response.text)
except requests.RequestException as e:
    print("Error:", e)