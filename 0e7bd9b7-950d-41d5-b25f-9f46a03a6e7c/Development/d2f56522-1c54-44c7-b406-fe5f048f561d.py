import pandas as pd
import os
from pathlib import Path

# Define paths
raw_shipment_path = Path('data/raw/ship')
raw_shipment_path.mkdir(parents=True, exist_ok=True)

# CSV input path (assuming shipment data is in a file named shipments.csv)
csv_path = 'shipments.csv'

# Check if CSV exists
if os.path.exists(csv_path):
    csv_exists = True
    print(f'✓ Found CSV at: {csv_path}')
else:
    csv_exists = False
    print(f'✗ CSV not found at: {csv_path}')
    print('Expected columns: po_id, po_line, supplier_id, route, ship_ts, eta_ts, receipt_ts, qty, cost, defect_flag')
