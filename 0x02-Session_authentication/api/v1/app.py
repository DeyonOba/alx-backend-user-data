#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request, logging
from flask_cors import (CORS, cross_origin)
import os
import sys

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = os.getenv('AUTH_TYPE')
if auth_type == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
elif auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.before_request
def handle_before_request():
    """
    Handles authentication before request.
    """
    # print("Handle authorization before request.")

    if auth:
        exclude_path = [
            '/api/v1/status/',
            '/api/v1/unauthorized/',
            '/api/v1/forbidden/',
            '/api/v1/auth_session/login/',
        ]
        path = auth.require_auth(request.path, exclude_path)
        # print(f"{path=}")
        if path:
            auth_type = auth.authorization_header(request)
            session_cookie = auth.session_cookie(request)
            # print(f"{auth_type=}")
            if auth_type is None and session_cookie is None:
                abort(401)
            current_user = auth.current_user(request)
            # print(f"{current_user=}")
            if not current_user:
                abort(403)
        request.current_user = auth.current_user(request)


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Unauthorized access
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden access
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
