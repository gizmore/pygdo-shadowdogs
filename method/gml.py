from gdo.core.GDO_Permission import GDO_Permission
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Location import GDT_Location
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD


class gml(MethodSD):

    def gdo_user_permission(self) -> str | None:
        return GDO_Permission.ADMIN

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_Player('player').humans().online().not_null(),
            GDT_Location('location').not_null(),
        )
        super().gdo_create_form(form)

    def form_submitted(self):
        new = msg.message_copy().env_user(chappy, True).message(line).result(None)
        Application.MESSAGES.put(new)
