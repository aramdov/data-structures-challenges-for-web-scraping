# Data Transformation Challenge

## Problem Description

You are given a list of product data from different e-commerce sources that needs to be normalized into a consistent format. The data contains nested structures, inconsistent field names, and varying data types that need to be transformed.

### Task

Implement the `normalize_product_data` function in `challenge.py` that:

1. Flattens nested product data
2. Normalizes field names
3. Converts values to consistent types
4. Handles missing or null values with sensible defaults

### Input Format

The input will be a list of dictionaries containing product data with varying structures:

```python
products = [
    {
        "product": {
            "name": "Laptop Pro",
            "details": {
                "price": "1299.99",
                "stock": "15"
            },
            "tags": ["electronics", "computers"]
        }
    },
    {
        "name": "Desk Lamp",
        "pricing": {
            "amount": "49.50",
            "currency": "USD"
        },
        "inventory": "23",
        "categories": "home,lighting"
    }
]
```

### Expected Output

The function should return a list of normalized product dictionaries:

```python
[
    {
        "name": "Laptop Pro",
        "price": 1299.99,
        "stock": 15,
        "tags": ["electronics", "computers"]
    },
    {
        "name": "Desk Lamp",
        "price": 49.50,
        "stock": 23,
        "tags": ["home", "lighting"]
    }
]
```

### Requirements

- All prices should be converted to float
- Stock quantities should be converted to integer
- Tags should always be a list of strings
- Missing values should use these defaults:
  - price: 0.0
  - stock: 0
  - tags: []

### Running Tests

1. Make sure you have pytest installed:
```bash
pip install pytest
```

2. Navigate to the project root directory (where the main README.md is located):
```bash
cd /path/to/data-structure-challenges-for-web-scraping
```

3. Run the tests:
```bash
# Run all tests (both challenge and solution implementations)
pytest challenges/02_data_transformation/test_transformation.py -v

# Run only solution tests
pytest challenges/02_data_transformation/test_transformation.py -v -k "solution"

# Run only challenge tests
pytest challenges/02_data_transformation/test_transformation.py -v -k "challenge"

# Run a specific test for both implementations
pytest challenges/02_data_transformation/test_transformation.py -v -k "test_basic_product_normalization"
```

The tests will verify your implementation against various scenarios:
- Basic product normalization
- Alternative data structures
- Missing values
- Invalid data
- Multiple products

### Caveats
- The currency field is intentionally excluded from the normalized output because the challenge aims to standardize the data into a consistent format with only the essential fields that are common across different input structures. 
- In the input data, currency information appears inconsistently:
    - Some products have it (like the Desk Lamp with "currency": "USD")
    - Others don't include currency information at all
- This simplification makes the challenge more focused on the key aspects of data transformation:
    - Flattening nested structures
    - Type conversion
    - Handling missing values
    - Normalizing inconsistent field names