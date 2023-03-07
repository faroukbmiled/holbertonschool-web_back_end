#!/usr/bin/env python3
"""exercise.py"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional, Any
from functools import wraps
from datetime import datetime


def call_history(method: Callable) -> Callable:
    """call_history"""
    key = method.__qualname__
    input = key + ":inputs"
    output = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ wrapped function """
        self._redis.rpush(input, str(args))
        out = method(self, *args, **kwds)
        self._redis.rpush(output, str(out))
        return out

    return wrapper


def count_calls(method: Callable) -> Callable:
    """count_calls"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ wrap """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    """class Cache"""

    def __init__(self, name: str):
        """init"""
        self.name = name
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[int, float, str, bytes]) -> str:
        """store"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """get"""
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """get_str"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """get_int"""
        return self.get(key, int)


def replay(method: Callable):
    """replay"""
    key = method.__qualname__
    inputs = key + ":inputs"
    output = key + ":outputs"
    plugin = method.__self__._redis
    count = plugin.get(key).decode("utf-8")
    print("{} was called {} times:".format(key, count))
    In = plugin.lrange(inputs, 0, -1)
    Out = plugin.lrange(output, 0, -1)
    zipped = list(zip(In, Out))
    for k, v in zipped:
        attr, data = k.decode("utf-8"), v.decode("utf-8")
        print("{}(*{}) -> {}".format(key, attr, data))
