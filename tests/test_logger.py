#!/usr/bin/env python3

"""Test the simplified logger module."""

import json
import logging
import os
import shutil
import tempfile
import unittest

from common.logger.logger import JsonFormatter, add_file_handler, get_logger


class TestLogger(unittest.TestCase):
    """Test the logger functionality."""

    def setUp(self):
        """Set up test environment."""
        # Create temporary directory for log files
        self.test_dir = tempfile.mkdtemp()

        # Reset root logger
        root = logging.getLogger()
        for handler in root.handlers[:]:
            root.removeHandler(handler)

    def tearDown(self):
        """Clean up after tests."""
        shutil.rmtree(self.test_dir)

    def test_get_logger(self):
        """Test getting a configured logger."""
        logger = get_logger("test_simple", level="DEBUG")

        # Check logger level
        self.assertEqual(logger.level, logging.DEBUG)

        # Check handlers
        self.assertEqual(len(logger.handlers), 1)
        self.assertIsInstance(logger.handlers[0], logging.StreamHandler)

    def test_logger_caching(self):
        """Test that loggers are cached."""
        logger1 = get_logger("test_cache")
        logger2 = get_logger("test_cache")

        # Loggers should be the same instance
        self.assertIs(logger1, logger2)

    def test_add_file_handler(self):
        """Test adding a file handler to a logger."""
        # Create a logger with DEBUG level
        logger = get_logger("test_file", level="DEBUG")
        log_file = os.path.join(self.test_dir, "logs", "test.log")

        # Add file handler with DEBUG level
        add_file_handler(logger, log_file, level="DEBUG")

        # Check handlers
        self.assertEqual(len(logger.handlers), 2)
        self.assertIsInstance(logger.handlers[1], logging.FileHandler)

        # Log some messages
        logger.debug("Debug message")
        logger.info("Info message")

        # Check log file contents
        with open(log_file, "r") as f:
            content = f.read()

        self.assertIn("Debug message", content)
        self.assertIn("Info message", content)

    def test_json_formatter(self):
        """Test the JSON formatter."""
        formatter = JsonFormatter()

        # Create a log record
        record = logging.LogRecord(
            name="test_json",
            level=logging.INFO,
            pathname=__file__,
            lineno=100,
            msg="Test message",
            args=(),
            exc_info=None,
        )

        # Format the record
        formatted = formatter.format(record)

        # Parse the JSON
        log_data = json.loads(formatted)

        # Check the fields
        self.assertEqual(log_data["name"], "test_json")
        self.assertEqual(log_data["level"], "INFO")
        self.assertEqual(log_data["message"], "Test message")
        self.assertEqual(log_data["path"], __file__)
        self.assertEqual(log_data["line"], 100)


if __name__ == "__main__":
    unittest.main()
