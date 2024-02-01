import time
import requests
import json

base_url = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(base_url)
token = response.json().get("token")
sleep = response.json().get("seconds")
params = {"token": token}
print(sleep)

while "result" not in response.text:
    response = requests.get(base_url, params=params)
    if response.json().get("status") == "Job is NOT ready":
        time.sleep(sleep)

print(response.status_code)
print(response.text)
