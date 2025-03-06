from gdo.shadowdogs.itembase.Item import Item


class Weapon(Item):
    def get_actions(self) -> list[str]:
        return ['attack']
