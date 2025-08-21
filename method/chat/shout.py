from gdo.core.GDT_RestOfText import GDT_RestOfText
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.engine.MethodSD import MethodSD


class shout(MethodSD):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_RestOfText('message').not_null(),
        )

    def sd_execute(self):
        pass
