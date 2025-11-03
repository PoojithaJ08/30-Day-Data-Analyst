import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pathlib import Path
from datetime import datetime

# Configuration
chunk_size = 100000  # Process 100k rows at a time
required_columns = ['po_id', 'po_line', 'supplier_id', 'route', 'ship_ts', 'eta_ts', 'receipt_ts', 'qty', 'cost', 'defect_flag']

total_rows_processed = 0
chunks_processed = 0

if csv_exists:
    # Process CSV in chunks
    for chunk_idx, chunk_df in enumerate(pd.read_csv(csv_path, chunksize=chunk_size)):
        # Extract required columns
        shipment_chunk = chunk_df[required_columns].copy()
        
        # Parse ship_ts to extract ship_date for partitioning
        shipment_chunk['ship_date'] = pd.to_datetime(shipment_chunk['ship_ts']).dt.date
        
        # Group by ship_date and write partitioned parquet
        for ship_date, date_group in shipment_chunk.groupby('ship_date'):
            # Remove ship_date from the data before writing
            output_data = date_group.drop(columns=['ship_date'])
            
            # Create partition directory
            partition_dir = raw_shipment_path / f'ship_date={ship_date}'
            partition_dir.mkdir(parents=True, exist_ok=True)
            
            # Write parquet file (append mode)
            output_file = partition_dir / f'chunk_{chunk_idx}.parquet'
            output_data.to_parquet(output_file, index=False, engine='pyarrow')
        
        total_rows_processed += len(chunk_df)
        chunks_processed += 1
    
    print(f'✓ Processed {total_rows_processed} rows in {chunks_processed} chunks')
    print(f'✓ Data written to: {raw_shipment_path}')
else:
    print('⚠ Skipping processing - CSV not found')
    print('To run this pipeline, upload a CSV file named "shipments.csv" with the required columns')
