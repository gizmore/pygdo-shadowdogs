from gdo.base.Application import Application
from gdo.base.Util import Arrays
from gdo.shadowdogs.SD_Quest import SD_Quest

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class KillQuest(SD_Quest):

    KILLS: dict[str, int] = None

    def sd_init_quest(self):
        for mob, count in self.KILLS.items():
            Application.EVENTS.subscribe(f'sd_kill_{mob}', self.on_sd_kill)

    def on_sd_kill(self, killer: 'SD_Player', victim: 'SD_Player'):
        for mob, need in self.KILLS.items():
            if victim.gdo_val('p_npc_name') == mob:
                have = int(self.qv_get(f'killed_{mob}', '0', killer))
                have += 1
                self.qv_set(f'killed_{mob}', str(have), killer)

    def check_accomplished(self) -> bool:
        result = True
        for mob, need in self.KILLS.items():
            have = int(self.qv_get(f'killed_{mob}', '0'))
            if have < need:
                result = False
        return result

    def render_descr(self) -> str:
        out = []
        for mob, need in self.KILLS.items():
            have = int(self.qv_get(f'killed_{mob}', '0'))
            out.append(f"{have}/{need} {mob}s")
        return self.t(f'sdqd_{self.__class__.__name__.lower()}', (Arrays.human_join(out),))
