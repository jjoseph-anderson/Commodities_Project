print("Hello")

print(3+3)

import pandas as pd
import requests
from datetime import datetime



latitude = 40.71   # New York City
longitude = -74.01
start_date = "2024-01-01"
end_date = "2024-12-31"

url = (
    f"https://archive-api.open-meteo.com/v1/archive?"
    f"latitude={latitude}&longitude={longitude}"
    f"&start_date={start_date}&end_date={end_date}"
    "&daily=temperature_2m_max,temperature_2m_min"
    "&timezone=America%2FNew_York"
)

response = requests.get(url)
data = response.json()

# Step 4: Convert to DataFrame
df = pd.DataFrame(data['daily'])
df['date'] = pd.to_datetime(df['time'])
df['t_avg'] = (df['temperature_2m_max'] + df['temperature_2m_min']) / 2

print(df)

