from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class MethodSDObstacle(MethodSD):

    def sd_with_location(self) -> bool:
        return True

    async def sd_execute(self):
        trigger = self.gdo_sd_trigger()
        obstacles = self.get_obstacles(trigger)
        if len(obstacles) == 1:
            await self.execute_obstacle(obstacles[0])
        return self.empty()

    def get_obstacles(self, for_trigger: str = None) -> list[Obstacle]:
        obstacles = []
        if loc := self.get_location():
            if hasattr(loc, f'on_{for_trigger}') and self.sd_with_location():
                obstacles.append(loc)
            for obs in loc.obstacles(self.get_action_name(), self.get_player()):
                if hasattr(obs, f'on_{for_trigger}'):
                    obstacles.append(obs)
        return obstacles

    def gdo_sd_trigger(self):
        return self.gdo_trigger()[2:]

    async def execute_obstacle(self, obstacle: Obstacle):
        trigger = self.gdo_sd_trigger()
        await getattr(obstacle.player(self.get_player()), f'on_{trigger}')(self.parameters())
