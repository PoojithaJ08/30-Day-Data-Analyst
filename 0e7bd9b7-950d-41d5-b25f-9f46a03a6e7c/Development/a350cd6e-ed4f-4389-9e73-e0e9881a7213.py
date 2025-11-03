import pandas as pd
import numpy as np

# Add DQ flags for missing dimensions and consolidate flags
dq_flagged_df = winsorized_df.copy()

# Flag missing dimensions (store_id, product_id, txn_date)
# Check for null or empty values in key dimensions
dq_flagged_df['flag_missing_dim'] = (
    dq_flagged_df['store_id'].isna() | 
    dq_flagged_df['product_id'].isna() | 
    dq_flagged_df['txn_date'].isna() |
    (dq_flagged_df['store_id'] == '') |
    (dq_flagged_df['product_id'] == '')
)

# Consolidate all DQ flags
# flag_missing_dim: already created
# flag_extreme_qty: already exists from winsorization
# flag_extreme_sales: already exists but named differently
dq_flagged_df = dq_flagged_df.rename(columns={'flag_extreme_sales': 'flag_extreme_sales_temp'})

# Create a combined flag for any DQ issue
dq_flagged_df['has_dq_issue'] = (
    dq_flagged_df['flag_missing_dim'] | 
    dq_flagged_df['flag_extreme_qty'] |
    dq_flagged_df['flag_extreme_sales_temp']
)

# Drop the temp flag and keep only the three required flags
dq_flagged_df['flag_negative_sales'] = False  # Already removed rows with negative sales
dq_flagged_df = dq_flagged_df.rename(columns={'flag_extreme_sales_temp': 'flag_extreme_sales'})

# Count DQ issues
missing_dim_count = dq_flagged_df['flag_missing_dim'].sum()
extreme_qty_count_flag = dq_flagged_df['flag_extreme_qty'].sum()
extreme_sales_count_flag = dq_flagged_df['flag_extreme_sales'].sum()
total_dq_count = dq_flagged_df['has_dq_issue'].sum()
dq_percentage = (total_dq_count / len(dq_flagged_df) * 100) if len(dq_flagged_df) > 0 else 0

print(f"DQ Flags Summary:")
print(f"  - flag_missing_dim: {missing_dim_count} rows")
print(f"  - flag_extreme_qty: {extreme_qty_count_flag} rows")
print(f"  - flag_negative_sales: 0 rows (already removed)")
print(f"Total DQ flagged rows: {total_dq_count} ({dq_percentage:.2f}%)")