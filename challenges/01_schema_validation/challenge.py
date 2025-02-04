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
        # TODO: Implement validation logic
        # 1. Check if input is a dictionary
        # 2. Iterate through schema fields
        # 3. Validate presence of required fields
        # 4. Convert values to expected types
        raise NotImplementedError("Implement the validate method")
    
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
        # TODO: Implement type coercion logic
        # 1. Handle None values
        # 2. Handle values already of correct type
        # 3. Implement conversion logic for:
        #    - Strings to numbers (int, float)
        #    - Strings to booleans ('true'/'false', '1'/'0', 'yes'/'no')
        #    - Strings to lists (comma-separated)
        raise NotImplementedError("Implement the _coerce_value method")


def example_usage():
    """Demonstrates how to use the SchemaValidator class."""
    validator = SchemaValidator()
    
    # Example: Basic type conversion
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