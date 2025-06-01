from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os



def generate_key(key_len):
    if key_len not in [64, 128, 192]:
        raise ValueError("Wrong key length")

    return os.urandom(key_len//8)


def encrypt(data: bytes, key: bytes):
    iv = os.urandom(8)

    padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()

    encryptor = Cipher(algorithms.TripleDES(key), modes.CBC(iv)).encryptor()
    encrypted_data = iv + encryptor.update(padded_data)
    encrypted_data += encryptor.finalize()

    return encrypted_data


def decrypt(encrypted_data: bytes, key: bytes) -> bytes:
    iv = encrypted_data[:8]
    encrypted_data = encrypted_data[8:]

    decryptor = Cipher(algorithms.TripleDES(key), modes.CBC(iv)).decryptor()
    decrypted_text = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
    decrupted_data = unpadder.update(decrypted_text) + unpadder.finalize()

    return decrupted_data
