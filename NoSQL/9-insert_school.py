#!/usr/bin/env python3
"""python mysql"""


def insert_school(mongo_collection, **kwargs):
    """python mysql"""
    return mongo_collection.insert_one(kwargs).inserted_id
