from src.main.gui.util_classes.Point import Point
from src.main.map.map import Map
from src.main.buildings.AbstractBuilding import AbstractBuilding


class Engine:
    """
    Class that stands in the middle between gui and backend. It **only** transfers command from gui to
    map and vice versa. It does not hold any data about gui (like which building is chosen, what tile is hovered etc.).
    The only thing it does is **checking validity** of commands to be made.
    """

    def __init__(self, map_size: int):
        self.map = Map(map_size)

    def place_building_on_map(self, lower_left: Point, building: AbstractBuilding):
        """
        Given signal from gui, checks whether it's possible to place a building and then places it.

        :param lower_left: Point - bottom left corner of building
        :param building: AbstractBuilding - building to be placed
        :return: bool
        """

        if self.map.possible_to_place(lower_left, building):
            self.map.place_building(lower_left, building)
            return True
        return False

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
