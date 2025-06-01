import json


def load_in_json(path: str, data: dict) -> None:
    with open(path, 'w') as fp:
        json.dump(data, fp)


def load_from_json(path: str) -> dict:
    with open(path, 'r') as json_file:
        json_data = json.load(json_file)
        return json_data


def load_from_txt(path: str, enc: str = 'utf-8')-> str:
    with open(path, 'r', encoding=enc) as file:
        data = file.read()
        return data


def load_in_txt(data: str, path: str, enc: str = 'utf-8')-> None:
    with open(path, 'w', encoding= enc) as file:
        file.write(data)


def load_bytes_in(data: bytes, path:str)-> None:
    with open(path, 'wb') as file:
        file.write(data)


def load_bytes_from(path:str)-> bytes:
    with open(path, 'rb') as file:
        data = file.read()
        return data
