#!/usr/bin/env python3
"""this module updata topics"""


def update_topics(mongo_collection, name, topics):
    """this method update name of a collection and topis"""
    query_filter = {'name': name}
    update_value = {"$set": {'topics': topics}}

    output = mongo_collection.update_many(query_filter, update_value)
