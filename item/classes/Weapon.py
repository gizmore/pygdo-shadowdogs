from gdo.shadowdogs.item.Item import Item


class Weapon(Item):

    def get_slot(self) -> str:
        return 'p_armor'

    def get_actions(self) -> list[str]:
        return ['attack']
