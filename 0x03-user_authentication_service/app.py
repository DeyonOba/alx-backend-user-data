#!/usr/bin/env python3
"""
Basic Flask app module.
"""
from flask import Flask, jsonify, request

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
