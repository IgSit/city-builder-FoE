from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.util_classes import Dimensions, Cost
from src.main.engine.Engine import Engine

from src.main.resources.Goods import ResourceType, ResourceQuantity
from src.main.work_modes.WorkModes import WorkMode


class ProductionBuilding(AbstractBuilding):
    """
    Stores information about production building, what are requirements and products
    now only names, it will be extended in future
    """
    def __init__(self, name: str, dimensions: Dimensions, cost: Cost, required: ResourceQuantity,
                 produced: ResourceQuantity, engine: Engine):
        super().__init__(name, dimensions, cost)
        self.required = required
        self.produced = produced
        self.engine = engine

    def on_start_work(self, mode: WorkMode):
        """Gather user resources when building starts to work"""
        self.work_mode = mode
        self.time_left = mode.value
        if self.engine.has_resources(self.engine.resources.resource_to_cost(self.required)):
            self.engine.remove_resource(self.required)
        # todo condition has enough resources

    def on_finish_work(self):
        self.work_mode = None
        self.engine.add_resource(self.produced)

