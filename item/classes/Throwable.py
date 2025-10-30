from gdo.shadowdogs.item.Item import Item


class Throwable(Item):

    def sd_methods(self,player: 'SD_Player') -> list[str]:
        return [
            "sdthrow",
        ]