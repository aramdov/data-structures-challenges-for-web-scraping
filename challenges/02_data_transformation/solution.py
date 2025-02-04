from typing import List, Dict, Any

def extract_value(data: Dict[str, Any], *keys: str, default: Any = None) -> Any:
    """Helper function to safely extract nested values."""
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def normalize_tags(tags: Any) -> List[str]:
    """Convert various tag formats to a list of strings."""
    if not tags:
        return []
    if isinstance(tags, str):
        return [tag.strip() for tag in tags.split(',') if tag.strip()]
    if isinstance(tags, list):
        return [str(tag) for tag in tags]
    return []

def normalize_product_data(products: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Normalize product data from various sources into a consistent format.
    """
    normalized = []
    
    for product in products:
        # Extract name from either top level or nested product object
        name = extract_value(product, 'name') or extract_value(product, 'product', 'name', default='')
        
        # Extract and convert price
        price_str = (
            extract_value(product, 'details', 'price') or
            extract_value(product, 'product', 'details', 'price') or
            extract_value(product, 'pricing', 'amount') or
            '0.0'
        )
        try:
            price = float(price_str)
        except (ValueError, TypeError):
            price = 0.0
            
        # Extract and convert stock
        stock_str = (
            extract_value(product, 'details', 'stock') or
            extract_value(product, 'product', 'details', 'stock') or
            extract_value(product, 'inventory') or
            '0'
        )
        try:
            stock = int(float(stock_str))
        except (ValueError, TypeError):
            stock = 0
            
        # Extract and normalize tags
        tags = (
            extract_value(product, 'tags') or
            extract_value(product, 'product', 'tags') or
            extract_value(product, 'categories')
        )
        normalized_tags = normalize_tags(tags)
        
        # Create normalized product entry
        normalized.append({
            'name': name,
            'price': price,
            'stock': stock,
            'tags': normalized_tags
        })
    
    return normalized
