from src.main.buildings.util_classes.Cost import Cost
from src.main.gui.util_classes.Point import Point
from src.main.map.map import Map
from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.resources.Resources import Resources


class Engine:
    """
    Class that stands in the middle between gui and backend. It **only** transfers command from gui to
    map and vice versa. It does not hold any data about gui (like which building is chosen, what tile is hovered etc.).
    The only thing it does is **checking validity** of commands to be made.
    """

    def __init__(self, map_size: int):
        self.map = Map(map_size)
        self.resources = Resources()

    def possible_to_place(self, lower_left: Point, building: AbstractBuilding):
        """
        Given signal from gui, checks whether it's possible to place a building.

        :param lower_left: Point - bottom left corner of building
        :param building: AbstractBuilding - building to be placed
        :return: bool
        """

        return self.map.possible_to_place(lower_left, building) and self.resources.has_enough_resources(building)

    def place_building(self, lower_left: Point, building: AbstractBuilding, mode: str):
        self.map.place_building(lower_left, building)
        if mode != "MOVE":
            self.resources.on_building(building)

    def find_building_at_field(self, x: float, y: float):
        x, y = int(x), int(y)
        return self.map.find_building_at_field(x, y)

    def remove_building(self, building: AbstractBuilding, mode: str):
        self.map.remove_building(building)
        if mode != "MOVE":
            self.resources.on_destroy(building)

    def connected_to_town_hall(self, lower_left: Point, building: AbstractBuilding):
        return self.map.connected_to_town_hall(lower_left, building)

    def get_map_dimensions(self):
        """
        Returns **(int, int)** instead of Point object because of representing something logically different
        (dimensions of the map are final and there's no need in comparing them to other Points).

        :return: (int length, int width)
        """

        return self.map.length, self.map.width

    def is_tile_free(self, i: int, j: int):
        """
        Checks whether given tile of map is free.
        :param i: int
        :param j: int
        :return: bool
        """

        return self.map.free[i][j]

    def get_resources(self):
        return Cost(self.resources.money, self.resources.supply, self.resources.people)
