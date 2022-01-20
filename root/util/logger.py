#!/usr/bin/env python3

""" File with the logger class used by the various files """

import logging
import configparser
from logging.handlers import RotatingFileHandler


CONFIG = configparser.ConfigParser()
CONFIG.read("logger.conf")
FORMAT = "%(asctime)-15s %(levelname)s:%(funcName)-8s %(message)s"
FILE = "server.log"
LEVEL = logging.INFO
logging.basicConfig(
    format=FORMAT,
    level=logging.INFO,
    handlers=[RotatingFileHandler("server.log", maxBytes=10000000, backupCount=10)],
)


def info(message: str):
    """Log a message of at level INFO

    Args:
        message ([str]): The message to log
    """
    logging.info(message)


def error(message: str):
    """Log a message of at level ERROR

    Args:
        message ([str]): The message to log
    """
    logging.error(message)


def warn(message: str):
    """Log a message of at level WARNING

    Args:
        message ([str]): The message to log
    """
    logging.warning(message)


def debug(message: str):
    """Log a message of at level DEBUG

    Args:
        message ([str]): The message to log
    """
    logging.debug(message)


def log(level: int, message: str):
    """
    Args:
        level ([str]): The logging level
        message ([str]): The message to log
    """
    logging.log(level, message)