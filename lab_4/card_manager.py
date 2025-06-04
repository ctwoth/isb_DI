import multiprocessing as mp
import hashlib

class CardManager:
    @staticmethod
    def alg_luhn(num_str: str) -> bool:
        """
        using Luhn test to prove what card_num correct

        :param num_str:
        :return correct num or not:
        """
        total = 0

        for i, digit in enumerate(reversed (num_str)):
            num = int(digit)
            if i % 2 == 1:
                num *= 2
                if num > 9:
                    num = (num // 10) + (num % 10)

            total += num

        return total % 10 == 0

    @staticmethod
    def hashing_card(num: str) -> str:
        """
        getting hash of num using sha224 algorythm

        :param num:
        :return sha224_hash:
        """
        return hashlib.sha224(num.encode()).hexdigest()

    @staticmethod
    def find_card_from_hash(bins: list[str], last_nums: str, target_hash: str, free_cores: int = mp.cpu_count()) -> str:
        """
        using BINs, and last numbers trying to find card number knowing its hash with direct iteration on multiple processes.

        :param bins:
        :param last_nums:
        :param target_hash:
        :param free_cores:
        :return rinded_card:
        """
        num_range = 10**(16 - 6 - len(last_nums))
        core_range = num_range // free_cores

        with mp.Pool(processes=free_cores) as p:
            results = []

            for card_bin in bins:
                for iteration in range(free_cores):
                    start = core_range * iteration
                    end = core_range * (iteration + 1) if iteration != free_cores - 1 else num_range

                    results.append(p.apply_async(
                        CardManager.hash_search,
                        (card_bin, last_nums, start, end, target_hash)
                        )
                    )

            for i in range(len(results)):
                r = results[i].get()
                if r:
                    p.terminate()
                    return r

        return None

    @staticmethod
    def hash_search(card_bin: str, last_nums: str, start: int, end: int, target_hash: str) -> str:
        """
        direct iteration of card_nums in range from {start} to {end} numbers
        
        :param card_bin: 
        :param last_nums: 
        :param start: 
        :param end: 
        :param target_hash: 
        :return founded_num:
        """
        for middle_nums in range(start, end):
            card = f"{card_bin}{middle_nums}{last_nums}"

            rand_hash = CardManager.hashing_card(card)

            if rand_hash == target_hash:
                return card

        return None
