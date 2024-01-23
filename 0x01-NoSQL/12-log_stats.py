#!/usr/bin/env python3
""" this module return status log"""
from pymongo import MongoClient


def get_log_stat(mongo_collection):
    """get the start of nginx log"""
    log_count = mongo_collection.count()

    print(f'{log_count} logs')
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        method_count = log_count({'method': method})
        print(f'\tmethod {method}: {method_count}')

    get_count = log_count({'method': 'GET', "path": "/status"})
    print(f'{get_count} status check')
