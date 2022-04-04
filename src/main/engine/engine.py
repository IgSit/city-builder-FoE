from src.main.buildings.Buildings import Buildings
from src.main.map.map import Map


class Engine:

    def __init__(self, map_size: int):
        self.buildings = Buildings()
        self.map_ = Map(map_size, self.buildings)

    def place_chosen_on_map(self):
        if self.buildings.build_mode:
            self.map_.place_chosen_building()

    def run(self):
        pass
