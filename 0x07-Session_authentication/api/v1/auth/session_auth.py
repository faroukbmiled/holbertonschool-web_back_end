#!/usr/bin/env python3
"""
auth module for the API
"""
from api.v1.auth.auth import Auth
from uuid import uuid4

from models.user import User


class SessionAuth(Auth):
    """ SessionAuth Class """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ session comment """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        sess_id = str(uuid4())
        SessionAuth.user_id_by_session_id[sess_id] = user_id
        return sess_id

    @staticmethod
    def user_id_for_session_id(session_id: str) -> str:
        """ user_id comment """
        return SessionAuth.user_id_by_session_id.get(session_id)

    @classmethod
    def current_user(cls, request=None):
        """ comment """
        session_cookie = cls.session_cookie(request)
        if session_cookie is None:
            return None
        _id = cls.user_id_for_session_id(session_cookie)
        return User.get(_id)
