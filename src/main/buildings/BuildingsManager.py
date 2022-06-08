from copy import deepcopy

from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.DefenceBuilding import DefenceBuilding
from src.main.buildings.ProductionBuilding import ProductionBuilding
from src.main.buildings.ResidentialBuilding import ResidentialBuilding
from src.main.buildings.Road import Road
from src.main.buildings.util_classes.Cost import Cost
from src.main.buildings.util_classes.Dimensions import Dimensions
from src.main.engine.Engine import Engine
from src.main.gui.building_gui.BuildingGui import BuildingGui
from src.main.gui.util_classes.Point import Point
from src.main.resources.Goods import ResourceType, ResourceQuantity


class BuildingsManager:
    """
    Class to hold all possible buildings and just that.
    """

    def __init__(self, engine: Engine):
        residential = BuildingGui(ResidentialBuilding("residential", Dimensions(1, 1), Cost(200, 200, 0), 5),
                                  "../main/buildings/assets/temp4.png", "../main/buildings/assets/temp4_non_road.png")
        tenement = BuildingGui(ResidentialBuilding("tenement", Dimensions(2, 1), Cost(400, 400, 0), 15),
                               "../main/buildings/assets/tenement.png",
                               "../main/buildings/assets/tenement_non_road.png")
        mansion = BuildingGui(ResidentialBuilding("mansion", Dimensions(2, 2), Cost(800, 800, 0), 40),
                              "../main/buildings/assets/mansion.png", "../main/buildings/assets/mansion_non_road.png")
        shed = BuildingGui(ProductionBuilding("shed", Dimensions(1, 2), Cost(100, 50, 2),
                                              ResourceQuantity(ResourceType.NULL, 0),
                                              ResourceQuantity(ResourceType.WHEAT, 10), engine),
                           "../main/buildings/assets/shed.png", "../main/buildings/assets/shed_non_road.png")
        smith = BuildingGui(ProductionBuilding("smith", Dimensions(2, 1), Cost(400, 600, 5),
                                               ResourceQuantity(ResourceType.IRON, 10),
                                               ResourceQuantity(ResourceType.SUPPLY, 10), engine),
                            "../main/buildings/assets/smith.png", "../main/buildings/assets/smith_non_road.png")
        tree = BuildingGui(ProductionBuilding("tree", Dimensions(1, 1), Cost(0, 50, 1),
                                              ResourceQuantity(ResourceType.NULL, 0),
                                              ResourceQuantity(ResourceType.WOOD, 10), engine),
                           "../main/buildings/assets/tree.png", "../main/buildings/assets/tree_non_road.png")
        tower = BuildingGui(DefenceBuilding("tower", Dimensions(1, 1), Cost(700, 1000, 10), 0, 0, 0),
                            "../main/buildings/assets/tower.png", "../main/buildings/assets/tower_non_road.png")
        road = BuildingGui(Road("road", Dimensions(1, 1), Cost(50, 50, 0)), "../main/buildings/assets/road.png")
        road.sprite.scale = 0.78
        town_hall = BuildingGui(DefenceBuilding("town hall", Dimensions(2, 2), Cost(0, 0, 0), 0, 0, 0),
                                "../main/buildings/assets/townhall.png")
        field = BuildingGui(ProductionBuilding("field", Dimensions(1, 1), Cost(100, 50, 2),
                                              ResourceQuantity(ResourceType.NULL, 0),
                                              ResourceQuantity(ResourceType.WHEAT, 10), engine),
                           "../main/buildings/assets/temp2.png", "../main/buildings/assets/temp2.png")
        farm = BuildingGui(ProductionBuilding("farm", Dimensions(2, 2), Cost(100, 50, 2),
                                              ResourceQuantity(ResourceType.NULL, 0),
                                              ResourceQuantity(ResourceType.WHEAT, 10), engine),
                           "../main/buildings/assets/shed.png", "../main/buildings/assets/shed_non_road.png")
        anvil = BuildingGui(ProductionBuilding("anvil", Dimensions(1, 1), Cost(400, 600, 5),
                                               ResourceQuantity(ResourceType.IRON, 10),
                                               ResourceQuantity(ResourceType.SUPPLY, 10), engine),
                            "../main/buildings/assets/temp2.png", "../main/buildings/assets/temp2.png")
        sawmill = BuildingGui(ProductionBuilding("sawmill", Dimensions(1, 2), Cost(0, 50, 1),
                                              ResourceQuantity(ResourceType.NULL, 0),
                                              ResourceQuantity(ResourceType.WOOD, 10), engine),
                           "../main/buildings/assets/tree.png", "../main/buildings/assets/tree_non_road.png")
        main_sawmill = BuildingGui(ProductionBuilding("main sawmill", Dimensions(2, 2), Cost(0, 50, 1),
                                              ResourceQuantity(ResourceType.NULL, 0),
                                              ResourceQuantity(ResourceType.WOOD, 10), engine),
                           "../main/buildings/assets/tree.png", "../main/buildings/assets/tree_non_road.png")
        main_smith = BuildingGui(ProductionBuilding("main smith", Dimensions(2, 2), Cost(400, 600, 5),
                                               ResourceQuantity(ResourceType.IRON, 10),
                                               ResourceQuantity(ResourceType.SUPPLY, 10), engine),
                            "../main/buildings/assets/smith.png", "../main/buildings/assets/smith_non_road.png")
        bastion = BuildingGui(DefenceBuilding("bastion", Dimensions(1, 2), Cost(700, 1000, 10), 0, 0, 0),
                            "../main/buildings/assets/tower.png", "../main/buildings/assets/tower_non_road.png")
        castle = BuildingGui(DefenceBuilding("castle", Dimensions(2, 2), Cost(700, 1000, 10), 0, 0, 0),
                            "../main/buildings/assets/tower.png", "../main/buildings/assets/tower_non_road.png")

        self.buildings: [BuildingGui] = [road, tower, smith, tree, shed, residential, tenement, mansion,
                                         field, farm, anvil, sawmill, main_sawmill, main_smith, bastion, castle,
                                         town_hall]
        self.buildings_dict: {str: BuildingGui} = {building.building.name: building for building in self.buildings}

    def get_copy(self, i: int):
        return deepcopy(self.buildings[i])

    def get_copy_by_name(self, name: str):
        return deepcopy(self.buildings_dict.get(name))

    def get_copy_from_building(self, building: AbstractBuilding):
        if building is None:
            return
        return self.buildings_dict.get(building.name)
