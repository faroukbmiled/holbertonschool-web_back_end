#!/usr/bin/env python3
"""
auth module
"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from flask import jsonify, make_response, request

from models.user import User


class SessionAuth(Auth):
    """SessionAuth"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create_session"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        sess_id = str(uuid4())
        SessionAuth.user_id_by_session_id[sess_id] = user_id
        return sess_id

    @staticmethod
    def user_id_for_session_id(session_id: str) -> str:
        """user_id_for_session_id"""
        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """current_user"""
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return None
        _id = self.user_id_for_session_id(session_cookie)
        return User.get(_id)
