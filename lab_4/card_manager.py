import multiprocessing as mp
import hashlib


class CardManager:
    @staticmethod
    def hashing_card(num: str) -> str:
        return hashlib.sha224(num.encode()).hexdigest()

    @staticmethod
    def find_card_from_hash(bins: list[str], last_nums: str, target_hash: str, free_cores: int = mp.cpu_count()) -> str:
        num_range = 10**(16 - 6 - len(last_nums))
        core_range = num_range // free_cores

        with mp.Pool(processes=free_cores) as p:
            results = []
            start = 0

            for card_bin in bins:
                for iteration in range(free_cores):
                    start += core_range
                    end = start + core_range if iteration != free_cores - 1 else num_range

                    results.append(p.apply_async(
                        CardManager.hash_search,
                        (card_bin, last_nums, start, end, target_hash)
                        )
                    )

            for result in results:
                if result:
                    return result

        return None

    @staticmethod
    def hash_search(card_bin: str, last_nums: str, start: int, end: int, target_hash: str) -> str:
        for middle_nums in range(start, end):
            card = card_bin + f"{middle_nums}" + last_nums

            rand_hash = CardManager.hashing_card(card)

            if rand_hash == target_hash:
                return card

        return None
