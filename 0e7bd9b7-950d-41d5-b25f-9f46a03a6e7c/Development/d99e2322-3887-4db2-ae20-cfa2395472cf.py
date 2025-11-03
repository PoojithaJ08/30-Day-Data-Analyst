import pandas as pd

# Verify product catalog
catalog_df = pd.read_csv('data/raw/catalog/product_catalog.csv')

# Check required columns
required_cols = ['product_id', 'category', 'subcategory', 'brand', 'uom']
cols_present = all(col in catalog_df.columns for col in required_cols)

print(f'✓ Product catalog loaded: {len(catalog_df)} products')
print(f'✓ Required columns present: {cols_present}')
print(f'✓ Columns: {list(catalog_df.columns)}')