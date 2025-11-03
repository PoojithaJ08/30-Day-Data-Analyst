import pandas as pd
import os

# Verify FX data
fx_file_path = 'data/raw/fx/fx_data.parquet'
if os.path.exists(fx_file_path):
    verify_fx_df = pd.read_parquet(fx_file_path)
    print(f"✓ FX: {len(verify_fx_df)} records")
    print(f"  Columns: {list(verify_fx_df.columns)}")
    print(f"  Date range: {verify_fx_df['date'].min()} to {verify_fx_df['date'].max()}")
else:
    print("✗ FX: File not found")