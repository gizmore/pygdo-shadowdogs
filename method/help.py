from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDT_String import GDT_String


class help(Method):

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

    def gdo_trigger(self) -> str:
        return 'sdhelp'

    def gdo_parameters(self) -> [GDT]:
        return [
            GDT_String('key').not_null().initial('shadowdogs').positional(),
        ]

    def gdo_execute(self) -> GDT:
        pass
