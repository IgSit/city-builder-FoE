from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.gui.util_classes.Point import Point


class Map:

    def __init__(self, n: int):
        """
        Back-end map holding info which field is free (self.free 2d array) and holding list of buildings that are
        already placed on map (self.buildings).

        :param n: int - length of map (it is a square)
        """
        self.free: [[bool]] = [[True for _ in range(n)] for _ in range(n)]
        self.buildings: [AbstractBuilding] = []
        self.length: int = n
        self.width: int = n

    def possible_to_place(self, lower_right: Point, building: AbstractBuilding) -> bool:
        """
        Checks whether given building can be placed on map.

        :param lower_right: Point - bottom right corner of building desired position,
        :param building: AbstractBuilding - building to be placed.
        :return: bool
        """
        if int(lower_right.x) + building.dimensions.width - 1 > self.width - 1:
            return False
        if int(lower_right.y) + building.dimensions.length - 1 > self.length - 1:
            return False

        for x in range(int(lower_right.x), int(lower_right.x) + building.dimensions.width):
            for y in range(int(lower_right.y), int(lower_right.y) + building.dimensions.length):
                if not self.free[x][y]:
                    return False

        return True

    def place_building(self, lower_right: Point, building: AbstractBuilding) -> None:
        """
        Places building on map. **Important! Requires manual check of possible_to_place before!**

        :param lower_right: Point - bottom right corner of building desired position,
        :param building: AbstractBuilding - building to be placed.
        :return: void
        """

        for x in range(int(lower_right.x), int(lower_right.x) + building.dimensions.width):
            for y in range(int(lower_right.y), int(lower_right.y) + building.dimensions.length):
                self.free[x][y] = False

        self.buildings.append(building)

    def remove_building(self, building: AbstractBuilding):
        self.buildings.remove(building)
        for x in range(building.map_position[0], building.map_position[0] + building.dimensions.width):
            for y in range(building.map_position[1], building.map_position[1] + building.dimensions.length):
                self.free[x][y] = True

    def find_building_at_field(self, x: int, y: int):
        if self.free[x][y]:
            return None
        for building in self.buildings:
            if building.map_position[0] <= x < building.map_position[0] + building.dimensions.width \
                    and building.map_position[1] <= y < building.map_position[1] + building.dimensions.length:
                return building
