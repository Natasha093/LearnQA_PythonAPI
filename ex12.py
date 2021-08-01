import requests


class TestHeaders:
    def test_headers(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        header = response.headers
        header_value = header.get("x-secret-homework-header")
        print(header)
        assert 'x-secret-homework-header' in header, "There is no x-secret-homework-header in headers"
        assert header_value == "Some secret value", "Wrong header value"




