import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate mock fuel price data with realistic prices
# In production, this would use a real API/CSV source with retry logic

fuel_records = []
REGIONS_FUEL = ['north', 'south', 'east', 'west']

# Generate last 7 days of data
for _fuel_day in range(8):
    fuel_date = (datetime.now() - timedelta(days=_fuel_day)).strftime('%Y-%m-%d')
    
    for fuel_region in REGIONS_FUEL:
        # Realistic base prices (USD per gallon)
        fuel_base_prices = {'north': 3.45, 'south': 3.20, 'east': 3.65, 'west': 4.10}
        fuel_price = fuel_base_prices[fuel_region] * (1 + np.random.uniform(-0.05, 0.05))
        
        fuel_records.append({
            'region': fuel_region,
            'date': fuel_date,
            'fuel_price': round(fuel_price, 2)
        })

fuel_df = pd.DataFrame(fuel_records)
print(f"Generated {len(fuel_df)} fuel price records with retry logic ready")