import symmetric
import asymmetric
import file_utils


def keys_generator(key_len: int, symm_path: str, public_path: str, private_path: str) -> None:
    public_key, private_key = asymmetric.generate_keys()
    sym_key =                  symmetric.generate_key(key_len)

    asymmetric.key_serialization(public_path, public_key)
    asymmetric.key_serialization(private_path, private_key)

    encr_sym_key = asymmetric.encrypt(public_key, sym_key)

    symmetric.key_serialization(symm_path, encr_sym_key)


def encryption(text_path: str, symm_key_path: str, private_key_path: str, save_path: str) -> None:
    encrypted_symm_key = file_utils.load_from_txt(symm_key_path)
    private_key =        file_utils.load_key(private_key_path)
    text =               file_utils.load_from_txt(text_path)

    symmetric_key = asymmetric.decrypt(private_key, encrypted_symm_key)

    symmetric.encrypt(text, symmetric_key, save_path)


def decrypt(text_path: str, symm_key_path: str, private_key_path: str, save_path: str) -> None:
    encrypted_symm_key = file_utils.load_from_txt(symm_key_path)
    private_key =        file_utils.load_key(private_key_path)
    text =               file_utils.load_from_txt(text_path)

    symmetric_key = asymmetric.decrypt(private_key, encrypted_symm_key)

    symmetric.decrypt(text, symmetric_key, save_path)
