#!/usr/bin/env python3
"""Module containing BasicAuth functionality.
"""
from api.v1.auth.auth import Auth
import re
import base64
from typing import Tuple, Union


class BasicAuth(Auth):
    """Class BasicAuth"""
    def extract_base64_authorization_header(
         self, authorization_header: str
    ) -> str:
        """
        Gets the Base64 part of the Authorization header
        for a Basic Authentication.
        """
        pattern = r"Basic\s+(.+)"
        PATTERN = re.compile(pattern)
        if type(authorization_header) is str:
            match = re.match(PATTERN, authorization_header)
            if match:
                return match.group(1)
        return None
        # Solution below is still correct but I wanted to try out
        # regex instead
        # if (
        #     type(authorization_header) is str and
        #     authorization_header.startswith("Basic ") and
        #     authorization_header.count(" ") == 1
        # ):
        #     return authorization_header.split(" ")[-1].strip()
        # return None

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Extracts the decoded value of a Base64 string"""

        if type(base64_authorization_header) is str:
            if self.extract_base64_authorization_header(
                base64_authorization_header
            ):
                base64_authorization_header = (
                    self.extract_base64_authorization_header(
                        base64_authorization_header
                    )
                )
            try:
                header_encode_str = base64_authorization_header.encode("ascii")
                output = base64.b64decode(header_encode_str, validate=True)
                return output.decode("ascii")
            except Exception:
                pass
        return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Union[Tuple[str, str], Tuple[None, None]]:
        """
        Extracts users email and password from the Base64 decoded value.
        """
        if type(decoded_base64_authorization_header) is str:
            if (
                decoded_base64_authorization_header.count(":") == 1
                and not decoded_base64_authorization_header.startswith(":")
                and not decoded_base64_authorization_header.endswith(":")
            ):
                return tuple(decoded_base64_authorization_header.split(":"))
        return None, None
