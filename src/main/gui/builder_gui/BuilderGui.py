import arcade
import math as mt
from typing import Optional

from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.buildings.util_classes.Dimensions import Dimensions
from src.main.engine.Engine import Engine
from src.main.gui.builder_gui.BuildingsListSection import BuildingListSection
from src.main.gui.building_gui.BuildingGui import BuildingGui
from src.main.gui.map_gui.MapGui import MapGui
from src.main.buildings.BuildingsManager import BuildingsManager
from src.main.gui.util_classes.Point import Point


class BuilderGui:
    def __init__(self, map_gui: MapGui, engine: Engine, tile_size: int = 64):
        self.map_gui: MapGui = map_gui
        self.engine: Engine = engine
        self.front_building: Optional[BuildingGui] = None
        self.back_building: Optional[AbstractBuilding] = None
        self.mode: Optional[str] = None
        self.tile_size: int = tile_size
        self.screen_width, self.screen_height = arcade.window_commands.get_display_size()
        self.building_manager: BuildingsManager = BuildingsManager()
        self.building_list_section = BuildingListSection(self, self.building_manager)
        self._place_town()

    def on_draw(self):
        if self.mode == "BUILD":
            self.building_list_section.on_draw()
        if self.front_building is not None:
            self._colour_building_tiles()
            self.front_building.sprite.draw()

    def on_mouse_motion(self, x: float, y: float):
        self._set_chosen_building_sprite_coordinates(x, y)

    def on_mouse_drag(self, x: float, y: float):
        self._set_chosen_building_sprite_coordinates(x, y)

    def on_mouse_press(self, x: float, y: float):
        if self.front_building is not None:
            self._place_building()
        elif self.mode == "MOVE":
            self.back_building = self._remove_building(x, y)
            self.front_building = self.building_manager.get_copy_from_building(self.back_building)
            self._set_chosen_building_sprite_coordinates(x, y)
        elif self.mode == "SELL":
            self._remove_building(x, y)

    def on_quit(self):
        if self.mode is not None:
            self.mode = None
            self.front_building = None
            return True
        return False

    def _set_chosen_building_sprite_coordinates(self, x: float, y: float):
        if self.front_building is not None:
            scale = self.front_building.sprite.scale
            self.front_building.sprite.center_x = x
            self.front_building.sprite.bottom = y - self.tile_size / 2 * scale / 0.78

    def _colour_building_tiles(self):
        cords = self.map_gui.find_field_under_cursor()
        if cords is None:
            return

        x, y = cords
        free = self.engine.possible_to_place(Point(x, y), self.front_building.building, self.mode)

        for w in range(x, min(x + self.front_building.building.dimensions.width, self.map_gui.length)):
            for k in range(y, min(y + self.front_building.building.dimensions.length, self.map_gui.width)):
                color = arcade.csscolor.SKY_BLUE if free else arcade.csscolor.RED
                self.map_gui.mark_field(w, k, color)

    def _place_building(self, i=None, j=None):
        if i is None and j is None:
            coords = self.map_gui.find_field_under_cursor()
            if coords is None:
                return
            i, j = coords

        if self.engine.possible_to_place(Point(i, j), self.front_building.building, self.mode):
            self.back_building.map_position = (i, j)
            self.map_gui.map_buildings.append(self.front_building)
            self.map_gui.map_buildings.sort(key=self._lower_left_priority)
            a, b = self.map_gui.get_middle_point(i, j)
            scale = self.front_building.sprite.scale
            dimensions = self.back_building.dimensions
            self.front_building.screen_coordinates = Point(a + self._calc_ratio(dimensions) * self.tile_size,
                                                           b - self.tile_size / 2 * scale / 0.78)
            self.engine.place_building(Point(i, j), self.back_building, self.mode)
            self.front_building = None

    def _remove_building(self, x: float, y: float):
        coords = self.map_gui.find_field_under_cursor()
        if coords is None:
            return
        i, j = coords

        building: AbstractBuilding = self.engine.find_building_at_field(i, j)
        if building is None or (building.name == "town hall" and self.mode == "SELL"):
            return

        self.engine.remove_building(building, self.mode)

        building_list = arcade.SpriteList()
        for building_gui in self.map_gui.map_buildings:
            building_list.append(building_gui.sprite)

        hit_buildings = arcade.get_sprites_at_point((x, y), building_list)
        self.map_gui.remove_building_sprite(hit_buildings[0])

        return building

    def _lower_left_priority(self, building_gui: BuildingGui):
        x, y = building_gui.lower_left()
        a, b = self.map_gui.field_priority[x][y]
        return a, building_gui.building_priority, (-1 + 2*(building_gui.building_priority != 2))*b

    def _place_town(self):
        self.front_building = self.building_manager.get_copy(len(self.building_manager.buildings) - 1)
        self.back_building = self.front_building.building
        self._place_building(0, 0)

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
