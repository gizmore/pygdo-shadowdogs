from gdo.core.GDT_Bool import GDT_Bool
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_SkillAttribute import GDT_SkillAttribute
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class lvlup(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdlvlup'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdl'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_Bool('simulate').not_null().initial('0'),
            GDT_SkillAttribute('field').skills().attributes().not_null(),
        )
        super().gdo_create_form(form)

    def get_skill(self):
        skill = self.param_val('field')
        if self.parameter('field').is_skill(skill):
            return skill

    def get_attribute(self):
        attr = self.param_val('field')
        if self.parameter('field').is_attribute(attr):
            return attr

    async def sd_execute(self):
        player = self.get_player()
        field = self.param_val('field')
        mul = Shadowdogs.KARMA_PER_ATTRIBUTE
        if skill := self.get_skill():
            mul = Shadowdogs.KARMA_PER_SKILL
        old_lvl = player.gb(field)
        new_lvl = old_lvl + 1
        need_karma = (old_lvl + 1) * mul
        have_karma = player.gb('p_karma')
        if have_karma < need_karma:
            return self.err('err_sd_lvlup_karma', (self.t(field), old_lvl, new_lvl, need_karma, have_karma))
        player.increment(field, 1)
        player.increment('p_karma', -1)
        return self.reply('msg_sd_lvlup', (need_karma, self.t(field), old_lvl, new_lvl))
