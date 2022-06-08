from src.main.buildings.BuildingsManager import BuildingsManager
from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.util_classes.Cost import Cost
from src.main.engine.Engine import Engine


class TechnologiesManager:
    def __init__(self, engine: Engine, buildings_manager: BuildingsManager):
        self.buildings_manager = buildings_manager
        residential = Technology("residential", buildings_manager.buildings_dict["residential"], engine, Cost())
        tenement = Technology("tenement", buildings_manager.buildings_dict["tenement"], engine,
                              Cost(100, 100, 0, 100, 100, 100))
        mansion = Technology("mansion", buildings_manager.buildings_dict["mansion"], engine,
                             Cost(1000, 1000, 0, 1000, 1000, 1000))

        anvil = Technology("anvil", buildings_manager.buildings_dict["anvil"], engine, Cost())
        smith = Technology("smith", buildings_manager.buildings_dict["tenement"], engine,
                              Cost(100, 100, 0, 100, 100, 100))
        main_smith = Technology("main smith", buildings_manager.buildings_dict["main smith"], engine,
                             Cost(1000, 1000, 0, 1000, 1000, 1000))

        field = Technology("field", buildings_manager.buildings_dict["field"], engine, Cost())
        shed = Technology("shed", buildings_manager.buildings_dict["shed"], engine,
                              Cost(100, 100, 0, 100, 100, 100))
        farm = Technology("farm", buildings_manager.buildings_dict["farm"], engine,
                             Cost(1000, 1000, 0, 1000, 1000, 1000))

        tower = Technology("tower", buildings_manager.buildings_dict["tower"], engine, Cost())
        bastion = Technology("bastion", buildings_manager.buildings_dict["bastion"], engine,
                              Cost(100, 100, 0, 100, 100, 100))
        castle = Technology("castle", buildings_manager.buildings_dict["castle"], engine,
                             Cost(1000, 1000, 0, 1000, 1000, 1000))

        tree = Technology("tree", buildings_manager.buildings_dict["tree"], engine, Cost())
        sawmill = Technology("sawmill", buildings_manager.buildings_dict["sawmill"], engine,
                              Cost(100, 100, 0, 100, 100, 100))
        main_sawmill = Technology("main sawmill", buildings_manager.buildings_dict["main sawmill"], engine,
                             Cost(1000, 1000, 0, 1000, 1000, 1000))
        self.technologies = [residential, tenement, mansion, anvil, smith, main_smith, field, shed, farm, tower,
                             bastion, castle, tree, sawmill, main_sawmill]
        self.technologies_dict = {tech.name: tech for tech in self.technologies}
        self.technologies_branches = [
            TechnologyBranch("Residential", residential, tenement, mansion),
            TechnologyBranch("Blacksmithing", anvil, smith, main_smith),
            TechnologyBranch("Farming", field, shed, farm),
            TechnologyBranch("Lumber", tree, sawmill, main_sawmill),
            TechnologyBranch("Defence", tower, bastion, castle)
        ]


class Technology:
    def __init__(self, name: str, building: AbstractBuilding, engine: Engine, unlock_cost: Cost = Cost()):
        self.name = name
        self.unlock_cost = unlock_cost
        self.building = building
        self.engine = engine
        self.unlocked = False
        self.required_technology = None

    def unlock(self):
        if not self.unlocked and self.engine.has_resources(self.unlock_cost) and (self.required_technology is None or
                                                            self.required_technology.unlocked):
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

