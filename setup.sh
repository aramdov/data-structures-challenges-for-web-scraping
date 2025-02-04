#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Setting up Python virtual environment...${NC}"

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

echo -e "${GREEN}Virtual environment created and activated${NC}"

# Upgrade pip
echo -e "${BLUE}Upgrading pip...${NC}"
pip install --upgrade pip

# Install dependencies
echo -e "${BLUE}Installing dependencies...${NC}"
pip install -r requirements.txt

# Set up pre-commit hooks (optional)
# echo -e "${BLUE}Setting up pre-commit hooks...${NC}"
# pre-commit install

echo -e "${GREEN}Setup complete! Virtual environment is ready.${NC}"
echo -e "${BLUE}To activate the virtual environment, run:${NC}"
echo "source venv/bin/activate"