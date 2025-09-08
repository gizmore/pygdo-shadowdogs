from gdo.base.GDT import GDT
from gdo.shadowdogs.GDT_Quest import GDT_Quest
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.engine.MethodSD import MethodSD


class quest(MethodSD):

     @classmethod
     def gdo_trigger(cls) -> str:
         return "sdquest"

     @classmethod
     def gdo_trig(cls) -> str:
         return "sdqu"

     def gdo_parameters(self) -> list[GDT]:
         return [
             GDT_Quest('quest').positional(),
         ]

     def get_quest(self) -> SD_Quest:
         return self.param_value('quest')

     async def sd_execute(self):
         if not (quest := self.get_quest()):
             return self.execute_command('sdquests')
         return self.reply('msg_sd_quest', (quest.render_name(), quest.render_descr()))
