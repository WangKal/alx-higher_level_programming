#!/usr/bin/python3
"""Module 3-to_json_string.
"""


import json


def to_json_string(my_obj):
    """Returns JSON of my_obj.
    Args:
        - my_obj: string to represent
    Returns: JSON
    """

    return json.dumps(my_obj)
