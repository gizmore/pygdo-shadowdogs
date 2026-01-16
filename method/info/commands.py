from gdo.shadowdogs.engine.MethodSD import MethodSD


class commands(MethodSD):

    async def sd_execute(self):
        return self.msg('msg_sd_commands', ())
