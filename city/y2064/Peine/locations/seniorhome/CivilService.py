from gdo.base.Trans import t
from gdo.shadowdogs.SD_Quest import SD_Quest


class CivilService(SD_Quest):

    def reward(self) -> str|None:
        return '50xNuyen'

    def reward_source(self) -> str:
        return t('sdqa_from_civil_service')

    async def on_worked(self):
        times = int(self.qv_get('times', '0'))
        await self.send_to_player(self.get_player(), 'sdqs_civil_service_month')
        times += 1
        self.qv_set('times', str(times))
        await self.on_reward()
        if times >= 11:
            await self.accomplished()
            await self.give_spell(self.get_player(), 'calm', self.reward_source())
