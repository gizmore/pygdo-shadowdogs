from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDT_String import GDT_String
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.engine.MethodSD import MethodSD


class help(MethodSD):

    HELP = {
        'shadowdogs': {
            'attributes': {
                'body': 'increases HP.',
            },
            'skills': {
                'fight': 'Increases attack',
            },
            'stats': {
                'HP': 'Your health. When it reaches zero you become death.',
            },
            'various': {

            },
        },
    }

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdhelp'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(GDT_String('key').not_null().initial('shadowdogs').positional())
        super().gdo_create_form(form)

    def gdo_execute(self) -> GDT:
        pass
