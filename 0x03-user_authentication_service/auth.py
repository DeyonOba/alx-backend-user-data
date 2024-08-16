#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Use the email and password given to register a user.

        Args:
            email(str): User's email.
            password(str): User's password

        Returns:
            user(User): User object.

        Raises:
            ValueError: If email already exists in db.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            user = None

        if user:
            raise ValueError(f"User {email} already exists")

        hashed_password = _hash_password(password)

        user = self._db.add_user(email, hashed_password.decode('utf-8'))
        return user

    def valid_login(email: str, password: str) -> bool:
        """
        Finds user in database using the email, check if the hashed
        password is a match with the password given.

        Args:
            email(str): User's email
            password(str): User's password

        Returns:
            bool: True if they is a user with the same hashed password,
                False if there is not.
        """
        try:
            user = self._db.find_user_by(email)
        except ValueError:
            return False
        hashed_pwd = user.hashed_password.encode("utf-8")

        if bcrypt.checkpw(password.encode("utf-8"), hashed_pwd):
            return True
        else:
            return False
