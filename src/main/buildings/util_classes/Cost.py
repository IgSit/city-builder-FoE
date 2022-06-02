from src.main.resources.Goods import ResourceType


class Cost:
    def __init__(self,
                 money_cost: int = 0,
                 supply_cost: int = 0,
                 people_cost: int = 0,
                 wheat_cost: int = 0,
                 iron_cost: int = 0,
                 wood_cost: int = 0):
        self.money_cost = money_cost
        self.supply_cost = supply_cost
        self.people_cost = people_cost
        self.wheat_cost = wheat_cost
        self.iron_cost = iron_cost
        self.wood_cost = wood_cost
        self.cost_dict = {
            ResourceType.MONEY: money_cost,
            ResourceType.SUPPLY: supply_cost,
            ResourceType.PEOPLE: people_cost,
            ResourceType.WHEAT: wheat_cost,
            ResourceType.IRON: iron_cost,
            ResourceType.WOOD: wood_cost
        }
