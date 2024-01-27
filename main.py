import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)
print(response.status_code)