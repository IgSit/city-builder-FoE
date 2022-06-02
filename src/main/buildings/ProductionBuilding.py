from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.util_classes import Dimensions, Cost
from src.main.resources.Goods import ResourceType


class ProductionBuilding(AbstractBuilding):
    """
    Stores information about production building, what are requirements and products
    now only names, it will be extended in future
    """
    def __init__(self, name: str, dimensions: Dimensions, cost: Cost, required: ResourceType, produced: ResourceType):
        super().__init__(name, dimensions, cost)
        self.required = required
        self.produced = produced
