from gdo.shadowdogs.item.classes.Equipment import Equipment


class Amulet(Equipment):
    def get_slot(self) -> str:
        return 'p_amulet'
