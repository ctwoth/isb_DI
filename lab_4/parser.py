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
        if args.task not in ["gui", "tests"]:
            raise ValueError("Incorrect mode")
        if not os.path.isfile(args.settings):
            raise ValueError("setting file not exist")

    @staticmethod
    def parse() -> argparse.Namespace:
        """
        parse args and validate them

        :return args from argparse:
        """
        parser = argparse.ArgumentParser(description="program work settings")

        parser.add_argument("task",            type=str,                          help="Program task: gui or (unit) tests")
        parser.add_argument("-s", "--settings",type=str, default="settings.json", help="Path to settings in JSON-file")

        args = parser.parse_args()
        Parser.validate_args(args)

        return args