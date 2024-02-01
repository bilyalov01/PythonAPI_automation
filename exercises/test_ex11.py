import requests

class TestCookie:
    def test_cookie_method(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")

        cookie_value = response.cookies
        print(dict(cookie_value))

        assert 'HomeWork' in cookie_value, "There is no cookie"