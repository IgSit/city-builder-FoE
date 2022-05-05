from collections import deque
from typing import Optional

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
        self.road_to_hall: [[bool]] = [[False for _ in range(n)] for _ in range(n)]
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
        self.find_roads_to_hall()

    def remove_building(self, building: AbstractBuilding):
        for x in range(building.map_position[0], building.map_position[0] + building.dimensions.width):
            for y in range(building.map_position[1], building.map_position[1] + building.dimensions.length):
                self.free[x][y] = True

        self.buildings.remove(building)
        self.find_roads_to_hall()

    def find_building_at_field(self, x: int, y: int) -> Optional[AbstractBuilding]:
        if self.free[x][y]:
            return None
        for building in self.buildings:
            if building.map_position[0] <= x < building.map_position[0] + building.dimensions.width \
                    and building.map_position[1] <= y < building.map_position[1] + building.dimensions.length:
                return building

    def connected_to_town_hall(self, lower_left: Point, building: AbstractBuilding):
        if building.name == "town hall":
            return True
        x, y = int(lower_left.x), int(lower_left.y)
        for i in range(building.dimensions.width):
            if 0 <= x + i < self.width and 0 <= y - 1 < self.length and self.road_to_hall[x + i][y - 1]:
                return True
            if 0 <= x + i < self.width and 0 <= y + building.dimensions.length < self.length \
                    and self.road_to_hall[x + i][y + building.dimensions.length]:
                return True

        for j in range(building.dimensions.length):
            if 0 <= x - 1 < self.width and 0 <= y + j < self.length and self.road_to_hall[x - 1][y + j]:
                return True
            if 0 <= x + building.dimensions.width < self.width and 0 <= y + j <= self.length \
                    and self.road_to_hall[x + building.dimensions.width][y + j]:
                return True

        return False

    def find_roads_to_hall(self):
        visited = [[False for _ in range(self.width)] for _ in range(self.length)]
        queue = deque([])

        for a, b in self._find_hall_coordinates():
            visited[a][b] = True
            queue.append((a, b))

        while queue:
            x, y = queue.popleft()
            neighbours: [(int, int)] = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for w, k in neighbours:
                if 0 <= w < self.width and 0 <= k < self.length and not self.free[w][k] and not visited[w][k]:
                    building = self.find_building_at_field(w, k)
                    if building.is_road():
                        visited[w][k] = True
                        queue.append((w, k))

        self.road_to_hall = visited

        for building in self.buildings:
            lower_left = Point(building.map_position[0], building.map_position[1])
            building.connected_to_town = self.connected_to_town_hall(lower_left, building)

    def _find_hall_coordinates(self):
        town_coordinates: [(int, int)] = []
        for building in self.buildings:
            if building.name == "town hall":
                start_x, start_y = building.map_position
                for x in range(start_x, start_x + building.dimensions.width):
                    for y in range(start_y, start_y + building.dimensions.length):
                        town_coordinates.append((x, y))
                return town_coordinates
