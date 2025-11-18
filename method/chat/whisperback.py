from gdo.shadowdogs.engine.MethodSD import MethodSD


class whisperback(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdwhisperback'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdwb'

    async def sd_execute(self):
        pass
