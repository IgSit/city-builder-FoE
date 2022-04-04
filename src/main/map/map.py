from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.Buildings import Buildings


class Map:

    def __init__(self, n: int, buildings: Buildings):
        self.free = [[True for _ in range(n)] for _ in range(n)]
        self.buildings = buildings
        self.length = n
        self.width = n
        self.chosen_field = None

    def set_chosen_field(self, point: (int, int)):
        self.chosen_field = point

    def is_free(self, point: (int, int)):
        return self.free[point[0]][point[1]]

    def place_chosen_building(self):
        if self.chosen_field is not None and self.buildings.chosen is not None:
            x, y = self.chosen_field
            if self.free[x][y]:
                self.buildings.chosen.placed = True
                self.free[x][y] = False
                self.buildings.on_map.append(self.buildings.chosen)
                self.buildings.chosen = None


