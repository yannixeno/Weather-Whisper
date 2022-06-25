import requests

BASE_URL = "https://api.kanye.rest"

response = requests.get(BASE_URL)

if response.status_code == 200:
    data = response.json()
    quote = data['quote']

    print("Kanye West said: " + quote)

else:
    print("An error occurred.")

    