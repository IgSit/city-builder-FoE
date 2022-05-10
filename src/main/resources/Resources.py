from enum import Enum, auto

from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.util_classes.Cost import Cost


class Resources:

    def __init__(self):
        self.money = 1000
        self.supply = 1000
        self.people = 15

    def has_enough_resources(self, building: AbstractBuilding):
        cost: Cost = building.cost
        return cost.money_cost <= self.money and cost.supply_cost <= self.supply and cost.people_cost <= self.people

    def on_building(self, building: AbstractBuilding):
        self.money -= building.cost.money_cost
        self.supply -= building.cost.supply_cost
        self.people -= building.cost.people_cost

        self.people += building.add_new_people()

    def on_destroy(self, building: AbstractBuilding):
        self.money += building.cost.money_cost // 2
        self.supply += building.cost.supply_cost // 2
        self.people += building.cost.people_cost

        self.people -= building.add_new_people()


class ResourceType(Enum):
    MONEY, SUPPLY, PEOPLE = auto, auto, auto
    WHEAT, IRON, WOOD = auto, auto, auto
    NULL = auto
