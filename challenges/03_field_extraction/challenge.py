from typing import Any, Dict, Tuple, Callable

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
    
    Example:
        data = {
            "user": {
                "name": "John Doe",
                "location": {
                    "city": "San Francisco"
                }
            },
            "metrics": {
                "visits": "1234"
            }
        }
        
        mapping = {
            "name": ("user.name", str),
            "city": ("user.location.city", str),
            "visit_count": ("metrics.visits", int)
        }
        
        result = {
            "name": "John Doe",
            "city": "San Francisco",
            "visit_count": 1234
        }
    
    Raises:
        ValueError: If path format is invalid or mapping is malformed
    """
    # TODO: Implement the field extraction logic:
    # 1. Validate mapping format
    # 2. Parse and validate path strings
    # 3. Extract values using paths
    # 4. Apply transformations
    # 5. Handle missing values and errors
    
    return {}
