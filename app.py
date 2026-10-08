import os

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request

# Load variables from the .env file into the environment
load_dotenv()

app = Flask(__name__)

API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """
    Fetch current weather for a city from OpenWeatherMap.
    Returns a tuple: (weather_data, error_message).
    One of the two is always None.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return None, "API key not found. Please add OPENWEATHER_API_KEY to your .env file."

    params = {"q": city, "appid": api_key}

    try:
        response = requests.get(API_URL, params=params, timeout=10)
    except requests.exceptions.Timeout:
        return None, "The request timed out. Please try again."
    except requests.exceptions.ConnectionError:
        return None, "Could not connect to the internet. Please check your connection."
    except requests.exceptions.RequestException:
        return None, "Something went wrong while contacting the weather service."

    if response.status_code == 200:
        try:
            data = response.json()
            temp_kelvin = data["main"]["temp"]
            weather = {
                "city": data["name"],
                "country": data["sys"].get("country", ""),
                # API returns Kelvin by default, so convert to Celsius
                "temperature": round(temp_kelvin - 273.15, 1),
                "humidity": data["main"]["humidity"],
                # API gives m/s; convert to km/h
                "wind_speed": round(data["wind"]["speed"] * 3.6, 1),
                "condition": data["weather"][0]["description"].title(),
                "icon": data["weather"][0]["icon"],
            }
            return weather, None
        except (ValueError, KeyError, IndexError):
            return None, "Received unexpected data from the weather service."

    if response.status_code == 404:
        return None, f'City "{city}" was not found. Please check the spelling and try again.'
    if response.status_code == 401:
        return None, "Invalid API key. Check your .env file (new keys can take up to 2 hours to activate)."
    if response.status_code == 429:
        return None, "Too many requests. Please wait a moment and try again."

    return None, f"Weather service error (code {response.status_code}). Please try again later."


@app.route("/")
def home():
    city = request.args.get("city")  # None when the page is first opened
    weather = None
    error = None

    if city is not None:
        city = city.strip()
        if not city:
            error = "Please enter a city name."
        else:
            weather, error = get_weather(city)

    return render_template("index.html", weather=weather, error=error, city=city or "")


if __name__ == "__main__":
    app.run(debug=True)
