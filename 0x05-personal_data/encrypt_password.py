#!/usr/bin/env python3
"""password encrypter"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hash_password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """is_valid"""
    return bcrypt.checkpw(password.encode(), hashed_password)
