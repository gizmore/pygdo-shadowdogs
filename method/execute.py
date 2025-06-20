from gdo.base.GDT import GDT
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.GDT_Executable import GDT_Executable
from gdo.shadowdogs.obstacle.minigame.Executable import Executable


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
            GDT_Executable('exe'),
        ]

    def get_exe(self) -> Executable:
        pass

    def sd_execute(self):
        p = self.get_player()