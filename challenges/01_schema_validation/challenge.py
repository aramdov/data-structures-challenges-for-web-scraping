from typing import Any, Dict, Type
from dataclasses import dataclass


@dataclass
class ValidationError(Exception):
    """Represents a validation error with contextual information.
    
    Attributes:
        path: The path to the field that failed validation
        message: A descriptive error message
        value: The value that failed validation
    """
    path: str
    message: str
    value: Any
    
    def __str__(self):
        return f"{self.path}: {self.message}"


class SchemaValidator:
    """A schema validator that ensures data conforms to expected types.
    
    This validator should:
    1. Check that input data matches the schema's type requirements
    2. Convert data to the correct type when possible (type coercion)
    3. Provide clear error messages when validation fails
    4. Handle nested data structures gracefully
    
    Example:
        validator = SchemaValidator()
        data = {'age': '25', 'active': 'true'}
        schema = {'age': int, 'active': bool}
        result = validator.validate(data, schema)
        # result = {'age': 25, 'active': True}
    """
    
    def validate(self, data: Dict[str, Any], schema: Dict[str, Type]) -> Dict[str, Any]:
        """Validates input data against a schema and returns transformed data.
        
        Args:
            data: The input dictionary to validate
            schema: A dictionary mapping field names to their expected types
            
        Returns:
            A new dictionary with all values converted to their expected types
            
        Raises:
            ValidationError: If any field fails validation
        """
        if not isinstance(data, dict):
            raise ValidationError("root", "Input must be a dictionary", data)
            
        result = {}
        for field_name, expected_type in schema.items():
            # Alternative for handling missing `field_name` in `data` is to use `data.get(field_name)`
            # With `data.get(field_name)`, we can provide a default value if `field_name` is missing
            # Default value can be `None` or any other value. 
            # For example, `data.get(field_name, 'default_value')`
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
                raise ValidationError(e.path, e.message, e.value)
                
        return result
    
    def _coerce_value(self, value: Any, target_type: Type, path: str) -> Any:
        """Attempts to convert a value to the target type.
        
        Args:
            value: The value to convert
            target_type: The type to convert to
            path: The current field path (for error reporting)
            
        Returns:
            The converted value
            
        Raises:
            ValidationError: If the value cannot be converted
        """
        if value is None:
            raise ValidationError(path, "Value cannot be None", value)
            
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
                    # Handle empty string case
                    if not value:
                        return []
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


def example_usage():
    """Demonstrates how to use the SchemaValidator class."""
    validator = SchemaValidator()
    
    # Example 1: Basic type conversion
    data = {
        'user_id': '123',         # Should convert to int
        'active': 'true',         # Should convert to bool
        'score': '98.6',          # Should convert to float
        'tags': 'a,b,c'          # Should convert to list
    }
    
    schema = {
        'user_id': int,
        'active': bool,
        'score': float,
        'tags': list
    }
    
    try:
        result = validator.validate(data, schema)
        print("Validated data:", result)
    except ValidationError as e:
        print(f"Validation failed at {e.path}: {e.message}")


if __name__ == "__main__":
    example_usage()