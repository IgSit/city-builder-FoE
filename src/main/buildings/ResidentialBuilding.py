from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.util_classes import Dimensions, Cost


class ResidentialBuilding(AbstractBuilding):
    def __init__(self, name: str, dimensions: Dimensions, cost: Cost, people: int):
        super().__init__(name, dimensions, cost)
        self.people = people

    def add_new_people(self):
        return self.people
