#!/usr/bin/env python3
"""Module containing Authentication functionality.
"""
from flask import request
from typing import List
import os
# User = Typevar("User")


class Auth:
    """Class manages API authentication."""
    def require_auth(
        self, path: str, excluded_paths: List[str]
    ) -> bool:
        """Not implemented yet."""
        if not path or not excluded_paths:
            return True

        for x_path in excluded_paths:
            if x_path.endswith("*"):
                return x_path[:-1] not in path
            elif path.rstrip('/') == x_path.rstrip('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Not implemented yet."""
        if request:
            return request.headers.get('Authorization')
        return request

    def current_user(self, request=None):
        """
        Gets the current user from the request Authentication type.
        """
        auth_user = self.authorization_header(request)
        # print(f"{auth_user=}")
        # print("User:", os.getenv('AUTH_TYPE'))
        if auth_user == os.getenv("AUTH_TYPE"):
            return auth_user
        return None
