from gdo.shadowdogs.engine.MethodSD import MethodSD


class xls(MethodSD):

    def sd_requires_item_klass(self) -> list[str]:
        return [
            'Deck',
        ]

    async
