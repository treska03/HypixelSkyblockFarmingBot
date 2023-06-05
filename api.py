import requests
import json
from packages.utils import json_unpack

class PlayerApi:

    def __init__(self):
        self.api_key = None
        self.nickname = None
        self.uuid = None
        self._get_credentials()
        self._set_player_uuid()

    def _get_credentials(self):
        try:
            f = json_unpack("config.json")
            self.nickname = f["PLAYER"]["nickname"]
            self.api_key = f["PLAYER"]["api_key"]
            print(f"User: {self.nickname}\nHypixel API key: {self.api_key}")
        except KeyError:
            raise KeyError("config.json file wrongly configured.")

    def _set_player_uuid(self):
        mojang_uri = f'https://api.mojang.com/users/profiles/minecraft/{self.nickname}'
        response = requests.get(mojang_uri)
        content = json.loads(response.content)
        self.uuid = content["id"]

    def check_garden(self, counter):
        hypixel_uri = f'https://api.hypixel.net/status?key={self.api_key}&uuid={self.uuid}'

        response = requests.get(url=hypixel_uri)
        if response.ok:
            content = json.loads(response.content)
            session = content["session"]
            if session["online"] and session["mode"] == "garden":
                return 0
        return counter + 1

class Ghost:
    """
    Empty class indicating that user doesn't want API features.
    Prevents grabbing data from config.json. 
    """