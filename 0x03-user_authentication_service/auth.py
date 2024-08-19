#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import Union


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


def _generate_uuid() -> str:
    """
    Generate a string representation of a new UUID.
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
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
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        hashed_pwd = user.hashed_password.encode("utf-8")

        if bcrypt.checkpw(password.encode("utf-8"), hashed_pwd):
            return True
        else:
            return False

    def create_session(self, email: str) -> Union[str, None]:
        """
        Find user corresponding to the email passed, generate a new
        unique user identification (UUID) and store it in the database
        attribute `session_id`.

        Args:
            email(str): User's email

        Returns:
            session_id(Union[str, None])
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(
                int(user.id),
                session_id=session_id
            )
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """
        Get User associated with session id passed.

        Args:
            session_id(str): User session id

        Returns:
            Union[User, None]
        """
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Update the corresponding user id user's session id to None
        within the database.
        """
        if not user_id:
            return None
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except NoResultFound:
            return
