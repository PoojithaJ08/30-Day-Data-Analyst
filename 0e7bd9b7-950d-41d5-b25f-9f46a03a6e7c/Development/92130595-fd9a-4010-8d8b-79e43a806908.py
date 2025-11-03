import pandas as pd
import numpy as np

# Winsorize extreme values at P99.5 per product-store combination
winsorized_df = cleaning_df.copy()

# Calculate P99.5 for qty and net_sales by product_id and store_id
winsorize_stats = winsorized_df.groupby(['product_id', 'store_id']).agg({
    'qty': lambda x: x.quantile(0.995) if len(x) > 0 else np.nan,
    'net_sales': lambda x: x.quantile(0.995) if len(x) > 0 else np.nan
}).reset_index()

winsorize_stats.columns = ['product_id', 'store_id', 'qty_p995', 'net_sales_p995']

# Merge the P99.5 values back to the main dataframe
winsorized_df = winsorized_df.merge(winsorize_stats, on=['product_id', 'store_id'], how='left')

# Create DQ flags for extreme values before capping
winsorized_df['flag_extreme_qty'] = (winsorized_df['qty'] > winsorized_df['qty_p995'])
winsorized_df['flag_extreme_sales'] = (winsorized_df['net_sales'] > winsorized_df['net_sales_p995'])

# Count extreme values
extreme_qty_count = winsorized_df['flag_extreme_qty'].sum()
extreme_sales_count = winsorized_df['flag_extreme_sales'].sum()

# Cap extreme values at P99.5
winsorized_df['qty'] = np.where(
    winsorized_df['qty'] > winsorized_df['qty_p995'],
    winsorized_df['qty_p995'],
    winsorized_df['qty']
)

winsorized_df['net_sales'] = np.where(
    winsorized_df['net_sales'] > winsorized_df['net_sales_p995'],
    winsorized_df['net_sales_p995'],
    winsorized_df['net_sales']
)

# Drop temporary columns
winsorized_df = winsorized_df.drop(['qty_p995', 'net_sales_p995'], axis=1)

print(f"Winsorized extreme values at P99.5 per product-store")
print(f"  - Extreme qty capped: {extreme_qty_count}")
print(f"  - Extreme sales capped: {extreme_sales_count}")
print(f"Total rows: {len(winsorized_df)}")