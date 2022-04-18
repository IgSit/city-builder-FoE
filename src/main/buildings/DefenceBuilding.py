from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.util_classes import Dimensions, Cost


class DefenceBuilding(AbstractBuilding):
    """
    Stores information about defence building values of durability, damage and range
    """
    def __init__(self, name: str, dimensions: Dimensions, cost: Cost, durability: int, damage: int, range_: int):
        super().__init__(name, dimensions, cost)
        self.durability = durability
        self.damage = damage
        self.range_ = range_
