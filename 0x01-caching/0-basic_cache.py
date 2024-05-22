#!/usr/bin/env python3
""" Basecaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    defines a class for caching information in key-value pairs
    Methods:
        put(key, item) - stores a key-value pair
        get(key) - retrieves the value associated with a key
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        store a key-value pair
        Args:
        Key
        Item
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return value linked to key
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
