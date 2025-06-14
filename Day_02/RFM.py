import pandas as pd
import datetime as dt

# Load CSV with encoding fix
rfm = pd.read_csv("/Users/poojithakrishnajonnalagadda/Downloads/DATA ANALYST PROJECT/DAY_2/DATASET/data.csv", encoding='ISO-8859-1')

# Rename columns
rfm.columns = ['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country']

# Convert InvoiceDate to datetime
rfm['InvoiceDate'] = pd.to_datetime(rfm['InvoiceDate'])

# Filter out null CustomerIDs and canceled invoices
rfm = rfm[rfm['CustomerID'].notnull()]
rfm = rfm[~rfm['InvoiceNo'].astype(str).str.startswith('C')]

# Create TotalPrice column
rfm['TotalPrice'] = rfm['Quantity'] * rfm['UnitPrice']

# Set reference date for recency calculation
reference_date = dt.datetime(2011, 12, 10)

# Group by CustomerID to get RFM metrics
rfm_metrics = rfm.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (reference_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'TotalPrice': 'sum'
}).reset_index()

# Rename RFM columns
rfm_metrics.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

# Preview
print("RFM Metrics:")
print(rfm_metrics.head())

# Assign scores using quantiles
rfm_metrics['R_score'] = pd.qcut(rfm_metrics['Recency'], 4, labels=[4, 3, 2, 1]).astype(int)
rfm_metrics['F_score'] = pd.qcut(rfm_metrics['Frequency'].rank(method='first'), 4, labels=[1, 2, 3, 4]).astype(int)
rfm_metrics['M_score'] = pd.qcut(rfm_metrics['Monetary'].rank(method='first'), 4, labels=[1, 2, 3, 4]).astype(int)

# Combine into RFM Segment
rfm_metrics['RFM_Score'] = rfm_metrics['R_score'].astype(str) + rfm_metrics['F_score'].astype(str) + rfm_metrics['M_score'].astype(str)

# Define segments
def segment(x):
    if x == '444': return 'Champions'
    elif x[0] == '4': return 'Loyal Customers'
    elif x[1] == '4': return 'Frequent Buyers'
    elif x[2] == '4': return 'Big Spenders'
    elif x == '111': return 'Lost'
    elif x[0] == '1': return 'At Risk'
    else: return 'Others'

rfm_metrics['Segment'] = rfm_metrics['RFM_Score'].apply(segment)

# Preview
print("Segmented RFM Table:")
print(rfm_metrics[['CustomerID', 'Recency', 'Frequency', 'Monetary', 'RFM_Score', 'Segment']].head())

# Export the final RFM table
rfm_metrics.to_csv("Segmented_RFM.csv", index=False)
print("Segmented_RFM.csv exported successfully.")
