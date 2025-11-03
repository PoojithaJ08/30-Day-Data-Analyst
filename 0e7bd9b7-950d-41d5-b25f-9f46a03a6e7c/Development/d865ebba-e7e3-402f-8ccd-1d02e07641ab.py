import os

# Create directory structure
os.makedirs('data/raw/wx', exist_ok=True)

# Save to Parquet
output_path = 'data/raw/wx/weather_data.parquet'
weather_df.to_parquet(output_path, index=False)

print(f"Saved {len(weather_df)} weather records to {output_path}")