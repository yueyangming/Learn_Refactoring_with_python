import json


def load_json(json_path):
    with open(json_path, 'r') as f_json:
        result = json.load(f_json)
    return result
