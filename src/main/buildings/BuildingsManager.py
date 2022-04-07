from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.ResidentialBuilding import ResidentialBuilding
from src.main.buildings.util_classes.Cost import Cost
from src.main.buildings.util_classes.Dimensions import Dimensions


class BuildingsManager:
    """
    Class to hold all possible buildings and just that.
    """

    def __init__(self):
        residential = ResidentialBuilding("residential", "../main/buildings/assets/temp4.png",
                                          Dimensions(1, 1), Cost(0, 0, 0), 5)
        self.buildings: [AbstractBuilding] = [residential]

    @staticmethod
    def get_copy():
        return ResidentialBuilding("residential", "../main/buildings/assets/temp4.png",
                                   Dimensions(1, 1), Cost(0, 0, 0), 5)
