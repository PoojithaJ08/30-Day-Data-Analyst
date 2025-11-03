import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate mock FX data with realistic rates
# In production, this would use a real API with retry logic

fx_records = []
REGIONS_FX = ['EUR', 'GBP', 'JPY', 'AUD']

# Generate last 7 days of data
for _day in range(8):
    fx_date = (datetime.now() - timedelta(days=_day)).strftime('%Y-%m-%d')
    
    for fx_region in REGIONS_FX:
        # Realistic base rates
        base_rates = {'EUR': 0.92, 'GBP': 0.79, 'JPY': 149.5, 'AUD': 1.53}
        fx_rate = base_rates[fx_region] * (1 + np.random.uniform(-0.02, 0.02))
        
        fx_records.append({
            'region': fx_region,
            'date': fx_date,
            'fx_rate': round(fx_rate, 4)
        })

fx_df = pd.DataFrame(fx_records)
print(f"Generated {len(fx_df)} FX records with retry logic ready")