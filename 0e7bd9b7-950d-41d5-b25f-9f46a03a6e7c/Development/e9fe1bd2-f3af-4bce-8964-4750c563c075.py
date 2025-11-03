import pandas as pd

# Generate comprehensive export metrics report
export_metrics = {
    'total_rows_exported': total_export_rows,
    'num_partitions': len(clean_partition_counts),
    'partition_distribution': clean_partition_counts,
    'file_sizes_bytes': export_file_sizes,
    'total_size_bytes': sum(export_file_sizes.values()),
    'avg_rows_per_partition': total_export_rows / len(clean_partition_counts) if len(clean_partition_counts) > 0 else 0,
    'output_path': str(clean_output_dir)
}

# Calculate total size in KB for better readability
total_size_kb = export_metrics['total_size_bytes'] / 1024

print("=" * 70)
print("POS CLEANED DATA EXPORT METRICS")
print("=" * 70)
print(f"\n📊 Export Summary:")
print(f"  Total Rows Exported: {export_metrics['total_rows_exported']}")
print(f"  Number of Partitions: {export_metrics['num_partitions']}")
print(f"  Output Path: {export_metrics['output_path']}")
print(f"\n📁 Partition Distribution:")
for partition_name, row_count in sorted(export_metrics['partition_distribution'].items()):
    file_size_kb = export_metrics['file_sizes_bytes'][partition_name] / 1024
    print(f"  {partition_name}: {row_count} rows ({file_size_kb:.2f} KB)")
print(f"\n💾 Storage Metrics:")
print(f"  Total Size: {total_size_kb:.2f} KB ({export_metrics['total_size_bytes']} bytes)")
print(f"  Avg Rows per Partition: {export_metrics['avg_rows_per_partition']:.1f}")
print("=" * 70)