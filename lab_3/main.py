import os

from file_utils import FileUtils
from parser import Parser
from cryptoSystem import CryptoSystem


def check_sets(sets: dict) -> None:
    """
    check what sets got all necessary files
    :param sets{dict}:
    :return:
    """
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
        args = Parser.parse()
        sets = FileUtils.load_from_json(args.settings)
        check_sets(sets)

        match args.task:
            case 'generation':
                CryptoSystem.generate_keys(args.key_bits, sets["symmetric_key"],
                                          sets["public_key"], sets["secret_key"])

            case 'encryption':
                CryptoSystem.encryption(sets["initial_file"], sets["symmetric_key"],
                                        sets["secret_key"], sets["encrypted_file"])

            case 'decryption':
                CryptoSystem.decryption(sets["encrypted_file"], sets["symmetric_key"],
                                        sets["secret_key"], sets["decrypted_file"])

            case _:
                raise ValueError("incorrect program task")

    except Exception as error:
        print("Error!\n\t", error)


if __name__ == '__main__':
    main()
