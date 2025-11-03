import pandas as pd
import numpy as np

# Apply schema validation with type coercion
validation_errors = []
validated_df = verified_df.copy()

# Track row-level validation status
validated_df['_validation_status'] = 'PASS'
validated_df['_validation_errors'] = ''

# Type coercion and validation for each column
for _col_name, _schema in pos_schema_definition.items():
    if _col_name not in validated_df.columns:
        validation_errors.append({
            'column': _col_name,
            'error_type': 'MISSING_COLUMN',
            'description': f'Required column {_col_name} is missing'
        })
        continue
    
    # Check nulls
    if not _schema['nullable']:
        _null_mask = validated_df[_col_name].isna()
        if _null_mask.any():
            _null_indices = validated_df[_null_mask].index
            for _idx in _null_indices:
                _err_msg = f"{_col_name}: NULL value"
                validated_df.loc[_idx, '_validation_status'] = 'FAIL'
                validated_df.loc[_idx, '_validation_errors'] += _err_msg + '; '
    
    # Type coercion
    _target_dtype = _schema['dtype']
    try:
        if _target_dtype == 'str':
            validated_df[_col_name] = validated_df[_col_name].astype(str)
        elif _target_dtype == 'int':
            validated_df[_col_name] = pd.to_numeric(validated_df[_col_name], errors='coerce').astype('Int64')
        elif _target_dtype == 'float':
            validated_df[_col_name] = pd.to_numeric(validated_df[_col_name], errors='coerce')
        elif _target_dtype == 'datetime64[ns]':
            validated_df[_col_name] = pd.to_datetime(validated_df[_col_name], errors='coerce')
    except Exception as _e:
        validation_errors.append({
            'column': _col_name,
            'error_type': 'TYPE_COERCION_FAILED',
            'description': f'Failed to coerce {_col_name} to {_target_dtype}: {str(_e)}'
        })
    
    # Value constraints
    if 'min_value' in _schema:
        _min_val = _schema['min_value']
        _invalid_mask = validated_df[_col_name] < _min_val
        if _invalid_mask.any():
            _invalid_indices = validated_df[_invalid_mask].index
            for _idx in _invalid_indices:
                _err_msg = f"{_col_name}: value < {_min_val}"
                validated_df.loc[_idx, '_validation_status'] = 'FAIL'
                validated_df.loc[_idx, '_validation_errors'] += _err_msg + '; '
    
    if 'allowed_values' in _schema:
        _allowed = _schema['allowed_values']
        _invalid_mask = ~validated_df[_col_name].isin(_allowed)
        if _invalid_mask.any():
            _invalid_indices = validated_df[_invalid_mask].index
            for _idx in _invalid_indices:
                _err_msg = f"{_col_name}: value not in {_allowed}"
                validated_df.loc[_idx, '_validation_status'] = 'FAIL'
                validated_df.loc[_idx, '_validation_errors'] += _err_msg + '; '

print(f"✓ Validation complete on {len(validated_df)} rows")