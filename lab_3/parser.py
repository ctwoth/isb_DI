import argparse
import os


class Parser:
    @staticmethod
    def validate_args(args: argparse.Namespace) -> None:
        """
        check what args correct, if not -> raise a error
        
        :param args from argparse:
        :return None:
        """
        if args.task not in ["generation", "encryption", "decryption"]:
            raise ValueError("Incorrect mode")
        if args.key_bits not in [64, 128, 192]:
            raise ValueError("Incorrect key_bits")
        if not os.path.isfile(args.settings):
            raise ValueError("setting file not exist")

    @staticmethod
    def parse() -> argparse.Namespace:
        """
        parse args and validate them
        
        :return args from argparse: 
        """
        parser = argparse.ArgumentParser(description="program work settings")

        parser.add_argument("task",            type=str,                          help="Program task: generation / encryption / decryption")
        parser.add_argument("-s", "--settings",type=str, default="settings.json", help="Path to settings in JSON-file")
        parser.add_argument("-kb","--key_bits",type=int, default=192,             help="3DES symmetric key length (64, 128 or 192)")

        args = parser.parse_args()
        Parser.validate_args(args)

        return args
