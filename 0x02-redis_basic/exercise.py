#!/usr/bin/env python3
"""this is a redis catche module"""
from uuid import uuid4
import redis
from functools import wraps
from typing import Union, Optional, Callable


def count_calls(method: Callable) -> Callable:
    """this is a count method"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """this method wrap the count decorator"""
        key = method.__qualname__
        self._redis.incr(key)

        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """this method store the history of redis call"""
    key = method.__qualname__
    key_inputs = key + ":inputs"
    key_outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ this method wrap the history decorator"""
        self._redis.rpush(key_inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(key_outputs, str(data))
        return data

    return wrapper


def replay(method: Callable) -> None:
    """this method replay the redis history"""
    name = method.__qualname__

    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")

    print(f"{name} was called {calls} times:")

    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)

    for i, o in zip(inputs, outputs):
        _input = i.decode("utf-8")
        _output = o.decode("utf-8")
        print(f"{name}(*{_input}) -> {_output}")


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
