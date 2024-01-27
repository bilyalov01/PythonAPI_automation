import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

k=0
for i in range(len(response.history)):
     print(response.history[i].url)
     k +=1

print(k)
print(response.text)
print(response.status_code)
print(response.url)