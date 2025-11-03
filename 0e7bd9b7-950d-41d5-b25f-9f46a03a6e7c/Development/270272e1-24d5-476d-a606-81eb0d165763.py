import os

# Create directory structure
os.makedirs('data/raw/fuel', exist_ok=True)

# Save to Parquet
fuel_output_path = 'data/raw/fuel/fuel_data.parquet'
fuel_df.to_parquet(fuel_output_path, index=False)

print(f"Saved {len(fuel_df)} fuel price records to {fuel_output_path}")