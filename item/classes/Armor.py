from gdo.shadowdogs.item.classes.Equipment import Equipment


class Armor(Equipment):

    def get_slot(self) -> str:
        return 'p_armor'
