import requests


class TestCookie:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie = response.cookies
        print(cookie.items())
        cookie_value = cookie.get("HomeWork")
        assert "HomeWork" in cookie, "Wrong cookie"
        assert cookie_value == "hw_value", "Wrong cookie value"
