import json


USERS_FILE = 'data/users.json'
ROOMS_FILE = 'data/rooms.json'


def load_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
