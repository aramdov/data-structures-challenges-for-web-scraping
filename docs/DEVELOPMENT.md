# Development Setup

This guide will help you set up your development environment for working with the data structures challenges.

## Prerequisites

- Python 3.9 or higher
- `pip` (Python package installer)
- `git` for version control

## Initial Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/data-structure-challenges.git
cd data-structure-challenges
```

2. Set up the virtual environment:

**Unix/MacOS**:
```bash
# Make the setup script executable
chmod +x setup.sh
# Run the setup script
./setup.sh
```

**Windows**:
```batch
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Daily Development

1. Activate the virtual environment:

**Unix/MacOS**:
```bash
source venv/bin/activate
```

**Windows**:
```batch
venv\Scripts\activate
```

2. Run tests:
```bash
pytest
```

3. Format code:
```bash
# Format Python files
black .
# Sort imports
isort .
```

4. Type checking:
```bash
mypy .
```

## Adding New Dependencies

When adding new dependencies:

1. Add them to `requirements.txt`
2. Install in your virtual environment:
```bash
pip install -r requirements.txt
```

## Deactivating the Virtual Environment

When you're done working:
```bash
deactivate
```

## IDE Integration

### VSCode

Add this to your `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```

### PyCharm

1. Go to Settings/Preferences
2. Project > Python Interpreter
3. Add Interpreter > Existing Environment
4. Select the `python` executable in the `venv/bin` directory