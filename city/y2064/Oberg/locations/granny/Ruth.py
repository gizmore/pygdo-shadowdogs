from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.city.y2064.Oberg.locations.granny.Lecture import Lecture
from gdo.shadowdogs.city.y2064.Peine.locations.obi.ParkingPlace import ParkingPlace
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Ruth(TalkingNPC):

    async def on_say(self, player: SD_Player, text: str):
        if text == 'hello':
            await self.say('sdqs_ruth_hello')
        elif text == 'work':
            if ParkingPlace.instance().is_in_quest():
                await self.say('sdqs_ruth_work2')
            elif Lecture.instance().is_in_quest():
                await self.say('sdqs_ruth_work4')
            elif ParkingPlace.instance().is_done():
                await self.say('sdqs_ruth_work3')
            else:
                await self.say('sdqs_ruth_work1')
        elif text == 'weed':
            await self.say('sdqs_ruth_weed')
        elif text == 'home':
            await self.say('sdqs_ruth_home')
