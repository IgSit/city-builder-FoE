import arcade

from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.gui.util_classes.Point import Point


class BuildingGui:
    """Gui of single backend building."""

    def __init__(self, building: AbstractBuilding, asset_path: str, asset_non_road_path: str = ""):
        self.building: AbstractBuilding = building
        self.asset_path: str = asset_path
        self.asset_non_road_path = asset_non_road_path
        self.screen_coordinates: Point = Point(0, 0)
        self.normal_sprite: arcade.Sprite = arcade.Sprite(asset_path, scale=0.7)
        self.sprite: arcade.Sprite = self.normal_sprite
        self.non_road_sprite = None
        if asset_non_road_path != "":
            self.non_road_sprite = arcade.Sprite(asset_non_road_path, scale=0.7)
            self.sprite = self.non_road_sprite
        self.building_priority = {(1, 1): 0, (2, 1): 1, (1, 2): 2, (2, 2): 3}[(self.building.dimensions.width,
                                                                               self.building.dimensions.length)]

    def lower_left(self):
        x = self.building.map_position[0] + self.building.dimensions.width - 1
        y = self.building.map_position[1] + self.building.dimensions.length - 1
        return x, y


