from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.util_classes.Cost import Cost
from src.main.resources.Goods import ResourceType, ResourceQuantity


class Resources:
    """Class storing info about 3 main resources, used to place/delete buildings"""

    def __init__(self):
        self.money = ResourceQuantity(ResourceType.MONEY, 10000)
        self.supply = ResourceQuantity(ResourceType.SUPPLY, 10000)
        self.people = ResourceQuantity(ResourceType.PEOPLE, 120)
        self.wheat = ResourceQuantity(ResourceType.WHEAT, 120)
        self.iron = ResourceQuantity(ResourceType.IRON, 120)
        self.wood = ResourceQuantity(ResourceType.WOOD, 120)
        self.resources_dict = {
            ResourceType.MONEY: self.money,
            ResourceType.SUPPLY: self.supply,
            ResourceType.PEOPLE: self.people,
            ResourceType.WHEAT: self.wheat,
            ResourceType.IRON: self.iron,
            ResourceType.WOOD: self.wood,
            ResourceType.NULL: ResourceQuantity(ResourceType.NULL, 0)
        }

    def has_enough_resources(self, cost: Cost):
        return all(map(lambda g: g.quantity >= cost.cost_dict[g.resource], self.resources_dict.values()))

    def has_enough_resource(self, good: ResourceQuantity):
        return self.resources_dict[good.resource].quantity >= good.quantity

    def on_building(self, building: AbstractBuilding):
        self.operation_on_resources(building.cost, lambda x, y: x.quantity - y)
        self.people.quantity += building.add_new_people()

    def on_destroy(self, building: AbstractBuilding):
        self.operation_on_resources(building.cost, lambda x, y: x.quantity + y // 2
        if x.resource != ResourceType.PEOPLE else x.quantity + y)
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

    def resource_to_cost(self, good: ResourceQuantity):
        vals = [good.quantity if good.resource == resource else 0 for resource in self.resources_dict.keys()][:-1]
        return Cost(*vals)

    def to_string(self):
        return f'M:{self.money.quantity} S:{self.supply.quantity} P:{self.people.quantity} ' \
               f'WH:{self.wheat.quantity} I:{self.iron.quantity} W:{self.wood.quantity}'

    def operation_on_resource(self, good: ResourceQuantity, func):
        self.operation_on_resources(self.resource_to_cost(good), func)

    def operation_on_resources(self, cost: Cost, func):
        for type_, good in self.resources_dict.items():
            good.quantity = func(good, cost.cost_dict[type_])
