import pandas as pd

# Define POS schema validation rules as a dictionary
# This schema includes type coercion and validation rules for each column

pos_schema_definition = {
    'txn_id': {
        'dtype': 'str',
        'nullable': False,
        'description': 'Transaction ID'
    },
    'store_id': {
        'dtype': 'str',
        'nullable': False,
        'description': 'Store ID'
    },
    'product_id': {
        'dtype': 'str',
        'nullable': False,
        'description': 'Product ID'
    },
    'txn_date': {
        'dtype': 'datetime64[ns]',
        'nullable': False,
        'description': 'Transaction date'
    },
    'qty': {
        'dtype': 'int',
        'nullable': False,
        'min_value': 0,
        'description': 'Quantity sold (must be >= 0)'
    },
    'net_sales': {
        'dtype': 'float',
        'nullable': False,
        'min_value': 0.0,
        'description': 'Net sales amount (must be >= 0)'
    },
    'promo_flag': {
        'dtype': 'int',
        'nullable': False,
        'allowed_values': [0, 1],
        'description': 'Promotion flag (0 or 1)'
    },
    'payment_type': {
        'dtype': 'str',
        'nullable': False,
        'allowed_values': ['cash', 'credit', 'debit', 'mobile', 'giftcard'],
        'description': 'Payment type (cash, credit, debit, mobile, or giftcard)'
    }
}

print("✓ POS schema definition created")
print(f"Schema defines validation for {len(pos_schema_definition)} columns")