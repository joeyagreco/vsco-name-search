import itertools
import random
import string
from functools import lru_cache

from client.VSCOClient import VSCOClient
from util.CustomLogger import CustomLogger


class VSCOService:
    def __init__(self):
        self.__LOGGER = CustomLogger.get_logger()
        self.__vsco_client = VSCOClient()

    def save_unused_usernames(self, min_length: int = 3, max_length: int = 38,
                              max_usernames_to_save: int = 1_000_000) -> None:
        """
        Saves unused VSCO usernames to a file.
        """

        unused_usernames: list[str] = list()

        for i in range(min_length, max_length + 1):
            all_words_length_n = self.get_all_n_length_words(i)
            random.shuffle(all_words_length_n)

            for word in all_words_length_n:
                username_is_taken = self.__vsco_client.username_is_taken(word)
                if username_is_taken:
                    self.__LOGGER.error(f"USERNAME '{word}' IS TAKEN")
                else:
                    self.__LOGGER.critical(f"USERNAME '{word}' IS NOT TAKEN")

    @lru_cache(maxsize=None)
    def get_all_n_length_words(self, n: int) -> list[str]:
        return ["".join(i) for i in itertools.product(string.ascii_lowercase, repeat=n)]
