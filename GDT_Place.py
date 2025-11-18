from gdo.core.GDT_Select import GDT_Select


class GDT_Place(GDT_Select):

    def __init__(self, name: str):
        super().__init__(name)

    def gdo_choices(self) -> dict:
        return {

        }