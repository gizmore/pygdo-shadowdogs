from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class MethodSDObstacle(MethodSD):

    async def sd_execute(self):
        trigger = self.gdo_sd_trigger()
        obstacles = self.get_obstacles(trigger)
        if len(obstacles) == 1:
            await self.execute_obstacle(obstacles[0])
        return self.empty()

    def get_obstacles(self, for_trigger: str = None) -> list[Obstacle]:
        if loc := self.get_location():
            pass


        return self.EMPTY_LIST

    def gdo_sd_trigger(self):
        return self.gdo_trigger()[2:]

    async def execute_obstacle(self, obstacle: Obstacle):
        trigger = self.gdo_sd_trigger()
        await getattr(obstacle.player(self.get_player()), f'on_{trigger}')()
