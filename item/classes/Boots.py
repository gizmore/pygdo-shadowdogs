from gdo.shadowdogs.item.classes.Equipment import Equipment


class Boots(Equipment):
    def get_slot(self) -> str:
        return 'p_boots'
