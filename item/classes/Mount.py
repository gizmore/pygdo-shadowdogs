from gdo.shadowdogs.item.classes.Equipment import Equipment


class Mount(Equipment):

    def get_slot(self) -> str:
        return 'p_mount'

    def get_seats(self) -> int:
        return self.dmi('seats')

    def get_speed(self) -> int:
        return self.dmi('speed')

    def get_storage(self) -> int:
        return self.dmi('storage')

    def get_overload(self) -> int:
        return self.dmi('overload')

    def get_weight(self) -> int:
        weight = 0
        for item in self.get_owner().mount:
            weight += item.get_weight()
        return weight

    def can_move(self) -> bool:
        return self.get_real_speed() > 0

    def get_real_speed(self) -> int:
        speed = self.get_speed()
        storage = self.get_storage()
        weight = self.get_weight()
        overload = self.get_overload()
        while weight > storage and speed > 0:
            weight -= overload
            speed -= 1
        return speed
