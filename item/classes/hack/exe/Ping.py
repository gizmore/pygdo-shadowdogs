from gdo.shadowdogs.item.classes.hack.Executable import Executable


class Ping(Executable):

    def sd_commands(self) -> list[str]:
        return [
            'sdping',
        ]

    def on_ping(self, direction: str) -> None:
        computer = self.get_computer()
        map = self.get_computer_map()
        tile = map.get_tile_for(direction)

        self.get_computer().on_ping(direction)
