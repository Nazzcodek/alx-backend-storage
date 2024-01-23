#!/usr/bin/env python3
""" this module return status log"""
from pymongo import MongoClient


def get_log_stats(mongo_collection):
    """get the start of nginx log"""
    log_count = mongo_collection.count_documents({})

    print(f'{log_count} logs')
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        method_count = mongo_collection.count_documents({'method': method})
        print(f'\tmethod {method}: {method_count}')

    get_count = mongo_collection.count_documents(
            {'method': 'GET', "path": "/status"}
            )
    print(f'{get_count} status check')

    top_ips = mongo_collection.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    print("IPs:")
    for ip in top_ips:
        _ip = ip.get("ip")
        _count = ip.get("count")
        print(f'\t{_ip}: {_count}')


if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017')
    nginx_collection = client.logs.nginx

    get_log_stats(nginx_collection)
