import requests
class TestHeaders:
    def test_headers(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.headers)

        assert 'x-secret-homework-header' in response.headers, "There is no such header"
        print("There is such header")