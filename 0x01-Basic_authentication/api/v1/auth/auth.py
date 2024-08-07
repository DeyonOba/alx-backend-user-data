#!/usr/bin/env python3
"""Module containing Authentication functionality.
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Class manages API authentication."""
    def require_auth(
        self, path: str, excluded_paths: List[str]
    ) -> bool:
        """Not implemented yet."""
        if not path or not excluded_paths:
            return True

        for x_path in excluded_paths:
            if path.rstrip('/') == x_path.rstrip('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Not implemented yet."""
        if request:
            return request.headers.get('Authorization')
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """Not implemented yet."""
        auth_user = self.authorization_header(request)
        # print(f"{auth_user=}")
        if auth_user == os.getenv("AUTH_TYPE"):
            return auth_user
        return None
