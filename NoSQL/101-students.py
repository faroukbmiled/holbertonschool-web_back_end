#!/usr/bin/env python3
"""python mysql"""


def top_students(mongo_collection):
    """python mysql"""
    return mongo_collection.aggregate([
        {
            "$project": {"name": "$name",
                         "averageScore": {"$avg": "$topics.score"}}
        },
        {"$sort": {"averageScore": -1}}
    ])
