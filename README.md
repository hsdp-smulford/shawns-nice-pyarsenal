# Shawn's Nice PyArsenal 🐍

[![CI/CD Pipeline](https://github.com/hsdp-smulford/shawns-nice-pyarsenal/actions/workflows/ci.yaml/badge.svg)](https://github.com/hsdp-smulford/shawns-nice-pyarsenal/actions/workflows/ci.yaml)
[![codecov](https://codecov.io/gh/hsdp-smulford/shawns-nice-pyarsenal/branch/main/graph/badge.svg)](https://codecov.io/gh/hsdp-smulford/shawns-nice-pyarsenal)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A curated arsenal of Python utilities, snippets, and whatnot.

## 🚀 Quick Start

### Using direnv (recommended)

```bash
# Install direnv if needed
brew install direnv

# Allow the direnv configuration for this directory
direnv allow .

# All environment variables and virtual env will be automatically loaded when you enter the directory
```

### Using Poetry

```bash
# Install dependencies
poetry install --no-root --with dev

# Activate the virtual environment (Poetry 2.0+)
poetry env activate

# To leave the virtual environment when done
deactivate

# Install pre-commit hooks
pre-commit install
```

### Using Make

```bash
# Set up complete development environment
make setup

# Run linting
make lint

# Run tests
make test
```

### Using Docker

```bash
# Build the Docker image
docker build -t pyarsenal .

# Run with interactive shell
docker run -it pyarsenal
```

## 🧰 Development Tools

### Linting and Formatting

- **Black**: Code formatting
- **Flake8**: Code linting
- **isort**: Import sorting
- **mypy**: Type checking

```bash
# Format code
make format

# Check code quality
make lint
```

### Security and Quality

- **Bandit**: Security scanning
- **Radon**: Code complexity analysis

```bash
# Run security checks
poetry run bandit -r . -x ./tests

# Check code complexity
poetry run radon cc . -a
```

### Testing

- **pytest**: Testing with coverage reporting

```bash
# Run tests
make test

# Run with coverage
make coverage
```

## 🔄 CI/CD Pipeline

This repository uses GitHub Actions for continuous integration:

### Testing Actions Locally

You can test GitHub Actions locally using [act](https://github.com/nektos/act):

```bash
# Install act (on macOS)
brew install act

# Run all workflows
act

# Run a specific workflow
act -W .github/workflows/ci.yaml

# Run a specific job
act -j test
```

1. **Code Quality**
   - Formatting checks with Black
   - Import ordering with isort
   - Linting with Flake8
   - Type checking with mypy
   - Security analysis with Bandit
   - Complexity analysis with Radon

2. **Testing**
   - Automated tests with pytest
   - Coverage reporting with pytest-cov
   - Coverage results uploaded to Codecov

3. **Build Validation**
   - Script compilation verification

The pipeline runs automatically on:
- Every push to the main branch
- All pull requests
- Manual trigger via GitHub Actions interface

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
