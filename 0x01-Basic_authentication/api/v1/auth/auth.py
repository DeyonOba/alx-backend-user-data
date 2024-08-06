#!/usr/bin/env python3
"""Module containing Authentication functionality.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class manages API authentication."""
    def require_auth(
        self, path: str, excluded_paths: List[str]
    ) -> bool:
        """Not implemented yet."""
        return False

    def authorization_header(self, request=None) -> str:
        """Not implemented yet."""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """Not implemented yet."""
        return request
