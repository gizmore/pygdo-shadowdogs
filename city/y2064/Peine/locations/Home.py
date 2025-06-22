from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.shadowdogs.obstacle.Searchable import Searchable


class Home(Location):

    OBSTACLES: dict[str,list[Obstacle]] = {
        Action.INSIDE: [
            Searchable('Fridge').obstacle_id('home.fridge').giving(['Coke']),
        ]
    }
