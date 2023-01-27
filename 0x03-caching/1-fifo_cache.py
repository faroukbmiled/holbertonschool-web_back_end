#!/usr/bin/env python3
"""Basic cache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache"""

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item in the cache"""

        if not key or not item:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1\
                and (key not in self.cache_data.keys()):
            print('DISCARD: {}'.format(self.keys[0]))
            del self.cache_data[self.keys[0]]
            self.keys = self.keys[1:]
        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
