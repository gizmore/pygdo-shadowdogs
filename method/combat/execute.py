from gdo.base.GDT import GDT
from gdo.core.GDT_RestOfText import GDT_RestOfText
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.GDT_Executable import GDT_Executable
from gdo.shadowdogs.item.classes.hack.Executable import Executable


class execute(MethodSD):

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdx'

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdexe'

    def sd_requires_action(self) -> list[str] | None:
        return [
            'hack',
        ]

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_Executable('exe'),
            GDT_RestOfText('args'),
        ]

    def get_exe(self) -> Executable:
        return self.param_value('exe')

    async def sd_execute(self):
        p = self.get_player()
        await self.get_exe().sd_run(self.param_value('args'))
