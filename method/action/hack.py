from gdo.shadowdogs.engine.MethodSDObstacle import MethodSDObstacle


class hack(MethodSDObstacle):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdhack'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdh'

    def sd_requires_item_klass(self) -> list[str]:
        return [
            'Deck',
        ]
