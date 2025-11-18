from gdo.shadowdogs.engine.MethodSD import MethodSD


class courses(MethodSD):

    def sd_is_location_specific(self) -> bool:
        return True

    async def sd_execute(self):
        return self.get_location().on_courses(self.get_player())
