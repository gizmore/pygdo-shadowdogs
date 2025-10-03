from gdo.date.Time import Time
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class Rent(SD_Quest):

    RENT = 650
    DUE = "4w"

    def reward_xp(self) -> int:
        return 10

    def render_descr(self) -> str:
        return self.t(f'sdqd_{self.__class__.__name__.lower()}', (Shadowdogs.display_nuyen(Rent.RENT), Time.display_timestamp(float(self.qv_get('due')))))

    async def on_accept(self):
        seconds = Time.human_to_seconds(self.DUE)
        due = self.get_time() + seconds
        self.qv_set('due', str(due))
