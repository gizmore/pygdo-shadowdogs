from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.city.y2064.Peine.locations.seniorhome.CivilService import CivilService
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Nurse(TalkingNPC):

    def sd_quest(self) -> type[SD_Quest]|None:
        return CivilService

    async def on_say(self, player: SD_Player, text: str):
        q = self.q()
        if text == 'work':
            self.qv_set('informed', '1')
            await self.say('sdqs_civil_service_good')
        elif text == 'yes':
            if self.qv_get('informed'):
                await self.say('sdqs_civil_service_accepted')
                await q.accept()
            else:
                await self.say('sdqs_civil_service_what')
        elif text == 'no':
            await self.say('sdqs_civil_service_no')
        else:
            await self.say('sdqs_civil_service_hello')
        await self.give_word(player, 'hello')
