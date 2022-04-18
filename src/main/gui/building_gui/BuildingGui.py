import arcade

from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.gui.util_classes.Point import Point


class BuildingGui:
    """Gui of single backend building."""

    def __init__(self, building: AbstractBuilding, asset_path: str):
        self.building: AbstractBuilding = building
        self.asset_path: str = asset_path
        self.screen_coordinates: Point = Point(0, 0)
        self.sprite: arcade.Sprite = arcade.Sprite(asset_path, scale=0.6)

    def lower_left(self):
        x = self.building.map_position[0] + self.building.dimensions.width - 1
        y = self.building.map_position[1]
        return x, y
