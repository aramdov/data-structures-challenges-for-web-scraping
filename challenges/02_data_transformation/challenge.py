from typing import List, Dict, Any

def normalize_product_data(products: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Normalize product data from various sources into a consistent format.
    
    Args:
        products: List of product dictionaries with varying structures
        
    Returns:
        List of normalized product dictionaries with consistent structure:
        [
            {
                "name": str,
                "price": float,
                "stock": int,
                "tags": List[str]
            },
            ...
        ]
        
    Example:
        Input:
        [
            {
                "product": {
                    "name": "Laptop Pro",
                    "details": {
                        "price": "1299.99",
                        "stock": "15"
                    },
                    "tags": ["electronics", "computers"]
                }
            }
        ]
        
        Output:
        [
            {
                "name": "Laptop Pro",
                "price": 1299.99,
                "stock": 15,
                "tags": ["electronics", "computers"]
            }
        ]
    """
    normalized = []
    
    # TODO: Implement the normalization logic:
    # 1. Extract name from either top level or nested product object
    # 2. Extract and convert price to float
    # 3. Extract and convert stock to integer
    # 4. Extract and normalize tags to list of strings
    # 5. Create normalized product entry with consistent structure
    
    return normalized
