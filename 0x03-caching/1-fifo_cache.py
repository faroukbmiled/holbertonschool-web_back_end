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
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_discarded = self.keys.pop(0)
                del self.cache_data[item_discarded]
                print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
