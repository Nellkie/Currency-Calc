import requests

def get_courses(amount:float = 1):
    """
    Fetches the latest exchange rates for USD, JPY, KZT, and RUB against the EUR.

    This function calls the fxratesapi.com API to retrieve real-time currency 
    conversion data. The calculation is based on the Euro (EUR) as the base currency.

    Args:
        amount (float): The amount of EUR to convert. Defaults to 1.

    Returns:
        dict: A dictionary containing the converted values for USD, JPY, KZT, and RUB.
    """
    url = f"https://api.fxratesapi.com/latest?currencies=USD,%20JPY,%20KZT,%20RUB&base=EUR&amount={amount}"

    response = requests.request("GET", url)

    data = response.json()

    return {"USD": data['rates']["USD"], "JPY": data['rates']["JPY"], "KZT": data['rates']["KZT"],"RUB":  data['rates']["RUB"]}
