import requests

response = requests.get("https://api.quotable.io/random")
response.raise_for_status()
data = response.json()
print(data["content"])
print(data["author"])