#!/usr/bin/env python3
"""python mysql"""


def list_all(mongo_collection):
    """python mysql"""
    if mongo_collection is not None:
        return []
    return list(mongo_collection.find())
