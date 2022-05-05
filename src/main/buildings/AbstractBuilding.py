from abc import ABC
from src.main.buildings.util_classes import Dimensions, Cost


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
        return 0

    @staticmethod
    def is_road():
        return False
