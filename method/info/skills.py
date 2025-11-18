from gdo.base.Trans import t
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.skill.Skill import Skill


class skills(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return "sdskills"

    @classmethod
    def gdo_trig(cls) -> str:
        return "sdsk"

    async def sd_execute(self):
        skills = []
        player = self.get_player()
        for key in Skill.SKILLS:
            skills.append("%s: %d(%d)" % (t(key), player.gb(key), player.g(key)))
        return self.reply('msg_sd_skills', (", ".join(skills),))
