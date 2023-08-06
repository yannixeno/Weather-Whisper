import tkinter as tk
import requests
import re
import configparser

API_KEY = ""
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
TEMP_UNIT_CELSIUS = "C"
TEMP_UNIT_FAHRENHEIT = "F"

def load_api_key():
    global API_KEY
    config = configparser.ConfigParser()
    config.read("config.ini")
    API_KEY = config.get("WeatherWhisper", "API_KEY")

def get_weather():
    city = city_entry.get()

    if not city:
        weather_label.config(text="Please enter a city name.")
        temp_label.config(text="")
        feels_like_label.config(text="")
        return

    if not re.match("^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$", city):
        weather_label.config(text="Invalid city name. Please use alphabetic characters only.")
        temp_label.config(text="")
        feels_like_label.config(text="")
        return

    try:
        request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
        response = requests.get(request_url)

        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            temperature_celsius = round(data["main"]["temp"] - 273.15)
            feels_like_celsius = round(data["main"]["feels_like"] - 273.15)
            temperature_fahrenheit = round(data["main"]["temp"] * 1.8 - 459.67)
            feels_like_fahrenheit = round(data["main"]["feels_like"] * 1.8 - 459.67)

            if temperature_unit == TEMP_UNIT_CELSIUS:
                temperature = temperature_celsius
                feels_like = feels_like_celsius
                unit_label.config(text="Temperature Units: Celsius")
            else:
                temperature = temperature_fahrenheit
                feels_like = feels_like_fahrenheit
                unit_label.config(text="Temperature Units: Fahrenheit")

            weather_label.config(text="Weather: " + weather)
            temp_label.config(text="Temperature: " + str(temperature) + " °" + temperature_unit)
            feels_like_label.config(text="It Feels Like: " + str(feels_like) + " °" + temperature_unit)
        else:
            weather_label.config(text="Error: Unable to fetch weather data.")
            temp_label.config(text="")
            feels_like_label.config(text="")
    except requests.exceptions.RequestException as e:
        weather_label.config(text="Error: Unable to connect to the weather service.")
        temp_label.config(text="")
        feels_like_label.config(text="")

def toggle_units():
    global temperature_unit
    if temperature_unit == TEMP_UNIT_CELSIUS:
        temperature_unit = TEMP_UNIT_FAHRENHEIT
    else:
        temperature_unit = TEMP_UNIT_CELSIUS
    get_weather()

# Create the GUI window
root = tk.Tk()
root.title("WeatherWhisper")
root.geometry("800x500")
root.configure(bg="#18191a")

# Load API key from configuration file
load_api_key()

# Title label
title_label = tk.Label(root, text="Weather Whisper", bg="#18191a", fg="white", font=("Arial", 40, "bold"))
title_label.pack(pady=20)

# Center Frame to stack widgets vertically in the center
center_frame = tk.Frame(root, bg="#18191a")
center_frame.pack(expand=True, anchor="center")

# Input field for city
city_entry = tk.Entry(center_frame, bg="#18191a", fg="white", insertbackground="white", width=30, font=("Arial", 16))
city_entry.pack(pady=10, anchor="center")

# Button to get weather
get_weather_button = tk.Button(center_frame, text="Get Weather", command=get_weather, bg="#18191a", fg="white", font=("Arial", 14, "bold"))
get_weather_button.pack(pady=5, anchor="center")

# Labels to display weather information
label_font = ("Arial", 18)
weather_label = tk.Label(center_frame, text="", bg="#18191a", fg="white", font=label_font)
weather_label.pack(pady=5, anchor="center")
temp_label = tk.Label(center_frame, text="", bg="#18191a", fg="white", font=label_font)
temp_label.pack(pady=5, anchor="center")
feels_like_label = tk.Label(center_frame, text="", bg="#18191a", fg="white", font=label_font)
feels_like_label.pack(pady=5, anchor="center")

# Temperature Units Dropdown
temperature_unit = TEMP_UNIT_CELSIUS  # Initial units in Celsius
unit_label = tk.Label(root, text="Temperature Units: Celsius", bg="#18191a", fg="white")
unit_label.pack(side="bottom", anchor="se", pady=5)
units_button = tk.Button(root, text="Switch Units", command=toggle_units, bg="#18191a", fg="white")
units_button.pack(side="bottom", anchor="se")

# Made by label
made_by_label = tk.Label(root, text="Made by Yanni X", bg="#18191a", fg="white")
made_by_label.pack(side="bottom", anchor="sw", padx=5, pady=5)

# Run the GUI event loop
root.mainloop()
