from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

import symmetric
import asymmetric
import file_utils


def generate_keys(key_len: int, symm_path: str, public_path: str, private_path: str) -> None:
    public_key, private_key = asymmetric.generate_keys()
    sym_key =                 symmetric.generate_key(key_len)

    asymmetric.public_key_serialization(public_key, public_path)
    asymmetric.private_key_serialization(private_key, private_path)

    encr_sym_key = asymmetric.encrypt(sym_key, public_key)

    file_utils.load_bytes_in(symm_path, encr_sym_key)


def encryption(text_path: str, symm_key_path: str, private_key_path: str, save_path: str) -> None:
    encrypted_symm_key = file_utils.load_bytes_from(symm_key_path)
    private_key =        load_pem_private_key(file_utils.load_bytes_from(private_key_path),None)
    text =               file_utils.load_from_txt(text_path)

    symmetric_key = asymmetric.decrypt(encrypted_symm_key, private_key)

    encrypted_text = symmetric.encrypt(text.encode('utf-8'), symmetric_key)
    file_utils.load_in_txt(encrypted_text.decode('utf-8'), save_path)


def decryption(text_path: str, symm_key_path: str, private_key_path: str, save_path: str) -> None:
    encrypted_symm_key = file_utils.load_bytes_from(symm_key_path)
    private_key =        load_pem_private_key(file_utils.load_bytes_from(private_key_path),None)
    text =               file_utils.load_from_txt(text_path)

    symmetric_key = asymmetric.decrypt(encrypted_symm_key, private_key)

    decrypted_text = symmetric.decrypt(text.encode('utf-8'), symmetric_key)
    file_utils.load_in_txt(decrypted_text.decode('utf-8'), save_path)
