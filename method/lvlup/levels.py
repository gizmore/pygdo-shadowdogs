from gdo.base.Util import Arrays
from gdo.shadowdogs.engine.MethodSD import MethodSD


class levels(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdlevel'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdlev'

    def sd_execute(self):
        party = self.get_party()
        lvls = [f"L{p.gb('p_level')}({p.g('p_level')}){p.render_name()}" for p in party.members]
        return self.reply('msg_sd_levels', (Arrays.human_join(lvls),))
