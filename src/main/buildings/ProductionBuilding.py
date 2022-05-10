from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.util_classes import Dimensions, Cost
from src.main.resources.Goods import ResourceQuantity, ResourceType
from src.main.work_modes.WorkModes import WorkMode


class ProductionBuilding(AbstractBuilding):
    """
    Stores information about production building, what are requirements and products
    now only names, it will be extended in future
    """
    def __init__(self, name: str, dimensions: Dimensions, cost: Cost, required: ResourceType, produced: ResourceType):
        super().__init__(name, dimensions, cost)
        self.required = required
        self.produced = produced

    def on_start_work(self, mode: WorkMode) -> ResourceQuantity:
        """Gather user resources when building starts to work"""
        if mode == WorkMode.EFFICIENT:
            return ResourceQuantity(self.required, 200)
        if mode == WorkMode.MODERATE:
            return ResourceQuantity(self.required, 600)
        if mode == WorkMode.LAZY:
            return ResourceQuantity(self.required, 2000)

    def on_finish_work(self, mode: WorkMode) -> ResourceQuantity:
        """Give user new resources when work is finished"""
        if mode == WorkMode.EFFICIENT:
            return ResourceQuantity(self.produced, 100)
        if mode == WorkMode.MODERATE:
            return ResourceQuantity(self.produced, 300)
        if mode == WorkMode.LAZY:
            return ResourceQuantity(self.produced, 1000)
