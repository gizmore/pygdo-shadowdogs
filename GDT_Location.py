from gdo.core.GDT_String import GDT_String


class GDT_Location(GDT_String):
    
    def __init__(self, name: str):
        super().__init__(name)
        