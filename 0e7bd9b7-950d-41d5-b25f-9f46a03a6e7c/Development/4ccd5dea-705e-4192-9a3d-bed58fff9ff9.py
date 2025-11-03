import pandas as pd
from pathlib import Path

# Ensure output directory exists
output_dir = Path('data/raw/pos')
output_dir.mkdir(parents=True, exist_ok=True)

# Convert txn_date to datetime for proper partitioning
pos_raw_df['txn_date'] = pd.to_datetime(pos_raw_df['txn_date'])

# Group by txn_date and save to partitioned Parquet files
partition_counts = {}
for date_val, group_df in pos_raw_df.groupby('txn_date'):
    # Format date as YYYY-MM-DD for partition folder
    date_str = date_val.strftime('%Y-%m-%d')
    partition_dir = output_dir / f'txn_date={date_str}'
    partition_dir.mkdir(exist_ok=True)
    
    # Save partition as Parquet
    partition_file = partition_dir / 'data.parquet'
    group_df.to_parquet(partition_file, index=False, engine='pyarrow')
    
    partition_counts[date_str] = len(group_df)

# Log results
total_rows = sum(partition_counts.values())
print(f"Saved {total_rows} rows across {len(partition_counts)} partitions")
for date_str, row_count in sorted(partition_counts.items()):
    print(f"  {date_str}: {row_count} rows")