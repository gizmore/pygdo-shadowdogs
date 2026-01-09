from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.locations.Location import Location
from gdo.ui.GDT_Success import GDT_Success


class Hospital(Location):

    SD_HEAL_PRICE = 100

    def sd_cyberware(self, player: SD_Player) -> list[tuple[str, int]]:
        return []

    def sd_methods(self) -> list[str]:
        return [
            'sdheal',
            'sdimplant',
            'sdview',
            'sdviewitem',
        ]

    def on_heal(self, player: SD_Player):
        player.give_hp(65535)
        return GDT_Success().text('msg_sd_healed')