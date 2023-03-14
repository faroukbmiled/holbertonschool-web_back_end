#!/usr/bin/env python3
"""python mysql"""


def schools_by_topic(mongo_collection, topic):
    """python mysql"""
    return mongo_collection.find({"topics": topic})
