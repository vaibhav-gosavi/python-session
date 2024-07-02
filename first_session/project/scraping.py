import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

URL = 'https://forecast.weather.gov/MapClick.php?textField1=38.4247341&textField2=-86.9624086#.X5F_jS2ZNQI'
response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Scraping the period names (days of the week)
    periods = [period.get_text() for period in soup.select('.tombstone-container .period-name')]
    
    # Scraping the short descriptions
    short_descs = [desc.get_text() for desc in soup.select('.tombstone-container .short-desc')]
    
    # Scraping the temperatures
    temps = [temp.get_text() for temp in soup.select('.tombstone-container .temp')]
    
    # Creating a DataFrame
    weather_data = pd.DataFrame({
        'Period': periods,
        'Short Description': short_descs,
        'Temperature': temps
    })
    
    # Save to CSV
    weather_data.to_csv('weather_forecast.csv', index=False)
    
    # Print scraped data
    print(weather_data)
    
    # Visualize Data
    plt.figure(figsize=(10, 5))
    plt.plot(weather_data['Period'], weather_data['Temperature'], marker='o')
    plt.xlabel('Period')
    plt.ylabel('Temperature')
    plt.title('7-Day Weather Forecast')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Failed to retrieve the web page")
