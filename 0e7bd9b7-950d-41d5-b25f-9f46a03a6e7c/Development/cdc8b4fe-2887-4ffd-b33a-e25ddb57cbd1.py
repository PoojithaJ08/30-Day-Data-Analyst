import pandas as pd

# Verify store reference
stores_df = pd.read_csv('data/raw/stores/store_reference.csv')

# Check required columns
required_cols = ['store_id', 'region_id', 'lat', 'lon']
cols_present = all(col in stores_df.columns for col in required_cols)

print(f'✓ Store reference loaded: {len(stores_df)} stores')
print(f'✓ Required columns present: {cols_present}')
print(f'✓ Columns: {list(stores_df.columns)}')