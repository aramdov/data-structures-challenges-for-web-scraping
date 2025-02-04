import pytest
from challenge import normalize_product_data as challenge_normalize
from solution import normalize_product_data as solution_normalize

# Note
# Fixtures are a way to provide reusable test data or setup:
# Benefits include Reusability, Setup/teardown,
# ,dependency injection, and scope control.

# Test data fixtures
@pytest.fixture
def basic_product():
    return [{
        "product": {
            "name": "Laptop Pro",
            "details": {
                "price": "1299.99",
                "stock": "15"
            },
            "tags": ["electronics", "computers"]
        }
    }]

@pytest.fixture
def basic_product_expected():
    return [{
        "name": "Laptop Pro",
        "price": 1299.99,
        "stock": 15,
        "tags": ["electronics", "computers"]
    }]


# Parametrize lets you run the same test with different inputs:
# Can test multiple cases with different inputs.
# Avoid duplicating test code.
# Test both implementations.
# Can support Combinatorial Testing by parametrizing multiple args.
@pytest.mark.parametrize("normalize_fn", [
    pytest.param(challenge_normalize, id="challenge"),
    pytest.param(solution_normalize, id="solution")
])
def test_basic_product_normalization(normalize_fn, basic_product, basic_product_expected):
    assert normalize_fn(basic_product) == basic_product_expected

@pytest.mark.parametrize("normalize_fn", [
    pytest.param(challenge_normalize, id="challenge"),
    pytest.param(solution_normalize, id="solution")
])
def test_alternative_structure(normalize_fn):
    input_data = [{
        "name": "Desk Lamp",
        "pricing": {
            "amount": "49.50",
            "currency": "USD"
        },
        "inventory": "23",
        "categories": "home,lighting"
    }]
    
    expected = [{
        "name": "Desk Lamp",
        "price": 49.50,
        "stock": 23,
        "tags": ["home", "lighting"]
    }]
    
    assert normalize_fn(input_data) == expected

@pytest.mark.parametrize("normalize_fn", [
    pytest.param(challenge_normalize, id="challenge"),
    pytest.param(solution_normalize, id="solution")
])
def test_missing_values(normalize_fn):
    input_data = [{
        "product": {
            "name": "Mystery Item"
        }
    }]
    
    expected = [{
        "name": "Mystery Item",
        "price": 0.0,
        "stock": 0,
        "tags": []
    }]
    
    assert normalize_fn(input_data) == expected

@pytest.mark.parametrize("normalize_fn", [
    pytest.param(challenge_normalize, id="challenge"),
    pytest.param(solution_normalize, id="solution")
])
def test_invalid_values(normalize_fn):
    input_data = [{
        "product": {
            "name": "Bad Data",
            "details": {
                "price": "invalid",
                "stock": "not a number"
            },
            "tags": None
        }
    }]
    
    expected = [{
        "name": "Bad Data",
        "price": 0.0,
        "stock": 0,
        "tags": []
    }]
    
    assert normalize_fn(input_data) == expected

@pytest.mark.parametrize("normalize_fn", [
    pytest.param(challenge_normalize, id="challenge"),
    pytest.param(solution_normalize, id="solution")
])
def test_multiple_products(normalize_fn):
    input_data = [
        {
            "product": {
                "name": "Item 1",
                "details": {"price": "10.99", "stock": "5"},
                "tags": ["tag1"]
            }
        },
        {
            "name": "Item 2",
            "pricing": {"amount": "20.50"},
            "inventory": "10",
            "categories": "tag2,tag3"
        }
    ]
    
    expected = [
        {
            "name": "Item 1",
            "price": 10.99,
            "stock": 5,
            "tags": ["tag1"]
        },
        {
            "name": "Item 2",
            "price": 20.50,
            "stock": 10,
            "tags": ["tag2", "tag3"]
        }
    ]
    
    assert normalize_fn(input_data) == expected
