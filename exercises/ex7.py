import requests

response = (requests.request('GET', 'https://playground.learnqa.ru/ajax/api/compare_query_type'))

print(response.text)
print(response.status_code)
