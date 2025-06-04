import unittest
import random
import hashlib

from card_manager import CardManager


class TestCardManager(unittest.TestCase):
    def test_luhn_1(self):
        """testing 8532 sequence..."""
        self.assertEqual(CardManager.alg_luhn("8532"), True)

    def test_luhn_2(self):
        """testing 12345674 sequence..."""
        self.assertEqual(CardManager.alg_luhn("12345674"), True)

    def test_luhn_3(self):
        """testing founded card number"""
        self.assertEqual(CardManager.alg_luhn("4274232354001217"), False)


    def test_hashing_1(self):
        """testing hash of founded card"""
        self.assertEqual(CardManager.hashing_card("4274232354001217"), "e5c92fb926ffc9976ad06b46cc7eb656158f07b6e41a1666e005c9cd")

    def test_hashing_2(self):
        """testing hash of random card"""
        random_str = str(random.randint(10**15, 10**16))
        expected_hash = hashlib.sha224(random_str.encode()).hexdigest()

        self.assertEqual(CardManager.hashing_card(random_str),expected_hash)


if __name__ == '__main__':
    unittest.main()
