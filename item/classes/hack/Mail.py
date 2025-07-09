from gdo.shadowdogs.item.classes.Usable import Usable


class Mail(Usable):

    _mailtext_key: str
    _mailtext_args: tuple[any,...]

    def text(self, key: str, args: tuple[any,...]):
        self._mailtext_key = key
        self._mailtext_args = args
        return self

    def sd_commands(self) -> list[str]:
        return [
            'sdread',
        ]

    async def on_use(self):
        await self.send_to_player(self.get_player(), self._mailtext_key, self._mailtext_args)
