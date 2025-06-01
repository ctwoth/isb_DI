import argparse
import os


def validate_args(args: argparse.Namespace) -> None:
    if args.mode not in ["generation", "encryption", "decryption"]:
        raise ValueError("Incorrect mode")
    if args.key_bits in [64, 128, 192]:
        raise ValueError("Incorrect key_bits")

def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="program work settings")

    parser.add_argument("task",            type=str, help="Program task: generation / encryption / decryption")
    parser.add_argument("-s", "--settings",type=str, default="settings.json", help="Path to settings in JSON-file")
    parser.add_argument("-kb","--key_bits",type=int, default=192, help="3DES symmetric key length (64, 128 or 192)")
    parser.add_argument("-uk","--user_key",type=str, edefault="", help="Path to the symmetric key file")

    args = parser.parse_args()

    return args
