from gdo.base.GDT import GDT
from gdo.core.GDT_RestOfText import GDT_RestOfText
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD


class whisper(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdwhisper'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdw'

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_Player('target').online().not_null(),
            GDT_RestOfText('text').not_null(),
        ]

    def get_target(self) -> SD_Player:
        return self.param_value('target')

    def get_text(self) -> str:
        return self.param_value('text')

    async def sd_execute(self):
        await self.get_target().on_say(self.get_player(), self.get_text())
        await self.send_to_player(self.get_target(), 'msg_sd_whisper', (self.get_player().get_name(), self.get_text()))
        return self.empty()
