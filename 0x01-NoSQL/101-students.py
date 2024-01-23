#!/usr/bin/env python3
"""students average score module"""


def top_students(mongo_collection):
    """this methode returns students sorted average score"""
    sort_score = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
                }
            },
        {"$sort": {"averageScore": -1}}
        ])
    return sort_score
