import pandas as pd
from pathlib import Path

# Define output path for cleaned POS data
clean_output_dir = Path('data/clean/pos')
clean_output_dir.mkdir(parents=True, exist_ok=True)

# Convert txn_date to datetime if it's not already
export_df = final_cleaned_df.copy()
export_df['txn_date'] = pd.to_datetime(export_df['txn_date'])

# Group by txn_date for partitioning
clean_partition_counts = {}
export_file_sizes = {}
total_export_rows = 0

for txn_date_val, date_group_df in export_df.groupby(export_df['txn_date'].dt.date):
    # Create partition directory
    date_str_export = str(txn_date_val)
    partition_export_dir = clean_output_dir / f'txn_date={date_str_export}'
    partition_export_dir.mkdir(parents=True, exist_ok=True)
    
    # Write parquet file (idempotent - overwrites existing)
    partition_export_file = partition_export_dir / 'data.parquet'
    date_group_df.to_parquet(partition_export_file, index=False, engine='pyarrow')
    
    # Track metrics
    export_row_count = len(date_group_df)
    clean_partition_counts[date_str_export] = export_row_count
    export_file_sizes[date_str_export] = partition_export_file.stat().st_size
    total_export_rows += export_row_count

print(f'✅ Exported {total_export_rows} rows to {clean_output_dir}')
print(f'📁 Created {len(clean_partition_counts)} partitions')
print(f'🗂️  Partitions: {list(clean_partition_counts.keys())}')