#!/usr/bin/env python3
""" Basecaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class for caching
    """

    def __init__(self):
        """
        Initializes the class
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item by key
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
