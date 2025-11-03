import pandas as pd
import os

# Verify fuel data
fuel_file_path = 'data/raw/fuel/fuel_data.parquet'
if os.path.exists(fuel_file_path):
    verify_fuel_df = pd.read_parquet(fuel_file_path)
    print(f"✓ FUEL: {len(verify_fuel_df)} records")
    print(f"  Columns: {list(verify_fuel_df.columns)}")
    print(f"  Date range: {verify_fuel_df['date'].min()} to {verify_fuel_df['date'].max()}")
else:
    print("✗ FUEL: File not found")