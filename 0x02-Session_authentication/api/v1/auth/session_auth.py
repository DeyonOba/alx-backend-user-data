#!/usr/bin/env python3
"""Module containing SessionAuth functionality.
"""
from api.v1.auth.auth import Auth
import re
import uuid
import base64
from typing import Tuple, Union, TypeVar
from models.user import User
import hashlib


class SessionAuth(Auth):
    """Class Session Auth"""
    user_id_by_session_id: dict = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a `user_id`.
        """
        if type(user_id) is str:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id.update({session_id: user_id})
            return session_id
        return None
