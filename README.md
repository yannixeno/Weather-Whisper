# WeatherWhisper - Your Weather Forecast Assistant

WeatherWhisper is a simple and intuitive Python GUI application that helps you fetch real-time weather data for any city around the world. With a beautiful and user-friendly interface built using tkinter, WeatherWhisper allows you to quickly check the current weather conditions, temperature, and feels-like temperature in both Celsius and Fahrenheit.


![ezgif com-video-to-gif (1)](https://github.com/yannixeno/Weather-Whisper/assets/108096250/474d4b9b-3152-4361-a170-972aa7117c4c)

![ezgif com-video-to-gif (4)](https://github.com/yannixeno/Weather-Whisper/assets/108096250/b77027f4-a107-4ef2-ad88-28f5ad0d9922)







# Features
- Easy-to-Use Interface: WeatherWhisper provides a hassle-free experience with an elegant and straightforward user interface. Simply enter the name of your desired city, click "Get Weather," and get instant weather updates!

- Switchable Temperature Units: WeatherWhisper lets you view temperatures in both Celsius and Fahrenheit units. Just click the "Switch Units" button to toggle between them.

- Real-Time Data: The application fetches weather data from the OpenWeatherMap API, ensuring you receive up-to-date and accurate weather information.

- Error Handling: WeatherWhisper gracefully handles various scenarios, such as invalid city names, connection errors, and API-related issues, ensuring a smooth user experience.

# Getting Started
To use Weather Whisper, you'll need to obtain an API key from [OpenWeatherMap](https://openweathermap.org/).. Don't worry; it's a quick and easy process! Just follow the steps provided in the [Setup Guide](https://openweathermap.org/appid) to acquire your API key and configure the application.


# Dependency
To run WeatherWhisper, you'll need the following dependencies installed in your Python environment:

- [Python](https://www.python.org/): The programming language used to build the application.
- [tkinter](https://docs.python.org/3/library/tkinter.html): The standard GUI library for Python.
- [requests](https://docs.python-requests.org/en/latest/): A powerful HTTP library to make API requests.
- [configparser](https://docs.python.org/3/library/configparser.html): A module to work with configuration files.

You can install the necessary Python packages using pip. For example:

```bash
pip install requests
```

# How to run 
1. Clone the repository to your local machine.
2. Make sure you have Python and the required libraries (tkinter, requests, configparser) installed.
3. Add your API key to the config.ini file as per the provided Setup Guide.
4. Run the weatherwhisper.py script to launch the WeatherWhisper application.


# Base Code - Fetch Weather Data with OpenWeatherMap API
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

Please note that this base code is intended to demonstrate how to fetch weather data using the OpenWeatherMap API using the requests library. For the full functionality and GUI application, you can refer to the WeatherWhisper project provided in this repository.

If you have any further questions or need more assistance, feel free to ask!

## The explanation
I wanted to provide a step-by-step explanation of the code:

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

Please note (i know this is the second time i've said it) that to run this code successfully, you need to have a valid API key from OpenWeatherMap and the requests library installed in your Python environment. You can install the requests library using the following command:

```bash
pip install requests
```


# config.ini - Configuration File for Weather Whisper
The config.ini file plays a crucial role in the WeatherWhisper application, as it securely stores the API key required to access the OpenWeatherMap API. This configuration file ensures that the sensitive API key remains separate from the application's code, enhancing security and maintainability.

### purpose
The purpose of the config.ini file is to provide a centralized location for storing configuration parameters and settings that can be easily accessed and modified without altering the application's source code. In the case of WeatherWhisper, it serves as a container for the API key required to make requests to the OpenWeatherMap API.

### How to use
When setting up WeatherWhisper for the first time, the user needs to obtain their personal API key from the OpenWeatherMap website. Once obtained, the user must open the config.ini file with a text editor and replace the placeholder "your_api_key_here" with their actual API key. It is crucial to ensure that the API key is kept confidential and not shared with others, as it grants access to the OpenWeatherMap API under the user's account.


### Enhancing Security
By storing the API key in the config.ini file, WeatherWhisper avoids hardcoding sensitive information directly into the source code. This practice enhances security by reducing the risk of accidental exposure of the API key or unwanted disclosure when sharing code repositories with other developers.

### Conclusion
The config.ini file is a vital component of WeatherWhisper, providing a safe and convenient way to store the API key necessary for accessing real-time weather data from the OpenWeatherMap API. By using this configuration file, WeatherWhisper demonstrates best practices for secure and configurable application development.


# About the Author
WeatherWhisper was developed by Yanni X. I created this project to practice my Python skills and build a useful weather forecast tool for everyone to enjoy. I hope you find it helpful and that you have fun using it!

If you have any questions, feedback, or issues, don't hesitate to reach out. Enjoy your weather whispering experience! 😊

<sub>WeatherWhisper is a personal project and not affiliated with OpenWeatherMap. Please review the OpenWeatherMap API terms and conditions when using the application.</sub>


# The end 
Thank you for exploring Weather Whisper - Your Weather Forecast Assistant! 🌤️

Weather Whisper was designed with simplicity and convenience in mind, empowering you to effortlessly access real-time weather data for any city worldwide. With its user-friendly interface, switchable temperature units, and robust error handling, WeatherWhisper provides an enjoyable weather forecasting experience.

Throughout this project, we've learned how to interact with external APIs, securely store configuration settings, and build an intuitive GUI using tkinter. It has been a journey of exploration, growth, and creating a useful tool to keep you informed about the weather with just a few clicks.

We welcome your feedback and contributions to make WeatherWhisper even better. Your valuable insights and contributions are essential in shaping the future of this project and making it a valuable resource for weather enthusiasts worldwide.

As we conclude this project, we hope that WeatherWhisper has brought a touch of sunshine into your life, keeping you informed and prepared for whatever the weather may bring. Happy weather whispering! ☀️🌧️❄️

Until we meet again,
Yanni X.
