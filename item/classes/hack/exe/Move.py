from gdo.shadowdogs.item.classes.hack.Executable import Executable


class Move(Executable):

    def sd_commands(self) -> list[str]:
        return [
            'sdmove',
        ]

    def sd_run(self, args: str = None):
        pass
