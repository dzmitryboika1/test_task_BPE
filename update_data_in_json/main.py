"""
Json file is given. Find all the "updated" fields in it and change
the value to the current date and time in ISO 8601 format.
"""

import json
from datetime import datetime


def update_json_with_current_time(json_obj):
    """The function  checks if a given value is a dictionary or a list.
    If it is a dictionary, it calls recursively the same function on its values.
    If it is a list, it iterates over each element and recursively call the function on each element.
    It can handle any level of nesting in the JSON data."""
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            if key == "updated":
                json_obj[key] = datetime.utcnow().isoformat()
            else:
                update_json_with_current_time(value)
    elif isinstance(json_obj, list):
        for item in json_obj:
            update_json_with_current_time(item)
    return json_obj


def main():
    with open('source.json', 'r') as f:
        obj = update_json_with_current_time(json.load(f))
    with open('source.json', 'w') as f:
        json.dump(obj, f)


if __name__ == '__main__':
    main()
