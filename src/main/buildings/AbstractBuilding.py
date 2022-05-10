from abc import ABC
from src.main.buildings.util_classes import Dimensions, Cost
from src.main.resources.Goods import ResourceQuantity, ResourceType
from src.main.work_modes.WorkModes import WorkMode


class AbstractBuilding(ABC):
    """
    Abstract class to handle all typical operations of all buildings (placing, clicking etc). We communicate in gui
    via this class.
    """

    def __init__(self, name: str, dimensions: Dimensions, cost: Cost):
        self.name = name
        self.dimensions = dimensions
        self.cost = cost
        self.map_position = (-1, -1)
        self.connected_to_town = False

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
