#!/usr/bin/env python3
"""this module is use to insert into mongodb collection"""


def insert_school(mongo_collection, **kwargs):
    """this method insert into mongo_collection"""
    docs = mongo_collection.insert(kwargs)
    return docs
