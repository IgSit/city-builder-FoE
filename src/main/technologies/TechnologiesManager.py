from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.util_classes.Cost import Cost
from src.main.engine.Engine import Engine


class TechnologiesManager:
    def __init__(self, engine: Engine):
        self.technologies_list = []


class Technology:
    def __init__(self, name: str, building: AbstractBuilding, engine: Engine, unlock_cost: Cost = Cost()):
        self.name = name
        self.unlock_cost = unlock_cost
        self.building = building
        self.engine = engine
        self.unlocked = False
        self.required_technology = None

    def unlock(self):
        if self.engine.has_resources(self.unlock_cost) and self.required_technology is None or\
                self.required_technology.unlocked:
            self.engine.remove_resources(self.unlock_cost)
            self.unlocked = True


class TechnologyBranch:
    def __init__(self, name: str, basic: Technology, intermediate: Technology, advanced: Technology):
        self.name = name
        self.basic = basic
        self.intermediate = intermediate
        self.advanced = advanced
        self.intermediate.required_technology = self.basic
        self.advanced.required_technology = self.intermediate

