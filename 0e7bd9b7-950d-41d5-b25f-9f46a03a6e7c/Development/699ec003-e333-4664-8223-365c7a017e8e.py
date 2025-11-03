import requests
import pandas as pd
from datetime import datetime, timedelta
import os
import time

# Configuration
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"
REGIONS = {
    'north': {'lat': 51.5074, 'lon': -0.1278},
    'south': {'lat': 40.7128, 'lon': -74.0060},
    'east': {'lat': 35.6762, 'lon': 139.6503},
    'west': {'lat': 37.7749, 'lon': -122.4194}
}

# Fetch weather data with retry logic
weather_records = []

for wx_region_name, wx_coords in REGIONS.items():
    wx_max_retries = 3
    wx_retry_count = 0
    wx_success = False
    
    while wx_retry_count < wx_max_retries and not wx_success:
        try:
            wx_params = {
                'latitude': wx_coords['lat'],
                'longitude': wx_coords['lon'],
                'daily': 'temperature_2m_mean,precipitation_sum,wind_speed_10m_max',
                'past_days': 7,
                'timezone': 'auto'
            }
            
            wx_response = requests.get(WEATHER_API_URL, params=wx_params, timeout=10)
            wx_response.raise_for_status()
            
            wx_data = wx_response.json()
            wx_daily = wx_data['daily']
            
            for _wx_i in range(len(wx_daily['time'])):
                weather_records.append({
                    'region': wx_region_name,
                    'date': wx_daily['time'][_wx_i],
                    'temp_avg': wx_daily['temperature_2m_mean'][_wx_i],
                    'precip': wx_daily['precipitation_sum'][_wx_i],
                    'wind': wx_daily['wind_speed_10m_max'][_wx_i]
                })
            
            wx_success = True
            
        except Exception as e:
            wx_retry_count += 1
            if wx_retry_count < wx_max_retries:
                time.sleep(2 ** wx_retry_count)
            else:
                print(f"Failed to fetch weather for {wx_region_name} after {wx_max_retries} retries: {e}")

weather_df = pd.DataFrame(weather_records)
print(f"Fetched {len(weather_df)} weather records from API")