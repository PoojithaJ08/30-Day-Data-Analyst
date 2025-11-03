import pandas as pd

# Generate validation report with pass/fail counts and error types
validation_report = {
    'total_rows': len(validated_df),
    'pass_count': (validated_df['_validation_status'] == 'PASS').sum(),
    'fail_count': (validated_df['_validation_status'] == 'FAIL').sum(),
    'pass_rate': (validated_df['_validation_status'] == 'PASS').sum() / len(validated_df) * 100
}

# Error type breakdown
failed_rows_df = validated_df[validated_df['_validation_status'] == 'FAIL']
error_types = {}

if len(failed_rows_df) > 0:
    for _errors in failed_rows_df['_validation_errors']:
        for _error in _errors.split('; '):
            if _error.strip():
                _error_key = _error.split(':')[0].strip() if ':' in _error else _error
                error_types[_error_key] = error_types.get(_error_key, 0) + 1

validation_report['error_types'] = error_types
validation_report['schema_errors'] = validation_errors

# Print summary
print("=" * 60)
print("POS DATA VALIDATION REPORT")
print("=" * 60)
print(f"\nTotal Rows Validated: {validation_report['total_rows']}")
print(f"✓ Passed: {validation_report['pass_count']} ({validation_report['pass_rate']:.1f}%)")
print(f"✗ Failed: {validation_report['fail_count']} ({100-validation_report['pass_rate']:.1f}%)")

if validation_report['schema_errors']:
    print(f"\n⚠ Schema-level errors: {len(validation_report['schema_errors'])}")
    for _err in validation_report['schema_errors']:
        print(f"  - {_err['error_type']}: {_err['description']}")

if error_types:
    print(f"\n⚠ Row-level validation errors by type:")
    for _err_type, _count in error_types.items():
        print(f"  - {_err_type}: {_count} occurrences")
else:
    print("\n✓ All rows passed validation!")

print("\n" + "=" * 60)
print("Schema applied with type coercion:")
print("  • txn_id, store_id, product_id → str")
print("  • txn_date → datetime64[ns]")
print("  • qty → int (>=0)")
print("  • net_sales → float (>=0)")
print("  • promo_flag → int (in [0,1])")
print("  • payment_type → str (in allowed set)")
print("=" * 60)