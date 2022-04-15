import arcade

from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.gui.util_classes.Point import Point


class BuildingGui:
    """Gui of single backend building."""

    def __init__(self, building: AbstractBuilding, asset_path: str):
        self.building = building
        self.asset_path = asset_path
        self.screen_coordinates = Point(0, 0)
        self.sprite = arcade.Sprite(asset_path, scale=0.6)

    def is_after(self, other):
        """
        Checks whether building is after the other building according to map position.
        (Building is after when x index is bigger or x indexes are equal and y index is bigger.)

        :param other: AbstractBuilding
        :return: bool
        """

        return self.building.map_position[0] > other.building.map_position[0] or \
               (self.building.map_position[0] == other.building.map_position[0] and
                self.building.map_position[1] > other.building.map_position[1])
