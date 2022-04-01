from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.util_classes import Dimensions, Cost


class ResidentialBuilding(AbstractBuilding):
    def __init__(self, name: str, asset_path: str, dimensions: Dimensions, cost: Cost, people: int):
        super().__init__(name, asset_path, dimensions, cost)
        self.people = people
