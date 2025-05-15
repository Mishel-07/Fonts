import requests
import json

response = requests.get("https://raw.githubusercontent.com/Mishel-07/Fonts/refs/heads/main/fonts.json")
print(response.json())
