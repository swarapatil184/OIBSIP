# 🌤️ Basic Weather App (CLI)

A beginner-friendly **command-line weather application** built with Python.
This app fetches real-time weather data for any city using the **Open-Meteo API** — no API key required.



##  Features

* 🌍 Search weather by city name
* 🌡️ Displays temperature in °C and °F
* 💧 Shows humidity levels
* 🌬️ Displays wind speed
* 🌤️ Human-readable weather conditions (with emojis)
* 💡 Smart weather tips based on conditions
* ❌ Handles invalid city names and network errors gracefully
* 🔁 Interactive menu for repeated use

---

## 🛠️ Technologies Used

* Python 3
* `urllib` (for API requests)
* `json` (for parsing API response)
* Open-Meteo API (free weather data)

---

##  How to Run

1. Clone or download this repository
2. Navigate to the project folder
3. Run the script:

```bash id="run123"
python weather_app.py
```

---

## 🧪 Example Usage

```id="example456"
=============================================
   🌤️  Basic Weather App  🌤️
=============================================

Options:
  1. Check weather for a city
  2. Exit

Enter your choice (1 or 2): 1
Enter city name: Mumbai

=============================================
  🌍 Weather for Mumbai, India
=============================================
  Condition   : Partly cloudy ⛅
  Temperature : 32°C  (89.6°F)
  Humidity    : 78%
  Wind Speed  : 18 km/h
=============================================


##  How It Works

1. **City Search**
   Converts the city name into geographic coordinates (latitude & longitude) using the Open-Meteo Geocoding API.

2. **Weather Fetching**
   Uses coordinates to request current weather data from Open-Meteo.

3. **Display Output**
   Shows formatted weather information along with helpful tips.

---

## 🌦️ Weather Conditions Mapping

The app translates Open-Meteo weather codes into readable descriptions:

| Code  | Description             |
| ----- | ----------------------- |
| 0     | Clear sky ☀️            |
| 1–3   | Cloudy variations 🌤️☁️ |
| 51–65 | Rain 🌧️                |
| 71–75 | Snow 🌨️❄️              |
| 80–82 | Rain showers 🌦️        |
| 95–99 | Thunderstorm ⛈️         |

---

##  Limitations

* Requires internet connection
* Only shows **current weather** (no forecast)
* City matching depends on API accuracy

---

## 🚀 Future Improvements

* Add 7-day weather forecast
* Add support for GPS/location detection
* Create GUI version (Tkinter / PyQt)
* Add unit selection (Celsius/Fahrenheit toggle)
* Save search history
* Improve weather tips logic

---

## 📁 Project Structure

```id="structure789"
weather_app.py   # Main application
README.md        # Documentation
```







---
