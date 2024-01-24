#!/usr/bin/env python3
"""this is a redis catche module"""
from uuid import uuid4
import redis
from typing import Union, Callable


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

    def get(self,
            key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        """Get cache data"""
        result = self._redis.get(key)
        if fn:
            result = fn(result)
        return result

    def get_str(self, key: str) -> str:
        """Get cache string."""
        result = self._redis.get(key).decode('utf-8')
        return result

    def get_int(self, key: str) -> int:
        """Get cache int"""
        result = self._redis.get(key)
        try:
            result = int(result.decode('utf-8'))
        except Exception:
            result = 0
        return result
