import requests

url = "http://127.0.0.1:8000/books"
response = requests.get(url)

print(response.json())