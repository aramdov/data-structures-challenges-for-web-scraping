# Data Structure Challenges

A collection of data structure and transformation challenges focused on real-world scenarios in data processing and API development within the web scraping domain. This repository is designed to help engineers practice handling complex data structures, with an emphasis on validation, transformation, and clean code practices.

## 🎯 Purpose

This repository helps you practice:
- Schema validation and type coercion
- Complex data structure manipulation
- Clean, maintainable code organization
- Test-driven development
- Error handling and edge cases

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/aramdov/data-structure-challenges-for-web-scraping.git
cd data-structure-challenges-for-web-scraping
```

2. Set up your environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Run the tests:
```bash
pytest
```

## 📚 Repository Structure

### Challenges
Each challenge is organized in its own directory under `challenges/` with:
- README.md explaining the problem and requirements
- challenge.py containing the problem template
- solution.py containing a reference solution
- test_{challenge}.py containing test cases

### Core Concepts
The `core/` directory contains reusable utilities and patterns:
- validators.py: Common validation patterns
- transformers.py: Reusable data transformation utilities

### Documentation
The `docs/` directory contains:
- Detailed explanations of common patterns
- Setup instructions
- Contribution guidelines

## 🎯 Challenge Categories

1. **Schema Validation**
   - Type validation and coercion
   - Nested schema validation
   - Custom validation rules

2. **Data Transformation**
   - Nested structure flattening
   - Field extraction and mapping
   - Data normalization

3. **Field Extraction**
   - Path-based access
   - Custom transformation functions
   - Error handling

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](docs/CONTRIBUTING.md) first.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

This repository was inspired by real-world data processing challenges and the need for structured practice materials for engineering interviews.