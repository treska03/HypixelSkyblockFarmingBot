from pathlib import Path
import json
import os

def get_real_path(file):
    dir_path = os.path.dirname(os.path.abspath(os.path.realpath(__file__))).strip("\packages")
    return os.path.join(dir_path, file)

def json_unpack(file):
    try:
        path_to_file = get_real_path()
        with open(path_to_file, 'r') as f:
            f = json.load(f)
            return f
    except FileNotFoundError:
        raise FileNotFoundError(f"{file} cannot be found.")

def change_in_json(file, key, new_value):
    try:
        path_to_file = get_real_path(file)
        with open(path_to_file, "r") as f:
            data = json.load(f)
            print(data)
            data[key] = new_value
        with open(path_to_file, "w") as f:
            json.dump(data, f, indent=4)

    except KeyError:
        raise KeyError("config.json file wrongly configured.")
