def generate_keys() -> (str, str):
    return 'public', 'private'


def encrypt(text: str, public_key: str) -> str:
    return 'encrypted text'


def decrypt(text: str, private_key: str) -> str:
    return 'decrypted text'


def key_serialization(key: str, save_path: str) -> None:
    a = 3
