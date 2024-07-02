import requests
import matplotlib.pyplot as plt

def get_weather(city):
    # Open-Meteo API endpoint for weather data
    BASE_URL = 'https://api.open-meteo.com/v1/forecast'
    
    # Coordinates for the city (you can use a geocoding API to get these)
    coordinates = {
        'London': {'latitude': 51.5074, 'longitude': -0.1278}
    }
    
    if city not in coordinates:
        print(f"Coordinates for city '{city}' not found.")
        return None

    latitude = coordinates[city]['latitude']
    longitude = coordinates[city]['longitude']
    
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'daily': 'temperature_2m_min,temperature_2m_max',
        'timezone': 'Europe/London'
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None

def plot_weather(city, weather_data):
    dates = weather_data['daily']['time']
    min_temps = weather_data['daily']['temperature_2m_min']
    max_temps = weather_data['daily']['temperature_2m_max']

    plt.plot(dates, min_temps, label='Min Temp (°C)')
    plt.plot(dates, max_temps, label='Max Temp (°C)')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Weather Forecast for {city}')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

city = 'London'
weather_data = get_weather(city)

if weather_data:
    plot_weather(city, weather_data)
else:
    print("Failed to get weather data")
