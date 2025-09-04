from gdo.core.GDT_RestOfText import GDT_RestOfText
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.engine.MethodSD import MethodSD


class partymessage(MethodSD):
    """
    Send a message to all own party members.
    """

    @classmethod
    def gdo_trigger(cls) -> str:
        return "sdpartymessage"

    @classmethod
    def gdo_trig(cls) -> str:
        return "sdpm"

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_RestOfText('message').not_null(),
        )
        super().gdo_create_form(form)

    async def sd_execute(self):
        await self.send_to_party(self.get_party(), 'msg_sd_party_message', (self.get_player().render_name(), self.param_value('message')))
        return self.empty()
