import pandas as pd
import numpy as np

# Calculate unit_price = net_sales / qty where qty > 0
final_cleaned_df = dq_flagged_df.copy()

# Calculate unit price, handling division by zero
final_cleaned_df['unit_price'] = np.where(
    final_cleaned_df['qty'] > 0,
    final_cleaned_df['net_sales'] / final_cleaned_df['qty'],
    np.nan
)

# Count rows with unit_price calculated
unit_price_calculated = final_cleaned_df['unit_price'].notna().sum()
unit_price_null = final_cleaned_df['unit_price'].isna().sum()

print(f"Unit price calculation complete:")
print(f"  - Calculated: {unit_price_calculated} rows")
print(f"  - Null (qty=0): {unit_price_null} rows")
print(f"Total rows: {len(final_cleaned_df)}")