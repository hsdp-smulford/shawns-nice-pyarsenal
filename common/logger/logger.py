#!/usr/bin/env python3

"""Provide simple logging functionality for the application."""

import json
import logging
import os
from typing import Dict

# Cache of configured loggers
_LOGGERS: Dict[str, logging.Logger] = {}


class JsonFormatter(logging.Formatter):
    """Format log records as JSON objects."""

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record as a JSON string."""
        log_data = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
            "path": record.pathname,
            "line": record.lineno,
        }

        # Add exception info if present
        if record.exc_info:
            log_data["exception"] = {
                "type": (
                    record.exc_info[0].__name__ if record.exc_info[0] else "Unknown"
                ),
                "message": str(record.exc_info[1]) if record.exc_info[1] else "",
            }

        return json.dumps(log_data)


def get_logger(
    name: str, level: str = "INFO", json_format: bool = False
) -> logging.Logger:
    """Get a configured logger with console output.

    Args:
        name: Name of the logger
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        json_format: Whether to use JSON formatting

    Returns:
        Configured logger instance
    """
    # Return cached logger if available
    if name in _LOGGERS:
        return _LOGGERS[name]

    # Create new logger
    logger = logging.getLogger(name)

    # Clear any existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Set level
    logger.setLevel(getattr(logging, level))
    logger.propagate = False  # Prevent propagation to root logger

    # Create console handler
    handler = logging.StreamHandler()
    handler.setLevel(getattr(logging, level))

    # Set formatter
    if json_format:
        handler.setFormatter(JsonFormatter())
    else:
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )

    # Add handler to logger
    logger.addHandler(handler)

    # Cache the logger
    _LOGGERS[name] = logger

    return logger


def add_file_handler(
    logger: logging.Logger,
    filepath: str,
    level: str = "INFO",
    json_format: bool = False,
) -> None:
    """Add a file handler to an existing logger.

    Args:
        logger: The logger to add a handler to
        filepath: Path to the log file
        level: Logging level for this handler
        json_format: Whether to use JSON formatting
    """
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)

    # Create file handler
    handler = logging.FileHandler(filepath)

    # Set level to the same level as logger if not explicitly overridden
    log_level = getattr(logging, level)
    handler.setLevel(log_level)

    # Set formatter
    if json_format:
        handler.setFormatter(JsonFormatter())
    else:
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )

    # Add handler to logger
    logger.addHandler(handler)
