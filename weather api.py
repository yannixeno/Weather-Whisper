import requests

API_KEY = "insert your api key here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] * 1.8 - 459.67)
    feels_like = round(data["main"]["feels_like"] * 1.8 - 459.67)

    print("Weather:", weather)
    print("Temperature:", temperature, "°F")
    print("It Feels Like:", feels_like, "°F")
else:
    print("not valid, Please try again.")