from src.main.buildings.ResidentialBuilding import ResidentialBuilding
from src.main.buildings.util_classes.Dimensions import Dimensions


class Buildings:
    def __init__(self):
        self.build_mode = False
        self.all = []
        self.on_map = []
        self.chosen = ResidentialBuilding("test building", "../assets/temp4.png", Dimensions(1, 1), 0, 0)

    def change_mode(self):
        self.build_mode = not self.build_mode

