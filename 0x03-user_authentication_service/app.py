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
