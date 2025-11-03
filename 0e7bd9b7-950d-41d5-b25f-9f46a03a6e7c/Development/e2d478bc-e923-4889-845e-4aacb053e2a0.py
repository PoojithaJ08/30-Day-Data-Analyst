import pandas as pd
import os
import numpy as np

# Create directory structure
os.makedirs('data/raw/stores', exist_ok=True)

# Create sample store reference data
np.random.seed(42)
store_reference = pd.DataFrame({
    'store_id': [f'S{str(i).zfill(4)}' for i in range(1, 51)],
    'region_id': [f'R{str((i % 5) + 1).zfill(2)}' for i in range(1, 51)],
    'lat': np.random.uniform(25.0, 49.0, 50),  # US latitude range
    'lon': np.random.uniform(-125.0, -65.0, 50)  # US longitude range
})

# Save to CSV
stores_path = 'data/raw/stores/store_reference.csv'
store_reference.to_csv(stores_path, index=False)

print(f'Store reference saved: {len(store_reference)} stores')
print(f'Location: {stores_path}')