from gdo.shadowdogs.attr.Attribute import Attribute


class Quickness(Attribute):
    def apply(self, target: 'Player'):
        target.modify(self.get_name(), 1)
