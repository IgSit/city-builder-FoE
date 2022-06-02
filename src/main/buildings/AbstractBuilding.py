from abc import ABC
from typing import Optional

from src.main.buildings.util_classes import Dimensions, Cost
from src.main.resources.Goods import ResourceQuantity, ResourceType
from src.main.work_modes.WorkModes import WorkMode


class AbstractBuilding(ABC):
    """
    Abstract class to handle all typical operations of all buildings (placing, clicking etc). We communicate in gui
    via this class.
    """

    def __init__(self, name: str, dimensions: Dimensions, cost: Cost):
        self.name: str = name
        self.dimensions: Dimensions = dimensions
        self.cost: Cost = cost
        self.map_position: (int, int) = (-1, -1)
        self.connected_to_town: bool = False
        self.work_mode: Optional[WorkMode] = None
        self.time_left: float = 0

    def on_update(self, dt: float):
        if self.connected_to_town and self.time_left > 0:
            self.time_left -= dt
            self.time_left = max(self.time_left, 0)

    @staticmethod
    def add_new_people():
        """Function used primarily when new building is placed"""
        return 0

    @staticmethod
    def is_road():
        return False

    @staticmethod
    def on_start_work(mode: WorkMode) -> ResourceQuantity:
        """Gather user resources when building starts to work"""
        if mode == WorkMode.EFFICIENT:
            return ResourceQuantity(ResourceType.NULL, 0)
        if mode == WorkMode.MODERATE:
            return ResourceQuantity(ResourceType.NULL, 0)
        if mode == WorkMode.LAZY:
            return ResourceQuantity(ResourceType.NULL, 0)

    @staticmethod
    def on_finish_work(mode: WorkMode) -> ResourceQuantity:
        """Give user new resources when work is finished"""
        if mode == WorkMode.EFFICIENT:
            return ResourceQuantity(ResourceType.NULL, 0)
        if mode == WorkMode.MODERATE:
            return ResourceQuantity(ResourceType.NULL, 0)
        if mode == WorkMode.LAZY:
            return ResourceQuantity(ResourceType.NULL, 0)
