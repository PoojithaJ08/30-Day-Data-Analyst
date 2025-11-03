import pandas as pd
import os

# Verify weather data
wx_file_path = 'data/raw/wx/weather_data.parquet'
if os.path.exists(wx_file_path):
    verify_wx_df = pd.read_parquet(wx_file_path)
    print(f"✓ WEATHER: {len(verify_wx_df)} records")
    print(f"  Columns: {list(verify_wx_df.columns)}")
    print(f"  Date range: {verify_wx_df['date'].min()} to {verify_wx_df['date'].max()}")
else:
    print("✗ WEATHER: File not found")