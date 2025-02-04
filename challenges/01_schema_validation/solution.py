from typing import Any, Dict, Type, Optional, Union
from dataclasses import dataclass

@dataclass
class ValidationError:
    path: str
    message: str
    value: Any

class SchemaValidator:
    """A schema validator that supports type validation and coercion."""
    
    def validate(self, data: Dict[str, Any], schema: Dict[str, Type]) -> Dict[str, Any]:
        """Validates and transforms input data according to schema."""
        if not isinstance(data, dict):
            raise ValidationError("root", "Input must be a dictionary", data)
            
        result = {}
        for field_name, expected_type in schema.items():
            if field_name not in data:
                raise ValidationError(
                    field_name,
                    f"Required field '{field_name}' is missing",
                    None
                )
            
            try:
                result[field_name] = self._coerce_value(
                    data[field_name], 
                    expected_type,
                    field_name
                )
            except ValidationError as e:
                # Re-raise with path information
                raise ValidationError(
                    e.path,
                    e.message,
                    e.value
                )
                
        return result
    
    def _coerce_value(self, value: Any, target_type: Type, path: str) -> Any:
        """Attempts to coerce a value to the target type."""
        # Handle None values
        if value is None:
            raise ValidationError(path, f"Value cannot be None", value)
            
        # Already correct type
        if isinstance(value, target_type):
            return value
            
        try:
            # Handle boolean special case
            if target_type == bool:
                if isinstance(value, str):
                    value = value.lower()
                    if value in ('true', '1', 'yes'):
                        return True
                    if value in ('false', '0', 'no'):
                        return False
                raise ValidationError(
                    path,
                    f"Cannot convert '{value}' to boolean",
                    value
                )
                
            # Handle list special case
            if target_type == list:
                if isinstance(value, str):
                    # Assume comma-separated string
                    return [v.strip() for v in value.split(',')]
                if hasattr(value, '__iter__') and not isinstance(value, str):
                    return list(value)
                raise ValidationError(
                    path,
                    f"Cannot convert '{value}' to list",
                    value
                )
                
            # Handle numeric types
            if target_type in (int, float):
                try:
                    return target_type(value)
                except (ValueError, TypeError):
                    raise ValidationError(
                        path,
                        f"Cannot convert '{value}' to {target_type.__name__}",
                        value
                    )
                    
            # Handle strings
            if target_type == str:
                return str(value)
                
            raise ValidationError(
                path,
                f"Unsupported type conversion to {target_type.__name__}",
                value
            )
            
        except ValidationError:
            raise
        except Exception as e:
            raise ValidationError(
                path,
                f"Unexpected error during conversion: {str(e)}",
                value
            )

# Example usage showing more complex scenarios
if __name__ == "__main__":
    validator = SchemaValidator()
    
    # Test with various edge cases
    test_cases = [
        # Basic case
        ({
            'user_id': '123',
            'active': 'true',
            'score': '98.6',
            'tags': 'python,data,engineering'
        }, {
            'user_id': int,
            'active': bool,
            'score': float,
            'tags': list
        }),
        
        # Edge cases
        ({
            'user_id': 0,
            'active': 'FALSE',
            'score': 0.0,
            'tags': []
        }, {
            'user_id': int,
            'active': bool,
            'score': float,
            'tags': list
        })
    ]
    
    for data, schema in test_cases:
        try:
            result = validator.validate(data, schema)
            print(f"\nInput: {data}")
            print(f"Result: {result}")
        except ValidationError as e:
            print(f"\nValidation failed at {e.path}: {e.message}")