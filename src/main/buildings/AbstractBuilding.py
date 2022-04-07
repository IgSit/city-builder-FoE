import arcade
from abc import ABC
from src.main.buildings.util_classes import Dimensions, Cost
from src.main.gui.util_classes.Point import Point


class AbstractBuilding(ABC):
    """
    Abstract class to handle all typical operations of all buildings (placing, clicking etc). We communicate in gui
    via this class.
    """

    def __init__(self, name: str, asset_path: str, dimensions: Dimensions, cost: Cost):
        self.name = name
        self.asset_path = asset_path
        self.dimensions = dimensions
        self.cost = cost
        self.screen_coordinates = Point(0, 0)
        self.map_position = (-1, -1)
        self.sprite = arcade.Sprite(asset_path, scale=0.6)

    def is_after(self, other):
        """
        Checks whether building is after the other building according to map position.
        (Building is after when x index is bigger or x indexes are equal and y index is bigger.)

        :param other: AbstractBuilding
        :return: bool
        """

        return self.map_position[0] > other.map_position[0] or \
               (self.map_position[0] == other.map_position[0] and self.map_position[1] > other.map_position[1])
