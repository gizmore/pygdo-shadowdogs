from gdo.shadowdogs.obstacle.minigame.tile.Tile import Tile

class Vault(Tile):

    _password: str
    _password_difficulty: int

    _item_name: str
    _nuyen: int

    def __init__(self):
        super().__init__()

    def password(self, password: str, difficulty: int = 10):
        self._password = password
        self._password_difficulty = difficulty
        return self

    def giving(self, item_name: str):
        self._item_name = item_name
        return self

    def paying(self, nuyen: int):
        self._nuyen = nuyen
        return self
