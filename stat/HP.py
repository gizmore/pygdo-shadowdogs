from gdo.shadowdogs.engine.Modifier import Modifier


class HP(Modifier):

    def apply(self, target: 'Player'):
        if target.gdo_val('p_hp') <= 0:
            target.die()
