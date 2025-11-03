import os
from pathlib import Path

# Verify output structure
if csv_exists and total_rows_processed > 0:
    # List partition directories
    partitions = sorted([d.name for d in raw_shipment_path.iterdir() if d.is_dir()])
    
    print(f'✓ Total rows processed: {total_rows_processed:,}')
    print(f'✓ Chunks processed: {chunks_processed}')
    print(f'✓ Date partitions created: {len(partitions)}')
    print(f'✓ Output directory: {raw_shipment_path}')
    
    if partitions:
        print(f'\nPartitions: {", ".join(partitions[:5])}{"..." if len(partitions) > 5 else ""}')
else:
    print('⚠ No data processed yet')
    print('\nPipeline is ready to process shipment data.')
    print('Upload a CSV file named "shipments.csv" with these columns:')
    print('  - po_id, po_line, supplier_id, route')
    print('  - ship_ts, eta_ts, receipt_ts')
    print('  - qty, cost, defect_flag')
