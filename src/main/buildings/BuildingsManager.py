from copy import deepcopy

from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.DefenceBuilding import DefenceBuilding
from src.main.buildings.ProductionBuilding import ProductionBuilding
from src.main.buildings.ResidentialBuilding import ResidentialBuilding
from src.main.buildings.Road import Road
from src.main.buildings.util_classes.Cost import Cost
from src.main.buildings.util_classes.Dimensions import Dimensions
from src.main.gui.building_gui.BuildingGui import BuildingGui


class BuildingsManager:
    """
    Class to hold all possible buildings and just that.
    """

    def __init__(self):
        residential = BuildingGui(ResidentialBuilding("residential", Dimensions(1, 1), Cost(200, 200, 0), 5),
                                  "../main/buildings/assets/temp4.png")
        shed = BuildingGui(ProductionBuilding("shed", Dimensions(1, 2), Cost(100, 50, 2), "nothing", "wheat"),
                           "../main/buildings/assets/shed.png")
        smith = BuildingGui(ProductionBuilding("smith", Dimensions(2, 1), Cost(400, 600, 5), "iron ore", "tools"),
                            "../main/buildings/assets/smith.png")
        tree = BuildingGui(ProductionBuilding("tree", Dimensions(1, 1), Cost(0, 50, 1), "nothing", "wood"),
                           "../main/buildings/assets/tree.png")
        tower = BuildingGui(DefenceBuilding("tower", Dimensions(1, 1), Cost(700, 1000, 10), 0, 0, 0),
                            "../main/buildings/assets/tower.png")
        road = BuildingGui(Road("road", Dimensions(1, 1), Cost(50, 50, 0)), "../main/buildings/assets/road.png")
        town_hall = BuildingGui(DefenceBuilding("town hall", Dimensions(2, 2), Cost(0, 0, 0), 0, 0, 0),
                                           "../main/buildings/assets/townhall.png")

        # town hall ma być ostatni
        self.buildings: [BuildingGui] = [tower, smith, tree, shed, residential, road, residential, town_hall]

    def get_copy(self, i: int):
        return deepcopy(self.buildings[i])

    def get_copy_from_building(self, building: AbstractBuilding):
        if building is None:
            return
        for i in range(len(self.buildings)):
            if self.buildings[i].building.name == building.name:
                return self.get_copy(i)
