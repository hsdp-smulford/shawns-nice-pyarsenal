# Logger

A lightweight logging utility that simplifies Python's standard logging module with sensible defaults.

## Features

- Simple console logging with a clean format
- Optional file logging
- JSON formatting support for machine-readable logs
- Automatic logger caching to prevent duplicate handlers
- No external configuration files required

## Installation

The logger module is part of the `common` package and requires no additional dependencies beyond the Python standard library.

## Usage

### Basic Logging

Create a simple console logger:

```python
from common.logger import get_logger

# Create a logger with default INFO level
logger = get_logger("my_app")

# Log messages at different levels
logger.info("Application started")
logger.warning("Something may be wrong")
logger.error("An error occurred")
```

### Setting Log Level

Specify the log level when creating a logger:

```python
from common.logger import get_logger

# Create a logger with DEBUG level
logger = get_logger("my_app", level="DEBUG")

# Now debug messages will be shown
logger.debug("Detailed information for debugging")
```

### Adding File Logging

Add file logging to persist log messages:

```python
from common.logger import get_logger, add_file_handler

# Create a console logger first
logger = get_logger("my_app")

# Add a file handler
add_file_handler(logger, "/var/log/myapp/app.log")

# Log messages will now go to both console and file
logger.info("This message appears in both the console and the log file")
```

### JSON Formatted Logs

Enable JSON formatting for structured logging:

```python
from common.logger import get_logger, add_file_handler

# Create a logger with JSON output
logger = get_logger("audit", json_format=True)

# Add a JSON file handler for machine-readable logs
add_file_handler(logger, "/var/log/myapp/audit.log", json_format=True)

# Log messages (note: extra fields only appear in the JSON output)
logger.info("User login", extra={"user_id": 12345, "ip": "192.168.1.1"})
```

## API Reference

### get_logger(name, level="INFO", json_format=False)

Create and configure a logger with console output.

- **name**: Name of the logger
- **level**: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- **json_format**: Whether to use JSON formatting for logs
- **Returns**: Configured logger instance

### add_file_handler(logger, filepath, level="INFO", json_format=False)

Add a file handler to an existing logger.

- **logger**: The logger to add a handler to
- **filepath**: Path to the log file
- **level**: Logging level for this handler
- **json_format**: Whether to use JSON formatting
