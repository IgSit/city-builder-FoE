from copy import deepcopy

from src.main.buildings.DefenceBuilding import DefenceBuilding
from src.main.buildings.ProductionBuilding import ProductionBuilding
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
        shed = BuildingGui(ProductionBuilding("shed", Dimensions(1, 2), Cost(0, 0, 0), "nothing", "wheat"),
                           "../main/buildings/assets/shed.png")
        smith = BuildingGui(ProductionBuilding("smith", Dimensions(2, 1), Cost(0, 0, 0), "iron ore", "tools"),
                            "../main/buildings/assets/smith.png")
        tree = BuildingGui(ProductionBuilding("tree", Dimensions(1, 1), Cost(0, 0, 0), "nothing", "wood"),
                           "../main/buildings/assets/tree.png")
        tower = BuildingGui(DefenceBuilding("tower", Dimensions(1, 1), Cost(0, 0, 0), 0, 0, 0),
                            "../main/buildings/assets/tower.png")
        town_hall = BuildingGui(DefenceBuilding("town hall", Dimensions(2, 2), Cost(0, 0, 0), 0, 0, 0),
                                "../main/buildings/assets/townhall.png")
        self.buildings: [BuildingGui] = [tower, town_hall, smith, tree, shed, residential]

    def get_copy(self, i: int):
        return deepcopy(self.buildings[i])
