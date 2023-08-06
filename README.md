# Weather Whisper
"Weather Whisper" is a Python script that acts as your reliable personal weather information assistant. With this code, you can effortlessly fetch real-time weather data for any city in the world. Using the OpenWeatherMap API, WeatherWhisper provides you with valuable details such as weather descriptions, current temperatures, and feels-like temperatures, all conveniently converted to Fahrenheit.

Simply input the name of your desired city, and WeatherWhisper will work its magic to gather the most up-to-date weather information for you. Whether you're planning a trip, preparing for your daily activities, or just curious about the weather in a specific location, WeatherWhisper is here to whisper the answers to your weather-related queries.

Stay informed and stay ahead with WeatherWhisper - your dedicated companion for weather updates \

https://github.com/yannixeno/Weather-Whisper/assets/108096250/727403cf-0410-4e57-a8ca-626588c1ad0e


# Dependency
Please get your API key from here to make this code work
https://openweathermap.org/


# The Code 
```python
import requests

API_KEY = "(Insert your own API Key"
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
```

# The explanation
Here's a step-by-step explanation of the code:

Importing the ```requests``` library: The script starts by importing the ```requests``` library, which allows making HTTP requests to external APIs.

Setting up ```API_KEY``` and ```BASE_URL```: The API_KEY variable holds the API key required to access the OpenWeatherMap API. You need to replace ```"insert api key from OpenWeatherMap"``` with your actual API key from OpenWeatherMap. The ```BASE_URL``` variable holds the base URL for the OpenWeatherMap API endpoint for fetching weather data.

Getting user input: The script prompts the user to enter the name of a city. The city name is read from the standard input using the ```input()``` function and stored in the ```city``` variable.

Building the request URL: The ```request_url``` variable is constructed using an f-string (formatted string literals) to include the API key and the city name as query parameters in the URL.

Sending the API request: The script sends an HTTP GET request to the OpenWeatherMap API using the ```requests.get()``` function with the constructed ```request_url```. The response from the API is stored in the ```response``` variable.

Processing the API response: The script checks the status code of the response using ```response.status_code```. If the status code is 200 (OK), it means the API call was successful, and it proceeds to extract weather data from the JSON response.

Extracting weather data: The JSON data from the API response is parsed using ```response.json()```, and specific weather details such as the weather description, temperature, and feels-like temperature are extracted from the JSON data.

Converting temperature to Fahrenheit: The temperature values retrieved from the API response are in Kelvin. The script converts them to Fahrenheit by applying the appropriate formula (1 Kelvin = -459.67 °F).

Printing the weather information: If the API call was successful, the script prints the weather description, temperature in Fahrenheit, and feels-like temperature in Fahrenheit.

Handling invalid requests: If the API call was not successful (status code other than 200), the script prints "not valid, Please try again."

Please note that to run this code successfully, you need to have a valid API key from OpenWeatherMap and the requests library installed in your Python environment. You can install the requests library using the following command:

```bash
pip install requests
```

# The end 
With the help of the OpenWeatherMap API and the "requests" library, we embarked on a journey to discover real-time weather information for cities around the world. "WeatherWhisper" gracefully provided us with weather descriptions, temperatures, and feels-like values, all at the tip of our fingers. 🌍

A heartfelt thank you to our users for joining us on this meteorological expedition. We hope "WeatherWhisper" served you well in your weather-related quests. 🌈

As we bid adieu to this weather wonder, we wish you sunny days, cozy evenings, and calm winds in all your future endeavors. Stay curious, stay informed, and stay weather-wise! ☀️🌧️❄️

Until we meet again,
Yanni X.
