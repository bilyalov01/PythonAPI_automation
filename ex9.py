import requests
import json

base_url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
check_cookie_url = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

payload = {"login": "secret_login", "password": "secret_pass"}
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookie_value = response.cookies.get("auth_cookie")
cookies = {}
if cookie_value is not None:
    cookies.update({"auth_cookie": cookie_value})

response = requests.get(check_cookie_url, cookies = cookies)

print(response.text)
print(response.status_code)
print(dict(response.cookies))
print(cookie_value)