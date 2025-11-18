from gdo.base.Application import Application
from gdo.base.Util import Random
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Peine.locations.gunzelin.BaM import BaM
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Miehe(TalkingNPC):

    MIN_LEVEL = 1

    def sd_quest(self) -> type[SD_Quest]|None:
        return BaM

    async def on_say(self, player: SD_Player, text: str):

        if player.gb('p_mat') < self.MIN_LEVEL or not self.qv_get('init'):
            await self.say('sdqs_miehe_nono')
            await self.give_word(player, 'learn')
            await self.q().accept()
        elif text == "hello":
            await self.say('sdqs_miehe_hello')
        elif text == "learn":
            self.qv_set('task1', str(Random.mrand(1, 5)))
            self.qv_set('task2', str(Random.mrand(0, 3)))
            self.qv_set('t', str(Application.TIME))
            await self.say('sdqs_miehe_learn', (self.qv_get('task1'), self.qv_get('task2')))
        elif text in ('yes', 'no', 'work', 'home'):
            await self.say('sdqs_miehe_no_idea')
        elif self.qv_get('task1'):
            task1 = int(self.qv_get('task1'))
            task2 = int(self.qv_get('task2'))
            solution = str(2 ** task2)
            solution += ['k', 'm', 'g', 't', 'p'][task1-2]
            time = float(self.qv_get('t'))
            taken = Application.TIME - time
            if text == solution:
                if taken > BaM.TIME_SKILL_REQUIRED:
                    await self.say('sdqs_miehe_too_slow')
                else:
                    await self.say('sdqs_miehe_correct')
                    await self.q().accomplished()
                    player.incb('p_mat', 1)
            else:
                await self.say('sdqs_miehe_wrong_answer')
        else:
            await self.say('sdqs_miehe_else', (player.render_name_short(),))
        self.qv_set('init', '1')
