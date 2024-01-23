#!/usr/bin/env python3
"""module for mongo db match search"""


def schools_by_topic(mongo_collection, topic):
    """this method search school collection with a given topic"""
    search = mongo_collection.find({"topics": topic})

    return search
