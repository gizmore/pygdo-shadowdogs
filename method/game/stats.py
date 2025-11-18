from gdo.shadowdogs.engine.MethodSD import MethodSD


class stats(MethodSD):

    def sd_requires_player(self) -> bool:
        return False

    async def sd_execute(self):
        pass
