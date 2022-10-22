import requests

from util.ConfigReader import ConfigReader


class VSCOClient:
    def __init__(self):
        self.__VSCO_BASE_URL = ConfigReader.get("vsco-client", "BASE_URL")

    def username_is_taken(self, username: str) -> bool:
        url = f"{self.__VSCO_BASE_URL}{username}"

        response = requests.get(url)

        if response.status_code == 200:
            return True
        elif response.status_code == 404:
            return False
        else:
            response.raise_for_status()
            return False
