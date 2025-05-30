import os

import file_utils
import parcer
import CryptoSystem


def check_sets(sets) -> None:
    if not os.path.isfile(sets["initial_file"]):
        raise ValueError("Wrong path to initial file")

    if not os.path.isfile(sets["encrypted_file"]):
        raise ValueError("Wrong path to encrypted file")

    if not os.path.isfile(sets["decrypted_file"]):
        raise ValueError("Wrong path to decrypted file")

    if not os.path.isfile(sets["symmetric_key"]):
        raise ValueError("Wrong path to symmetric file")

    if not os.path.isfile(sets["public_key"]):
        raise ValueError("Wrong path to public key")

    if not os.path.isfile(sets["secret_key"]):
        raise ValueError("Wrong path to secret key")


def main() -> None:
    try:
        args = parcer.parse()
        sets = file_utils.load_from_json(args.settings)
        check_sets(sets)

        symmetric_key = file_utils.load_from_txt(sets["symmetric_key"])
        public_key =    file_utils.load_from_txt(sets["public_key"])
        private_key =   file_utils.load_from_txt(sets["private_key"])

        match args.task:
            case 'generation':
                CryptoSystem.generate_key(args.key_bits, sets["symmetric_key"], sets["public_key"], sets["private_key"])

            case 'encryption':
                text = file_utils.load_from_txt(sets["initial_file"])
                CryptoSystem.encryption(text, symmetric_key, public_key, private_key, sets["encrypted_file"])

            case 'decryption':
                text = file_utils.load_from_txt(sets["encrypted_file"])
                CryptoSystem.decryption(text, symmetric_key, public_key, private_key, sets["decrypted_file"])

            case _:
                raise ValueError("incorrect program task")

    except Exception as error:
        print("Error!\n\t", error)


if __name__ == '__main__':
    main()