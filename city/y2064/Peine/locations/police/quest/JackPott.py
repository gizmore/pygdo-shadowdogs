from gdo.base.Application import Application
from gdo.date.Time import Time
from gdo.shadowdogs.SD_Quest import SD_Quest


class JackPott(SD_Quest):

    TIMEOUT = Time.ONE_HOUR

    def reward_xp(self) -> int:
        return 20

    def get_timeout(self) -> int:
        return int(self.qv_get('timeout'))

    async def on_accept(self):
        self.qv_set('timeout', str(int(Application.TIME)))

    def render_descr(self) -> str:
        return self.t(f'sdqd_{self.__class__.__name__.lower()}', (Time.human_duration(int(Application.TIME) + self.TIMEOUT - self.get_timeout()),))
