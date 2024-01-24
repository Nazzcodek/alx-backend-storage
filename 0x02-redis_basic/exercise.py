#!/usr/bin/env python3
"""this is a redis catche module"""
from uuid import uuid4
import redis
from typing import Union


class Cache:
    """this is a the cache object"""
    def __init__(self):
        """the init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """this method store the data"""
        random_key = str(uuid4())
        self._redis.set(random_key, data)

        return random_key
