#!/usr/bin/env python3
"""
Module contains a function called `filter_datum` that returns the log
message obfuscated.

The function uses regex to replace occurrences of certain field values.
"""
import re
import logging
from typing import List



class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        Implement the format method to filter values
        in incoming log records using filter_datum.
        """
        


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Replace certain field values using reqular expression.

    Args:
        fields (List[str]): A list of strings representing all fields
        to obfuscate.
        redaction (str): A string representing by what the field will
        obfuscated.
        message (str): A string representing the log line.
        seperator (str): A string representing by which character is
        separating all fields in the log line.

    Returns:
        str: Obfuscated string
    """
    for field in fields:
        pattern = f"({field}=)([^{separator}*])"
        message = re.sub(pattern, r"\1" + redaction, message)
    return message
