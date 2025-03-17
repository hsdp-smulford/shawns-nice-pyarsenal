.PHONY: setup clean lint format test coverage install uninstall help dev-install

# Default target
.DEFAULT_GOAL := help

# Variables
PYTHON = python
POETRY = poetry

# Help command
help:
	@echo "Available commands:"
	@echo "  make setup        - Set up development environment"
	@echo "  make clean        - Remove build artifacts"
	@echo "  make lint         - Run linting tools"
	@echo "  make format       - Run code formatters"
	@echo "  make test         - Run tests"
	@echo "  make coverage     - Run tests with coverage report"
	@echo "  make install      - Install dependencies"
	@echo "  make dev-install  - Install development dependencies"
	@echo "  make uninstall    - Remove virtual environment"

# Setup development environment
setup: install dev-install
	$(POETRY) run pre-commit install

# Install dependencies
install:
	$(POETRY) install --no-root

# Install development dependencies
dev-install:
	$(POETRY) install --no-root --with dev

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete

# Run linting tools
lint:
	$(POETRY) run flake8 .
	$(POETRY) run mypy .
	$(POETRY) run bandit -r . -x ./tests

# Format code
format:
	$(POETRY) run black .
	$(POETRY) run isort .

# Run tests
test:
	$(POETRY) run pytest

# Run tests with coverage
coverage:
	$(POETRY) run pytest --cov=. --cov-report=html

# Uninstall
uninstall:
	rm -rf .venv/
