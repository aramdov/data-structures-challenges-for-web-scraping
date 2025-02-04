# Challenge 01: Schema Validation

## Problem Statement

Implement a schema validator that can validate and transform input data according to a specified schema. The validator should handle type coercion and nested structures while providing clear error messages for validation failures.

## Requirements

1. Type Validation
   - Validate basic Python types (str, int, float, bool, list, dict)
   - Support type coercion where appropriate
   - Handle nested structures

2. Error Handling
   - Provide clear error messages for validation failures
   - Include path information for nested structure errors
   - Handle missing required fields

3. Performance
   - Minimize unnecessary iterations
   - Handle large nested structures efficiently

## Example

```python
# Input
data = {
    'user_id': '123',
    'active': 'true',
    'score': '98.6',
    'tags': 'python,data,engineering'
}

schema = {
    'user_id': int,
    'active': bool,
    'score': float,
    'tags': list
}

# Expected Output
{
    'user_id': 123,
    'active': True,
    'score': 98.6,
    'tags': ['python', 'data', 'engineering']
}
```

## Edge Cases to Consider

1. Missing Fields
2. None Values
3. Invalid Type Conversions
4. Nested Structures
5. Empty Values

## Testing

Run the tests using:
```bash
pytest test_schema_validation.py
```

## Hints

1. Consider using Python's built-in `isinstance()` for type checking
2. Look into the `typing` module for more complex type validation
3. Consider creating custom exceptions for different validation errors