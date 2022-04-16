from copy import deepcopy

from src.main.buildings.ResidentialBuilding import ResidentialBuilding
from src.main.buildings.util_classes.Cost import Cost
from src.main.buildings.util_classes.Dimensions import Dimensions
from src.main.gui.building_gui.BuildingGui import BuildingGui


class BuildingsManager:
    """
    Class to hold all possible buildings and just that.
    """

    def __init__(self):
        residential = BuildingGui(ResidentialBuilding("residential", Dimensions(1, 1), Cost(0, 0, 0), 5),
                                  "../main/buildings/assets/temp4.png")
        self.buildings: [BuildingGui] = [residential]

    def get_copy(self, i: int):
        return deepcopy(self.buildings[i])
