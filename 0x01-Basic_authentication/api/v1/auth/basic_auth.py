#!/usr/bin/env python3
"""Module containing BasicAuth functionality.
"""
from api.v1.auth.auth import Auth
import re
import base64
from typing import Tuple, Union, TypeVar
from models.user import User
import hashlib


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

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> User:
        """
        Get User instance based on email and password.
        """
        if type(user_email) is str and type(user_pwd) is str:
            valid_password = (
                hashlib.sha256(user_pwd.encode())
                .hexdigest().lower()
            )
            user_details = {
                "email": user_email,
                "password": valid_password
            }
            User.load_from_file()
            attributes = User.search(attributes=user_details)
            if attributes:
                obj = attributes[0].__dict__
                return User.get(obj["id"])
        return None

    def current_user(self, request=None) -> User:
        """Get current users object from storage."""
        if not request:
            return None
        auth_header = self.authorization_header(request)
        if not auth_header:
            return None
        extract_base64_auth_header = (
            self.extract_base64_authorization_header(auth_header)
            )
        if not extract_base64_auth_header:
            return None
        decode_base64_auth_header = (
            self.decode_base64_authorization_header(
                extract_base64_auth_header
            )
        )
        if not decode_base64_auth_header:
            return None
        extract_user_credential = self.extract_user_credentials(
            decode_base64_auth_header
        )
        if not extract_user_credential[0]:
            return None
        user_object_credential = self.user_object_from_credentials(
            *extract_user_credential
        )
        if not user_object_credential:
            return None
        return user_object_credential
