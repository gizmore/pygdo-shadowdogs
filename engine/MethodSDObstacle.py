from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class MethodSDObstacle(MethodSD):

    async def form_submitted(self):
        if self.sd_method_is_instant():
            return self.sd_execute()
        player = self.get_player()
        if player.get_party().does(Action.FIGHT):
            player.combat_stack.command = self
            return self.empty()
        if player.is_busy():
            await self.send_to_player(player, 'err_sd_player_busy', (player.render_busy(),))
        await self.sd_before_execute()
        return await self.sd_execute()

    async def sd_before_execute(self):
        pass

    async def sd_execute(self):
        trigger = self.gdo_sd_trigger()
        obstacles = self.get_obstacles(trigger)
        if len(obstacles) == 1:
            await self.execute_obstacle(obstacles[0])
        return self.empty()

    def get_obstacles(self, for_trigger: str = None) -> list[Obstacle]:
        if loc := self.get_location():


        return self.EMPTY_LIST

    def gdo_sd_trigger(self):
        return self.gdo_trigger()[2:]

    async def execute_obstacle(self, obstacle: Obstacle):
        trigger = self.gdo_sd_trigger()
        await getattr(obstacle.player(self.get_player()), f'on_{trigger}')()
