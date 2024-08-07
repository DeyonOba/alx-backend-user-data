#!/usr/bin/env python3
"""Module containing BasicAuth functionality.
"""
from api.v1.auth.auth import Auth
import re


class BasicAuth(Auth):
    """Class BasicAuth"""
    def extract_base64_authorization_header(
         self, authorization_header: str
    ) -> str:
        """
        Gets the Base64 part of the Authorization header
        for a Basic Authentication.
        """
        # pattern = r"Basic\s+(.+)"
        # PATTERN = re.compile(pattern)
        # if type(authorization_header) is str:
        #     match = re.match(PATTERN, authorization_header)
        #     if match:
        #         return match.group(1)
        # return None
        # Solution below is still correct but I wanted to try out 
        # regex instead
        if (
            type(authorization_header) is str and
            authorization_header.startswith("Basic ")
            ):
            return authorization_header.split(" ")[-1].strip()
        return None
