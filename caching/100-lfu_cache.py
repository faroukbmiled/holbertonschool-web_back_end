#!/usr/bin/env python3
"""Basic cache"""
from base_caching import BaseCaching
import time
import collections


class LFUCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """init"""
        super().__init__()
        self.frequency = collections.defaultdict(int)
        self.time_stamp = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu_key, lfu_value = min(self.frequency.items(
            ), key=lambda x: (x[1], self.time_stamp[x[0]]))
            self.cache_data.pop(lfu_key)
            self.frequency.pop(lfu_key)
            self.time_stamp.pop(lfu_key)
            print("DISCARD:", lfu_key)
        self.cache_data[key] = item
        self.frequency[key] += 1
        self.time_stamp[key] = time.time()

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.time_stamp[key] = time.time()
        return self.cache_data[key]
