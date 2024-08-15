#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Converts password to a salted hashed password.

    Check if parameter `password` is a valid string, then convert
    the string to "utf-8" encoded byte string. Use `bcrypt.gensalt`
    to an extra layer of randomly generated string would be added
    to the password. Finally the passed is hashed using
    `bcrypt.hashpw`.

    Args:
        password(str): String contain a password

    Returns:
        hash_password(bytes): Salted hashed password
    """
    if type(password) is str:
        bstring = password.encode('utf-8')

        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(bstring, salt)
        return hash_password
