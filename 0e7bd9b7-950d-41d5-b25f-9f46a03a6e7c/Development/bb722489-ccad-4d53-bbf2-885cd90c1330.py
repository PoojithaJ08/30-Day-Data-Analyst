import os

# Create directory structure
os.makedirs('data/raw/fx', exist_ok=True)

# Save to Parquet
fx_output_path = 'data/raw/fx/fx_data.parquet'
fx_df.to_parquet(fx_output_path, index=False)

print(f"Saved {len(fx_df)} FX records to {fx_output_path}")