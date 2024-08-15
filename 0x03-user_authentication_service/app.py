#!/usr/bin/env python3
"""
Basic Flask app module.
"""
from flask import Flask, jsonify

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
