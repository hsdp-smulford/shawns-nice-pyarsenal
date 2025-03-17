#!/usr/bin/env python3

"""
Example demonstrating the use of the logger module.

This script demonstrates various features of the logger module including:
- Basic logging
- File logging
- JSON formatted logging
- Different log levels
"""

import os
import sys
import tempfile
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from common.logger import add_file_handler, get_logger


def demonstrate_basic_logging():
    """Demonstrate basic console logging."""
    print("\n=== Basic Logging ===")

    # Create a simple logger
    logger = get_logger("basic_example")

    # Log messages at different levels
    logger.debug("This is a DEBUG message (won't show with default INFO level)")
    logger.info("This is an INFO message")
    logger.warning("This is a WARNING message")
    logger.error("This is an ERROR message")

    # Create a logger with DEBUG level
    debug_logger = get_logger("debug_example", level="DEBUG")
    debug_logger.debug("This DEBUG message will show because we set level=DEBUG")
    debug_logger.info("This INFO message will also show")


def demonstrate_file_logging():
    """Demonstrate logging to a file."""
    print("\n=== File Logging ===")

    # Create a temporary directory for logs
    temp_dir = tempfile.mkdtemp()
    log_file = os.path.join(temp_dir, "example.log")

    # Create logger and add file handler
    logger = get_logger("file_example", level="DEBUG")
    add_file_handler(logger, log_file, level="DEBUG")

    # Log some messages
    logger.debug("Debug message - will be in console and file")
    logger.info("Info message - will be in console and file")
    logger.warning("Warning message - will be in console and file")

    # Show the content of the log file
    print(f"\nLog file created at: {log_file}")
    print("Log file contents:")
    with open(log_file, "r") as f:
        print(f.read())


def demonstrate_json_logging():
    """Demonstrate JSON formatted logging."""
    print("\n=== JSON Formatted Logging ===")

    # Create a logger with JSON formatting
    logger = get_logger("json_example", json_format=True)

    # Log some messages
    logger.info("This message will be formatted as JSON")

    # Log with extra context data (avoid reserved field names)
    logger.warning(
        "Processing failed",
        extra={
            "user_id": 12345,
            "process_name": "data_import",  # Avoid using 'process' (reserved)
            "status": "failed",
            "elapsed_time": 0.125,
        },
    )


def demonstrate_multiple_loggers():
    """Demonstrate using multiple loggers for different components."""
    print("\n=== Multiple Loggers ===")

    # Create loggers for different components
    api_logger = get_logger("api")
    db_logger = get_logger("database")
    ui_logger = get_logger("ui")

    # Simulate application flow with different loggers
    api_logger.info("API request received: GET /users/123")
    db_logger.info("Executing query: SELECT * FROM users WHERE id = 123")
    db_logger.info("Query returned 1 row")
    api_logger.info("API request completed in 0.23s")
    ui_logger.info("Rendering user profile page")


def main():
    """Run all demonstrations."""
    print("Logger Module Examples")
    print("=====================\n")

    demonstrate_basic_logging()
    demonstrate_file_logging()
    demonstrate_json_logging()
    demonstrate_multiple_loggers()

    print("\nAll examples completed.")


if __name__ == "__main__":
    main()
