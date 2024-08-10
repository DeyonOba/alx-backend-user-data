#!/usr/bin/env python3
"""Module containing SessionAuth functionality.
"""
from api.v1.auth.auth import Auth
import re
import base64
from typing import Tuple, Union, TypeVar
from models.user import User
import hashlib


class SessionAuth(Auth):
    """Class BasicAuth"""
    def extract_base64_authorization_header(
         self, authorization_header: str
    ) -> str:
        """
        Gets the Base64 part of the Authorization header
        for a Session Authentication.
        """
        pass
