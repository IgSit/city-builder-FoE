from abc import ABC
from typing import Optional

from src.main.buildings.util_classes.Dimensions import Dimensions
from src.main.buildings.util_classes.Cost import Cost
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
            if self.time_left <= 0:
                self.time_left = 0
                self.on_finish_work()

    def on_start_work(self, mode: WorkMode):
        """Gather user resources when building starts to work"""
        self.work_mode = mode
        self.time_left = mode.value
        # todo apply cost of starting work to resources (in Production Building)

    def on_finish_work(self):
        self.work_mode = None
        # todo apply cost of starting work to resources (in Production Building)

    @staticmethod
    def get_work_cost(mode: WorkMode):
        if mode in [WorkMode.LAZY, WorkMode.MODERATE, WorkMode.EFFICIENT]:
            return Cost()

    @staticmethod
    def add_new_people():
        """Function used primarily when new building is placed"""
        return 0

    @staticmethod
    def is_road():
        return False
