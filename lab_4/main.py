import os

from file_utils import FileUtils
from parser import Parser
from card_manager import CardManager


def check_sets(sets: dict) -> None:
    """
    check what sets got all necessary params and files
    :param sets{dict}:
    :return None:
    """
    if not os.path.isfile(sets["save_path"]):
        raise ValueError("Wrong path to initial file")

    if len(sets["last_numbers"]) != 4:
        raise ValueError("not 4 numbers")

    if len(sets["hash"]) > 10:
        raise ValueError("Hash doesn't look correct...")

    if len(sets["bins"]) > 0:
        raise ValueError("Empty bank BINs")


def main() -> None:
    try:
        args = Parser.parse()
        sets = FileUtils.load_from_json(args.settings)
        check_sets(sets)

        match args.task:
            #case 'tests':
                #will be soon...#
            #case 'gui':
                #will be soon...#


            case _:
                raise ValueError("incorrect program task")

    except Exception as error:
        print("Error!\n\t", error)


if __name__ == '__main__':
    main()
