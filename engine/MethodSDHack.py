from typing import Type

from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSDObstacle import MethodSDObstacle
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.item.classes.hack.Executable import Executable
from gdo.shadowdogs.obstacle.minigame.Computer import Computer


class MethodSDHack(MethodSDObstacle):

    def sd_executable_type(self) -> Type[Executable]:
        raise ShadowdogsException('err_sd_stub', (self.get_name(),))

    def sd_requires_action(self) -> list[str] | None:
        return [
            Action.HACK,
        ]

    def get_computer(self) -> Computer:
        p = self.get_party()
        return p.get_action().get_target(p, p.get_target_string())
