import pandas as pd
import os

# Create directory structure
os.makedirs('data/raw/catalog', exist_ok=True)

# Create sample product catalog data
product_catalog = pd.DataFrame({
    'product_id': [f'P{str(i).zfill(4)}' for i in range(1, 101)],
    'category': ['Electronics', 'Clothing', 'Home', 'Sports', 'Books'] * 20,
    'subcategory': ['Phones', 'Shirts', 'Furniture', 'Equipment', 'Fiction'] * 20,
    'brand': ['BrandA', 'BrandB', 'BrandC', 'BrandD', 'BrandE'] * 20,
    'uom': ['each', 'each', 'each', 'each', 'each'] * 20
})

# Save to CSV
catalog_path = 'data/raw/catalog/product_catalog.csv'
product_catalog.to_csv(catalog_path, index=False)

print(f'Product catalog saved: {len(product_catalog)} products')
print(f'Location: {catalog_path}')