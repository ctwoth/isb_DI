import json


def load_in_json(path: str, data: dict) -> None:
    with open(path, 'w') as fp:
        json.dump(data, fp)


def load_from_json(path: str) -> str:
    with open(path, 'r') as json_file:
        json_data = json.load(json_file)
        return json_data


def load_from_txt(path: str)-> None:
    with open(path, 'r') as file:
        data = file.read()
        return data


def load_in_txt(path: str, data: str)-> None:
    with open(path, 'w') as file:
        file.write(data)