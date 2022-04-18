import arcade
import math as mt
from typing import Optional

from src.main.buildings.util_classes.Dimensions import Dimensions
from src.main.engine.engine import Engine
from src.main.gui.builder_gui.BuildingsListSection import BuildingListSection
from src.main.gui.building_gui.BuildingGui import BuildingGui
from src.main.gui.map_gui.MapGui import MapGui
from src.main.buildings.BuildingsManager import BuildingsManager
from src.main.gui.util_classes.Point import Point


class BuilderGui:
    def __init__(self, map_gui: MapGui, engine: Engine, tile_size: int = 64):
        self.map_gui: MapGui = map_gui
        self.engine: Engine = engine
        self.chosen_building: Optional[BuildingGui] = None
        self.builder_mode: bool = False
        self.tile_size: int = tile_size
        self.screen_width, self.screen_height = arcade.window_commands.get_display_size()
        self.building_manager: BuildingsManager = BuildingsManager()
        self.building_list_section = BuildingListSection(self, self.building_manager)

    def on_draw(self):
        if self.builder_mode:
            self.building_list_section.on_draw()
        if self.chosen_building is not None:
            self.chosen_building.sprite.draw()

    def on_mouse_motion(self, x: float, y: float):
        if self.chosen_building is not None:
            scale = self.chosen_building.sprite.scale
            self.chosen_building.sprite.center_x = x
            self.chosen_building.sprite.bottom = y - self.tile_size / 2 * scale / 0.78

    def on_mouse_drag(self, x: float, y: float):
        if self.chosen_building is not None:
            scale = self.chosen_building.sprite.scale
            self.chosen_building.sprite.center_x = x
            self.chosen_building.sprite.bottom = y - self.tile_size / 2 * scale / 0.78

    def on_mouse_press(self):
        if self.chosen_building is not None:
            coords = self.map_gui.find_field_under_cursor()
            if coords is None:
                return
            i, j = coords
            self._place_building(i, j)

    def _place_building(self, i: int, j: int):
        if self.engine.place_building_on_map(Point(i, j), self.chosen_building.building):
            self.chosen_building.building.map_position = (i, j)
            self._append_building_to_lists()
            self.map_gui.map_buildings.sort(key=self._lower_left_priority)
            a, b = self.map_gui.get_middle_point(i, j)
            scale = self.chosen_building.sprite.scale
            dimensions = self.chosen_building.building.dimensions
            self.chosen_building.screen_coordinates = Point(a + self._calc_ratio(dimensions)*self.tile_size,
                                                            b - self.tile_size/2*scale/0.78)
            self.chosen_building = None

    def _append_building_to_lists(self):
        """
        Inserts a building in sorted array of buildings **(inserts both to map_gui.map_buildings and
        map_gui.map_buildings_sprite_list)**.

        :return: void
        """

        self.map_gui.map_buildings.append(self.chosen_building)
        self.map_gui.map_building_sprite_list.append(self.chosen_building.sprite)

    def _lower_left_priority(self, building_gui: BuildingGui):
        x, y = building_gui.lower_left()
        return self.map_gui.field_priority[x][y]

    @staticmethod
    def _calc_ratio(dimensions: Dimensions):
        """
        Calculates ratio of multiplying tile to be able to find bottom x value of sprite

        :param dimensions: Dimensions
        :return: float
        """
        if dimensions.width <= dimensions.length:
            a = dimensions.width
            b = dimensions.length
            sign = 1
        else:
            a = dimensions.length
            b = dimensions.width
            sign = -1
        d = mt.sqrt(a * a + b * b - a * b) / 2
        return sign * d * mt.sin(mt.pi / 3 - mt.asin(mt.sqrt(3) / 4 * a / d))
