from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.util_classes.Cost import Cost
from src.main.resources.Goods import ResourceType, ResourceQuantity


class Resources:
    """Class storing info about 3 main resources, used to place/delete buildings"""

    def __init__(self):
        self.money = ResourceQuantity(ResourceType.MONEY, 10000)
        self.supply = ResourceQuantity(ResourceType.SUPPLY, 10000)
        self.people = ResourceQuantity(ResourceType.PEOPLE, 20)
        self.wheat = ResourceQuantity(ResourceType.WHEAT, 0)
        self.iron = ResourceQuantity(ResourceType.IRON, 0)
        self.wood = ResourceQuantity(ResourceType.WOOD, 10)
        self.resources_dict = {
            ResourceType.MONEY: self.money,
            ResourceType.SUPPLY: self.supply,
            ResourceType.PEOPLE: self.people,
            ResourceType.WHEAT: self.wheat,
            ResourceType.IRON: self.iron,
            ResourceType.WOOD: self.wood
        }

    def has_enough_resources(self, cost: Cost):
        return all(map(lambda g: g.quantity >= cost.cost_dict[g.resource], self.resources_dict.values()))

    def has_enough_resource(self, good: ResourceQuantity):
        return self.resources_dict[good.resource].quantity >= good.quantity

    def on_building(self, building: AbstractBuilding):
        for type_, good in self.resources_dict.items():
            good.quantity -= building.cost.cost_dict[type_]

        self.people.quantity += building.add_new_people()

    def on_destroy(self, building: AbstractBuilding):
        for type_, good in self.resources_dict.items():
            if good.resource != ResourceType.PEOPLE:
                good.quantity += building.cost.cost_dict[type_] // 2
            else:
                good.quantity += building.cost.cost_dict[type_]

        self.people.quantity -= building.add_new_people()

    def get_resources(self):
        return Cost(
            self.money.quantity,
            self.supply.quantity,
            self.people.quantity,
            self.wheat.quantity,
            self.iron.quantity,
            self.wood.quantity
        )

    def operation_on_resource(self, good: ResourceQuantity, func):
        self.resources_dict[good.resource].quantity = \
            func(self.resources_dict[good.resource].quantity, good.quantity)
