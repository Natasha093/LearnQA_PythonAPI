import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
responses = response.history
count = len(responses)
print(f"Количество редиректов {count}")
print(response.url)