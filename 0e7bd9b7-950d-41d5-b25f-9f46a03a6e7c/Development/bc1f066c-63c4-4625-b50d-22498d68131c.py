import pandas as pd
from pathlib import Path

# Verify idempotency by re-reading the exported data
verify_clean_output_dir = Path('data/clean/pos')

# Read all partitions
verify_all_partitions = []
for partition_path in sorted(verify_clean_output_dir.glob('txn_date=*/data.parquet')):
    verify_df = pd.read_parquet(partition_path)
    verify_all_partitions.append(verify_df)

# Combine all partitions
verify_combined_df = pd.concat(verify_all_partitions, ignore_index=True)

# Verify row count matches
verify_row_match = len(verify_combined_df) == total_export_rows

# Verify all required columns are present
required_clean_columns = [
    'txn_id', 'store_id', 'product_id', 'txn_date', 'txn_ts',
    'qty', 'net_sales', 'promo_flag', 'payment_type',
    '_validation_status', '_validation_errors',
    'flag_extreme_qty', 'flag_extreme_sales', 'flag_missing_dim',
    'has_dq_issue', 'flag_negative_sales', 'unit_price'
]
verify_cols_present = all(col in verify_combined_df.columns for col in required_clean_columns)

print("=" * 70)
print("IDEMPOTENCY VERIFICATION")
print("=" * 70)
print(f"\n✅ Verification Results:")
print(f"  Partitions Found: {len(verify_all_partitions)}")
print(f"  Total Rows Read: {len(verify_combined_df)}")
print(f"  Expected Rows: {total_export_rows}")
print(f"  Row Count Match: {'✓ PASS' if verify_row_match else '✗ FAIL'}")
print(f"  All Columns Present: {'✓ PASS' if verify_cols_present else '✗ FAIL'}")
print(f"\n📋 Columns in Exported Data ({len(verify_combined_df.columns)}):")
print(f"  {', '.join(verify_combined_df.columns[:10])}")
if len(verify_combined_df.columns) > 10:
    print(f"  {', '.join(verify_combined_df.columns[10:])}")
print("=" * 70)