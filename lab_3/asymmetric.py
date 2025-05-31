from cryptography.hazmat.primitives.asymmetric import rsa


def generate_keys() -> (str, str):
    return 'public', 'private'


def encrypt(text: str,public_key: rsa.RSAPublicKey) -> bytes:
    return 'encrypted text'.encode('utf-8')


def decrypt(text: str, private_key: rsa.RSAPrivateKey) -> bytes:
    return 'decrypted text'.encode('utf-8')


def key_serialization(key: str, save_path: str) -> None:
    a = 3
