import pandas as pd
import sqlite3
from pathlib import Path

# Create connection (using mock database for demonstration)
# In production, replace with actual database connection
conn = sqlite3.connect(':memory:')

# Create sample POS transactions table for demonstration
sample_data = pd.DataFrame({
    'txn_id': [1, 2, 3, 4, 5],
    'store_id': [101, 102, 101, 103, 102],
    'product_id': [501, 502, 503, 501, 502],
    'txn_date': ['2024-01-15', '2024-01-15', '2024-01-16', '2024-01-16', '2024-01-17'],
    'txn_ts': ['2024-01-15 10:30:00', '2024-01-15 11:45:00', '2024-01-16 09:15:00', '2024-01-16 14:30:00', '2024-01-17 16:20:00'],
    'qty': [2, 1, 3, 1, 2],
    'net_sales': [29.98, 15.99, 44.97, 14.99, 31.98],
    'promo_flag': [0, 1, 0, 0, 1],
    'payment_type': ['credit', 'debit', 'cash', 'credit', 'debit']
})
sample_data.to_sql('pos_transactions', conn, if_exists='replace', index=False)

# Extract POS data with required columns
query = """
SELECT 
    txn_id,
    store_id,
    product_id,
    txn_date,
    txn_ts,
    qty,
    net_sales,
    promo_flag,
    payment_type
FROM pos_transactions
ORDER BY txn_date, txn_ts
"""

pos_raw_df = pd.read_sql_query(query, conn)
conn.close()

print(f"Extracted {len(pos_raw_df)} POS transactions")
print(f"Date range: {pos_raw_df['txn_date'].min()} to {pos_raw_df['txn_date'].max()}")