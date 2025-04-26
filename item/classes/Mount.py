from gdo.shadowdogs.item.classes.Equipment import Equipment


class Mount(Equipment):

    def get_slot(self) -> str:
        return 'p_mount'
