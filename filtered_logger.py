#!/usr/bin/env python3
"""
Module contains a function called `filter_datum` that returns the log
message obfuscated.

The function uses regex to replace occurrences of certain field values.
"""
import re
from typing import List


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    seperator: str
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
        pattern = re.compile(f"({field}=)([^{seperator}]*)")
        message = re.sub(pattern, r"\1" + redaction, message)
    return message


if __name__ == "__main__":
    fields = ["password", "date_of_birth"]
    messages = [
        "name=egg;email=eggmin@eggsample.com;password=eggcellent;\
date_of_birth=12/12/1986;",
        "name=bob;email=bob@dylan.com;password=bobbycool;\
date_of_birth=03/04/1993;"
    ]

    for message in messages:
        print(filter_datum(fields, 'xxx', message, ';'))
