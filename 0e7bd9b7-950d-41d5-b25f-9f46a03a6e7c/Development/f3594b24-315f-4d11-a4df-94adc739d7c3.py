import pandas as pd
import numpy as np

# Start with validated_df from validation
cleaning_df = validated_df.copy()

# Remove impossible values: qty < 0 or net_sales < 0
# Initialize DQ flags
cleaning_df['flag_negative_qty'] = (cleaning_df['qty'] < 0)
cleaning_df['flag_negative_sales'] = (cleaning_df['net_sales'] < 0)

# Count impossible values before removal
negative_qty_count = cleaning_df['flag_negative_qty'].sum()
negative_sales_count = cleaning_df['flag_negative_sales'].sum()

# Remove rows with impossible values
before_count = len(cleaning_df)
cleaning_df = cleaning_df[~(cleaning_df['flag_negative_qty'] | cleaning_df['flag_negative_sales'])]
after_count = len(cleaning_df)

# Drop the temporary flags since we removed these rows
cleaning_df = cleaning_df.drop(['flag_negative_qty', 'flag_negative_sales'], axis=1)

print(f"Removed {before_count - after_count} impossible rows")
print(f"  - Negative qty: {negative_qty_count}")
print(f"  - Negative sales: {negative_sales_count}")
print(f"Remaining rows: {after_count}")