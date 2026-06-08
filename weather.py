import requests

url = "https://wttr.in/Delhi?format=j1"

response = requests.get(url)
data = response.json()

temp = data['current_condition'][0]['temp_C']
feels_like = data['current_condition'][0]['FeelsLikeC']
description = data['current_condition'][0]['weatherDesc'][0]['value']

print(f"Delhi Weather Right Now:")
print(f"Temperature: {temp}°C")
print(f"Feels Like: {feels_like}°C")
print(f"Condition: {description}")