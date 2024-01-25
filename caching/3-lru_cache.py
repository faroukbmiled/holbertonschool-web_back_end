#!/usr/bin/env python3
"""Basic cache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """init"""
        super().__init__()
        self.recent_keys = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return None
        if key in self.recent_keys:
            self.recent_keys.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.recent_keys.pop(0)
            print("DISCARD: {}".format(lru_key))
            del self.cache_data[lru_key]
        self.cache_data[key] = item
        self.recent_keys.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.recent_keys.remove(key)
        self.recent_keys.append(key)
        return self.cache_data[key]
