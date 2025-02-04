import pytest
from challenge import SchemaValidator, ValidationError

@pytest.fixture
def validator():
    return SchemaValidator()


class TestSchemaValidation:
    """Test suite for schema validation functionality."""
    
    def test_basic_validation(self, validator):
        """Test basic type validation and coercion."""
        data = {
            'user_id': '123',
            'active': 'true',
            'score': '98.6',
            'tags': 'python,data,engineering'
        }
        schema = {
            'user_id': int,
            'active': bool,
            'score': float,
            'tags': list
        }
        
        result = validator.validate(data, schema)
        
        assert isinstance(result['user_id'], int)
        assert result['user_id'] == 123
        assert isinstance(result['active'], bool)
        assert result['active'] is True
        assert isinstance(result['score'], float)
        assert result['score'] == 98.6
        assert isinstance(result['tags'], list)
        assert result['tags'] == ['python', 'data', 'engineering']
    
    def test_missing_field(self, validator):
        """Test handling of missing required fields."""
        data = {'user_id': '123'}  # Missing required fields
        schema = {
            'user_id': int,
            'active': bool
        }
        
        with pytest.raises(ValidationError) as exc:
            validator.validate(data, schema)
        assert 'missing' in str(exc.value).lower()
        assert 'active' in str(exc.value)
    
    def test_invalid_type_conversion(self, validator):
        """Test handling of invalid type conversions."""
        data = {'user_id': 'not_an_integer'}
        schema = {'user_id': int}
        
        with pytest.raises(ValidationError) as exc:
            validator.validate(data, schema)
        assert 'cannot convert' in str(exc.value).lower()
    
    def test_boolean_conversion(self, validator):
        """Test various boolean string representations."""
        test_cases = [
            ('true', True),
            ('True', True),
            ('1', True),
            ('yes', True),
            ('false', False),
            ('False', False),
            ('0', False),
            ('no', False)
        ]
        
        for input_val, expected in test_cases:
            data = {'active': input_val}
            schema = {'active': bool}
            result = validator.validate(data, schema)
            assert result['active'] == expected
    
    def test_list_conversion(self, validator):
        """Test various list conversion scenarios."""
        test_cases = [
            ('a,b,c', ['a', 'b', 'c']),
            ('single', ['single']),
            ('', [])
        ]
        
        for input_val, expected in test_cases:
            data = {'tags': input_val}
            schema = {'tags': list}
            result = validator.validate(data, schema)
            assert result['tags'] == expected
    
    def test_none_values(self, validator):
        """Test handling of None values."""
        data = {'user_id': None}
        schema = {'user_id': int}
        
        with pytest.raises(ValidationError) as exc:
            validator.validate(data, schema)
        assert 'none' in str(exc.value).lower()
    
    def test_invalid_input_type(self, validator):
        """Test handling of invalid input type."""
        data = "not a dictionary"  # Invalid input type
        schema = {'user_id': int}
        
        with pytest.raises(ValidationError) as exc:
            validator.validate(data, schema)
        assert 'dictionary' in str(exc.value).lower()


if __name__ == '__main__':
    pytest.main([__file__])