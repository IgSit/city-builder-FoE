from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.util_classes.Cost import Cost
from src.main.buildings.util_classes.Dimensions import Dimensions


class Road(AbstractBuilding):

    def __init__(self, name: str, dimensions: Dimensions, cost: Cost):
        super().__init__(name, dimensions, cost)

    @staticmethod
    def is_road():
        return True
