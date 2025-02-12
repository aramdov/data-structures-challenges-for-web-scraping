# Field Extraction Challenge

## Problem Description

You need to implement a flexible field extraction system that can pull data from nested structures using path expressions and apply transformations. This is a common requirement when processing web scraping results or API responses where data needs to be extracted and transformed from complex nested structures.

### Task

Implement the `extract_fields` function in `challenge.py` that:

1. Extracts values from nested dictionaries using dot notation paths
2. Applies transformations to extracted values
3. Handles missing or invalid data gracefully
4. Returns a flattened dictionary with transformed values

### Input Format

The function takes two arguments:
1. `data`: A nested dictionary containing the source data
2. `mapping`: A dictionary defining extraction paths and transformations

```python
data = {
    "user": {
        "name": "John Doe",
        "location": {
            "city": "San Francisco",
            "state": "CA",
            "postal": "94105"
        }
    },
    "metrics": {
        "last_active": "2024-02-04T15:30:00Z",
        "visits": "1234",
        "engagement": {
            "likes": "50",
            "comments": "10"
        }
    }
}

mapping = {
    "name": ("user.name", str),
    "city": ("user.location.city", str),
    "visit_count": ("metrics.visits", int),
    "total_engagement": ("metrics.engagement", lambda x: int(x["likes"]) + int(x["comments"])),
    "active_date": ("metrics.last_active", lambda x: x.split("T")[0])
}
```

### Expected Output

The function should return a flattened dictionary with transformed values:

```python
{
    "name": "John Doe",
    "city": "San Francisco",
    "visit_count": 1234,
    "total_engagement": 60,
    "active_date": "2024-02-04"
}
```

### Requirements

- Support dot notation for nested field access (e.g., "user.location.city")
- Apply transformation functions to extracted values
- Handle missing paths by returning None for that field
- Support both simple transformations (like `int`, `str`) and complex lambda functions
- Maintain type hints and clean code practices

### Error Handling

- Missing paths should result in None for that field
- Failed transformations should result in None for that field
- Invalid path format should raise ValueError
- Invalid mapping format should raise ValueError

### Running Tests

1. Ensure pytest is installed:
```bash
pip install pytest
```

2. Run the tests:
```bash
# Run all tests
pytest challenges/03_field_extraction/test_field_extraction.py -v

# Run specific test categories
pytest challenges/03_field_extraction/test_field_extraction.py -v -k "solution"
pytest challenges/03_field_extraction/test_field_extraction.py -v -k "challenge"
```

### Tips

- Break down the problem into smaller functions:
  - Path parsing
  - Value extraction
  - Transformation application
- Use type hints to make the code more maintainable
- Consider edge cases in the data structure
- Think about error handling and validation

### Real-world Applications

This pattern is commonly used in:
- Web scraping data extraction
- API response processing
- Data migration scripts
- ETL pipelines
- Configuration management

### Extension Ideas

- Support list indexing in paths (e.g., "items.0.name")
- Add default values for missing fields
- Support multiple possible paths for a field
- Add validation functions to the mapping
