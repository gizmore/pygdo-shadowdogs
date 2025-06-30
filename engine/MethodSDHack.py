from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSDObstacle import MethodSDObstacle
from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.shadowdogs.obstacle.minigame.Computer import Computer


class MethodSDHack(MethodSDObstacle):

    def sd_requires_action(self) -> list[str] | None:
        return [
            Action.HACK,
        ]

    def get_computer(self) -> Computer:
        return self.get_party().get_target()

