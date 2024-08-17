#!/usr/bin/env python3
"""
Basic Flask app module.
"""
from flask import (
    Flask,
    jsonify,
    request,
    abort,
    make_response
)

app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """
    Index endpoint

        GET "/"

        {"message": "Bienvenue"}
    """
    payload = {'message': 'Bienvenue'}
    return jsonify(payload)


@app.route("/users", methods=['POST'])
def register_users():
    """
    Handles user registeration.

    If user is not registered (i.e. not found in the database "a.db")
    payload should return a jsonified output.

        `Status Code`: 200 OK
        {"email": "<registered email>", "message": "user created"}

    If user already has already been registered with the same email
    payload should return a jsonified output.

        `Status Code`: 400 BAD REQUEST
        {"message": "email already registered"}
    """
    from auth import Auth

    Auth = Auth()
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = Auth.register_user(email, password)

    except ValueError:
        payload = {"message": "email already registered"}
        return jsonify(payload), 400

    payload = {
        "email": f"{email}",
        "message": "user created"
    }
    return jsonify(payload)


@app.route("/sessions", methods=['POST'])
def login():
    """
    Handles user login.

    The request is expected to contain form data with "email" and
    a "password" fields.
    If the login information is incorrect, use `flask.abort` to respond
    with a 401 HTTP status. Otherwise, create a new session for the user,
    and store it the session ID as a cookie with the key "session_Id" on
    the response and return a JSON payload of the form.

    POST '/session'

    Returns:
        response:
            SUCCESS: STATUS CODE 200 OK
                {"email": "<user email>", "message": "logged in"}
            ERROR: STATUS CODE 401 Unauthorized
    """
    from auth import Auth

    Auth = Auth()
    email = request.form.get("email")
    password = request.form.get("password")

    if not Auth.valid_login(email, password):
        abort(401)

    session_id = Auth.create_session(email)

    if not session_id:
        abort(401)

    payload = {"email": f"{email}", "message": "logged in"}
    response = make_response(jsonify(payload))
    response.set_cookie("session_id", session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
