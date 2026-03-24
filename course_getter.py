import requests

def get_courses():
    url = "https://api.fxratesapi.com/latest?currencies=USD,%20JPY,%20KZT,%20RUB&base=EUR&amount=1"

    response = requests.request("GET", url)

    data = response.json()

    return data['rates']["USD"], data['rates']["JPY"], data['rates']["KZT"], data['rates']["RUB"]

print(get_courses())