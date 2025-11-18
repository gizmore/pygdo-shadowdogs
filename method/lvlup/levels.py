from gdo.base.Util import Arrays
from gdo.shadowdogs.engine.MethodSD import MethodSD


class levels(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdlevel'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdlev'

    async def sd_execute(self):
        party = self.get_party()
        lvls = [f"{p.render_name()}:L{p.gb('p_level')}({p.g('p_level')})" for p in party.members]
        return self.msg('msg_sd_levels', (Arrays.human_join(lvls),))
