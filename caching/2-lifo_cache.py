#!/usr/bin/env python3
"""Basic cache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """init"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return None
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            print("DISCARD: {}".format(last_key))
            del self.cache_data[last_key]
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
