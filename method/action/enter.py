from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD


class enter(MethodSD):
    def sd_requires_action(self) -> list[str] | None:
        return [
            Action.OUTSIDE,
        ]

    def sd_is_location_specific(self) -> bool:
        return True

    def sd_combat_seconds(self) -> int:
        return 10

    def sd_execute(self):
        self.get_party().do(Action.INSIDE)
        self.get_location()
