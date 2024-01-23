#!/usr/bin/env python3
""" 8-all.py module """


def list_all(mongo_collection) -> list:
    """  function that lists all documents in a collection """
    return mongo_collection.find()
