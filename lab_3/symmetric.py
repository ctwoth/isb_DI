from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

import file_utils


def generate_key(key_len):
    if key_len not in [64, 128, 192]:
        raise ValueError("Wrong key length")

    return os.urandom(key_len)


def encrypt(key: bytes, data: bytes):
    iv = os.urandom(8)

    padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    encryptor = Cipher(algorithms.TripleDES(key), modes.CBC(iv)).encryptor()
    encrypted_data = iv + encryptor.update(padded_data) + encryptor.finalize()

    return encrypted_data


def decrypt(key: bytes, cipher_text: bytes) -> bytes:
    iv = cipher_text[:8]
    cipher_text = cipher_text[8:]

    decryptor = Cipher(algorithms.TripleDES(key), modes.CBC(iv)).decryptor()
    decrypted_text = decryptor.update(cipher_text) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
    decrupted_data = unpadder.update(decrypted_text) + unpadder.finalize()

    return decrupted_data
