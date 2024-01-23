#!/usr/bin/env python3
"""students average score module"""


def top_students(mongo_collection):
    """this methode returns students sorted average score"""
    sort_score = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "avgScore": {"$avg": "$topics.score"}
                }
            },
        {"$sort": {"avgScore": -1}}
        ])
    return sort_score
