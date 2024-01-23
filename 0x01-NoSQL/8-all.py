#!/usr/bin/env python3
"""this module list all collection in mongodb"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """this fumction return the count of db collection"""
    docs = mongo_collection.find()

    if docs.count() == 0:
        return []

    return docs
