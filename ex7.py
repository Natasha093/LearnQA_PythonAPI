import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
params = ["GET", "PUT", "POST", "DELETE", "HEAD"]
methods = ["GET", "PUT", "POST", "DELETE", "HEAD"]
payload = {}
s = requests.Session()
for i in methods:
    req_without_params = requests.Request(i, url)
    response = s.send(req_without_params.prepare())
    print(f"Ответ, если нет параметров: {response.text}, метод: {req_without_params.method}")
    for j in params:
        payload = {"method": {j}}
        if i == 'GET':
            req = requests.Request(i, url, params=payload)
        else:
            req = requests.Request(i, url, data=payload)
        print(f"Метод: {req.method}, параметр: {payload}")
        response = s.send(req.prepare())
        print(f"Ответ: {response.text}")

