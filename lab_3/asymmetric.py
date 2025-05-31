from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

import file_utils


def generate_keys() -> (bytes, bytes):
    key = rsa.generate_private_key(public_exponent=65537,
                                   key_size=2048)

    return key, key.public_key()


def encrypt(text: bytes, public_key: rsa.RSAPublicKey) -> bytes:
    return public_key.encrypt(
        text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None)
    )


def decrypt(text: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
    return private_key.decrypt(
        text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None)
    )


def public_key_serialization(key: rsa.RSAPublicKey, save_path: str) -> None:
    serialization_data = key.public_bytes(encoding=serialization.Encoding.PEM,
                                          format=serialization.PublicFormat.SubjectPublicKeyInfo)

    file_utils.load_bytes_in(save_path, serialization_data)


def private_key_serialization(key: rsa.RSAPrivateKey, save_path: str) -> None:
    serialization_data = key.private_bytes(encoding=serialization.Encoding.PEM,
                                          format=serialization.PrivateFormat.TraditionalOpenSSL,
                                          encryption_algorithm=serialization.NoEncryption())

    file_utils.load_bytes_in(save_path, serialization_data)
