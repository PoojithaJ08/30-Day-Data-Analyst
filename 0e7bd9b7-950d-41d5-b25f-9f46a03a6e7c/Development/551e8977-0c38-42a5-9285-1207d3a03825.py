import pandas as pd

# Generate comprehensive DQ summary report
cleaning_report = {
    'total_rows': len(final_cleaned_df),
    'flag_missing_dim_count': final_cleaned_df['flag_missing_dim'].sum(),
    'flag_extreme_qty_count': final_cleaned_df['flag_extreme_qty'].sum(),
    'flag_negative_sales_count': final_cleaned_df['flag_negative_sales'].sum(),
    'total_flagged_rows': final_cleaned_df['has_dq_issue'].sum(),
    'flagged_percentage': (final_cleaned_df['has_dq_issue'].sum() / len(final_cleaned_df) * 100) if len(final_cleaned_df) > 0 else 0,
    'unit_price_calculated': final_cleaned_df['unit_price'].notna().sum(),
    'unit_price_null': final_cleaned_df['unit_price'].isna().sum()
}

# Check success criteria: <2% flagged rows
success_criteria_met = cleaning_report['flagged_percentage'] < 2.0

print("=" * 70)
print("POS DATA CLEANING SUMMARY REPORT")
print("=" * 70)
print(f"\n📊 Dataset Overview:")
print(f"  Total Rows: {cleaning_report['total_rows']}")
print(f"\n🚩 Data Quality Flags:")
print(f"  flag_missing_dim:     {cleaning_report['flag_missing_dim_count']} rows")
print(f"  flag_extreme_qty:     {cleaning_report['flag_extreme_qty_count']} rows")
print(f"  flag_negative_sales:  {cleaning_report['flag_negative_sales_count']} rows")
print(f"  Total Flagged:        {cleaning_report['total_flagged_rows']} rows ({cleaning_report['flagged_percentage']:.2f}%)")
print(f"\n💰 Unit Price Calculation:")
print(f"  Calculated:  {cleaning_report['unit_price_calculated']} rows")
print(f"  Null (qty=0): {cleaning_report['unit_price_null']} rows")
print(f"\n✅ Success Criteria:")
print(f"  Target: <2% flagged rows")
print(f"  Actual: {cleaning_report['flagged_percentage']:.2f}%")
print(f"  Status: {'PASS ✓' if success_criteria_met else 'FAIL ✗'}")
print("=" * 70)