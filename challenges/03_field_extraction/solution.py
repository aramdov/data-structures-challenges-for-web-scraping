from typing import Any, Dict, Tuple, Callable

def get_nested_value(data: Dict[str, Any], path: str) -> Any:
    """Helper function to get value from nested dictionary using dot notation path."""
    if not path or '..' in path:
        raise ValueError(f"Invalid path format: {path}")
    
    current = data
    for key in path.split('.'):
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current

def validate_mapping(mapping: Dict[str, Tuple[str, Callable]]) -> None:
    """Validate mapping format and raise ValueError if invalid."""
    for key, value in mapping.items():
        if not isinstance(value, tuple) or len(value) != 2:
            raise ValueError(f"Invalid mapping format for key '{key}': Expected (path, transform) tuple")
        path, transform = value
        if not isinstance(path, str):
            raise ValueError(f"Invalid path format for key '{key}': Expected string")
        if not callable(transform):
            raise ValueError(f"Invalid transform for key '{key}': Expected callable")

def extract_fields(data: Dict[str, Any], mapping: Dict[str, Tuple[str, Callable]]) -> Dict[str, Any]:
    """
    Extract and transform fields from nested data structure based on mapping rules.
    
    Args:
        data: A nested dictionary containing the source data
        mapping: A dictionary where:
            - key: the output field name
            - value: tuple of (path, transform_function)
                - path: dot notation string indicating nested location (e.g., "user.name")
                - transform_function: callable to transform the extracted value
    
    Returns:
        Dictionary with extracted and transformed values
    
    Raises:
        ValueError: If path format is invalid or mapping is malformed
    """
    # Validate mapping format
    validate_mapping(mapping)
    
    result = {}
    
    # Process each field in the mapping
    for output_field, (path, transform) in mapping.items():
        try:
            # Extract value using path
            value = get_nested_value(data, path)
            
            # Apply transformation if value exists
            if value is not None:
                try:
                    result[output_field] = transform(value)
                except Exception:
                    result[output_field] = None
            else:
                result[output_field] = None
                
        except ValueError as e:
            # Re-raise path format errors
            raise e
        except Exception:
            # Handle any other errors by setting field to None
            result[output_field] = None
    
    return result
