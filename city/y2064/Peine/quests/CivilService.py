from gdo.base.Trans import t
from gdo.shadowdogs.SD_Quest import SD_Quest


class CivilService(SD_Quest):

    def reward(self) -> str|None:
        return '50xNuyen'

    def reward_source(self) -> str:
        return t('sdqa_from_civil_service')

    async def on_worked(self):
        times = int(self.qv_get('times', '0'))
        if times >= 11:
            return await self.send_to_player(self.get_player(), 'sdqa_thx_for_free')
        times += 1
        self.qv_set('times', str(times))
        if times < 11:
            await self.on_reward()
        else:
            await self.accomplished()
