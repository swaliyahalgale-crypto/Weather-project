Weather Application
Problem Statement
Create a simple web-based Weather Application using Python. The application should allow users to search for the current weather of a city and display the required weather information.
Assigned Feature Set
Feature Set A
Search weather by city
Display temperature
Display humidity
Display wind speed
Display weather condition
Features Implemented
Search the current weather by city name
Displays temperature in °C (converted from Kelvin)
Displays humidity (%)
Displays wind speed (km/h)
Displays weather condition with an icon
Handles empty input, invalid city names, invalid API key, API errors and internet connection errors
Loading message while searching
Responsive design for mobile and desktop
API key stored securely in an environment variable (not in the source code)
Technologies Used
Python 3
Flask (web framework)
Requests (to call the API)
python-dotenv (to load the API key from .env)
OpenWeatherMap API (real-time weather data)
HTML5 and CSS3
AI Tools Used
Claude (by Anthropic) was used to help generate and explain parts of the code.
Important AI Prompts / AI Usage
Claude/AI assistance was used for generating and understanding parts of the code. The main prompt given to Claude was to create a Flask-based Weather Application using the OpenWeatherMap API with the five mandatory features (search by city, temperature, humidity, wind speed, weather condition), proper error handling, a responsive HTML/CSS interface, API key stored in an environment variable, and a beginner-friendly explanation of each file.
After generation, I read and understood the code, ran the application locally, and tested all features myself (valid city, invalid city, empty input, and no internet connection) to verify that it works correctly.
Instructions to Run the Project
Install Python 3 from https://www.python.org/downloads/ (tick "Add Python to PATH").
Open the project folder in VS Code and open a terminal (Command Prompt).
Create a virtual environment:
python -m venv venv
Activate it:
venv\Scripts\activate
Install the requirements:
pip install -r requirements.txt
Copy .env.example to .env:
copy .env.example .env
Open .env and replace your_api_key_here with your OpenWeatherMap API key (free at https://openweathermap.org/api).
Run the app:
python app.py
Open http://127.0.0.1:5000 in your browser.
Screenshots of the Working Project
(Add your own screenshots here after running the project)
Home page: screenshots/home.png
Weather result for a valid city: screenshots/result.png
Error message for an invalid city: screenshots/error.png
Mobile view: screenshots/mobile.png
