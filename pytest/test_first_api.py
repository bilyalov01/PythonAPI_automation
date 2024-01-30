import requests


class TestFirstAPI:
    def test_call_hello(self):
        url = "https://playground.learnqa.ru/api/hello"
        name = 'Ivan'
        data = {'name': name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is no field 'answer' in the response"

        expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]

        assert actual_response_text == expected_response_text, "Actual text in response is not correct"
