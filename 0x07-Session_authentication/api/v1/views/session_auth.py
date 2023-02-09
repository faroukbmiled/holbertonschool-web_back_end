#!/usr/bin/env python3
"""
auth module
"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from flask import jsonify, make_response, request
from .__init__ import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    email = request.form.get('email')
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    user = User.search(email)
    if user is None:
        return jsonify({"error": "no user found for this email"}), 404

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    if session_id is None:
        return jsonify({"error": "cannot create session"}), 500

    response = make_response(user.to_json())
    response.set_cookie(app_views.config['SESSION_NAME'], session_id)
    return response
