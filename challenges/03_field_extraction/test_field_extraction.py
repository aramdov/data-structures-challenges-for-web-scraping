import pytest
from challenge import extract_fields as challenge_extract
from solution import extract_fields as solution_extract

@pytest.fixture
def sample_data():
    return {
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

@pytest.fixture
def basic_mapping():
    return {
        "name": ("user.name", str),
        "city": ("user.location.city", str),
        "visit_count": ("metrics.visits", int),
        "total_engagement": ("metrics.engagement", lambda x: int(x["likes"]) + int(x["comments"])),
        "active_date": ("metrics.last_active", lambda x: x.split("T")[0])
    }

@pytest.mark.parametrize("extract_fn", [
    pytest.param(challenge_extract, id="challenge"),
    pytest.param(solution_extract, id="solution")
])
def test_basic_extraction(extract_fn, sample_data, basic_mapping):
    expected = {
        "name": "John Doe",
        "city": "San Francisco",
        "visit_count": 1234,
        "total_engagement": 60,
        "active_date": "2024-02-04"
    }
    
    result = extract_fn(sample_data, basic_mapping)
    assert result == expected

@pytest.mark.parametrize("extract_fn", [
    pytest.param(challenge_extract, id="challenge"),
    pytest.param(solution_extract, id="solution")
])
def test_missing_paths(extract_fn, sample_data):
    mapping = {
        "missing_field": ("user.nonexistent", str),
        "name": ("user.name", str)
    }
    
    expected = {
        "missing_field": None,
        "name": "John Doe"
    }
    
    result = extract_fn(sample_data, mapping)
    assert result == expected

@pytest.mark.parametrize("extract_fn", [
    pytest.param(challenge_extract, id="challenge"),
    pytest.param(solution_extract, id="solution")
])
def test_transformation_error(extract_fn, sample_data):
    mapping = {
        "bad_transform": ("metrics.visits", lambda x: int("not a number")),
        "name": ("user.name", str)
    }
    
    expected = {
        "bad_transform": None,
        "name": "John Doe"
    }
    
    result = extract_fn(sample_data, mapping)
    assert result == expected

@pytest.mark.parametrize("extract_fn", [
    pytest.param(challenge_extract, id="challenge"),
    pytest.param(solution_extract, id="solution")
])
def test_nested_transformations(extract_fn):
    data = {
        "items": {
            "values": [1, 2, 3, 4, 5],
            "metadata": {"total": "15"}
        }
    }
    
    mapping = {
        "sum": ("items.values", sum),
        "total": ("items.metadata.total", int)
    }
    
    expected = {
        "sum": 15,
        "total": 15
    }
    
    result = extract_fn(data, mapping)
    assert result == expected

@pytest.mark.parametrize("extract_fn", [
    pytest.param(challenge_extract, id="challenge"),
    pytest.param(solution_extract, id="solution")
])
def test_invalid_path_format(extract_fn):
    data = {"key": "value"}
    mapping = {
        "invalid": ("key..double.dot", str)
    }
    
    with pytest.raises(ValueError):
        extract_fn(data, mapping)

@pytest.mark.parametrize("extract_fn", [
    pytest.param(challenge_extract, id="challenge"),
    pytest.param(solution_extract, id="solution")
])
def test_invalid_mapping_format(extract_fn):
    data = {"key": "value"}
    invalid_mappings = [
        {"bad": "not_a_tuple"},
        {"bad": ("path",)},  # Missing transform function
        {"bad": ("path", "not_callable")}
    ]
    
    for mapping in invalid_mappings:
        with pytest.raises(ValueError):
            extract_fn(data, mapping)
