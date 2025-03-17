#!/usr/bin/env python3

"""Simple logger package."""

from common.logger.logger import JsonFormatter, add_file_handler, get_logger

__all__ = ["get_logger", "add_file_handler", "JsonFormatter"]
