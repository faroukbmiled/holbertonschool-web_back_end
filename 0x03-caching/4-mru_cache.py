#!/usr/bin/env python3
"""Basic cache"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """init"""
        super().__init__()
        self.recent_keys = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            raise ValueError("Key and item cannot be None")
        if key in self.recent_keys:
            self.recent_keys.pop(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = next(iter(self.recent_keys))
            print("DISCARD: {}".format(mru_key))
            self.recent_keys.pop(mru_key)
            self.cache_data.pop(mru_key)
        self.cache_data[key] = item
        self.recent_keys[key] = 0

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.recent_keys.pop(key)
        self.recent_keys[key] = 0
        return self.cache_data[key]
