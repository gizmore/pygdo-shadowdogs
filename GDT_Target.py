from gdo.core.GDT_String import GDT_String


class GDT_Target(GDT_String):

    def __init__(self, name: str):
        super().__init__(name)
        self.ascii()
        self.case_s()

    
