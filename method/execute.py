from gdo.base.GDT import GDT
from gdo.shadowdogs.engine.MethodSD import MethodSD


class execute(MethodSD):

    def gdo_trig(cls) -> str:
        return 'sdx'

    def gdo_trigger(cls) -> str:
        return 'sdexe'

    def sd_requires_action(self) -> list[str] | None:
        return [
            'hack',
        ]

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_Executeable('exe'),
        ]

    def sd_execute(self):
        self.get_player().