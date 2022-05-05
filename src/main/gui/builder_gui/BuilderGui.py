import arcade
import math as mt
from typing import Optional

from src.main.buildings.AbstractBuilding import AbstractBuilding
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
        self.mode: Optional[str] = None
        self.tile_size: int = tile_size
        self.screen_width, self.screen_height = arcade.window_commands.get_display_size()
        self.building_manager: BuildingsManager = BuildingsManager()
        self.building_list_section = BuildingListSection(self, self.building_manager)
        self._place_town()

    def on_draw(self):
        if self.mode == "BUILD":
            self.building_list_section.on_draw()
        if self.chosen_building is not None:
            self._colour_building_tiles()
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

    def on_mouse_press(self, x: float, y: float):
        if self.chosen_building is not None:
            self._place_building()
        elif self.mode == "MOVE":
            building: AbstractBuilding = self._remove_building(x, y)
            self.chosen_building = self.building_manager.get_copy_from_building(building)
        elif self.mode == "SELL":
            self._remove_building(x, y)
        else:
            # kod tylko pokazujący, że działa, docelowo do usunięcia
            cords = self.map_gui.find_field_under_cursor()
            if cords is None:
                return
            x, y = cords
            building = self.engine.find_building_at_field(x, y)
            if building is None:
                return
            print("Connected to town hall", building.connected_to_town)
            # aż dotąd

    def _colour_building_tiles(self):
        cords = self.map_gui.find_field_under_cursor()
        if cords is None:
            return

        x, y = cords
        free = self.engine.map.possible_to_place(Point(x, y), self.chosen_building.building)

        for w in range(x, min(x + self.chosen_building.building.dimensions.width, self.map_gui.length)):
            for k in range(y, min(y + self.chosen_building.building.dimensions.length, self.map_gui.width)):
                color = arcade.csscolor.SKY_BLUE if free else arcade.csscolor.RED
                self.map_gui.mark_field(w, k, color)

    def _place_building(self, i=None, j=None):
        if i is None and j is None:
            coords = self.map_gui.find_field_under_cursor()
            if coords is None:
                return
            i, j = coords

        if self.engine.possible_to_place(Point(i, j), self.chosen_building.building):
            self.chosen_building.building.map_position = (i, j)
            self.map_gui.map_buildings.append(self.chosen_building)
            self.map_gui.map_buildings.sort(key=self._lower_left_priority)
            a, b = self.map_gui.get_middle_point(i, j)
            scale = self.chosen_building.sprite.scale
            dimensions = self.chosen_building.building.dimensions
            self.chosen_building.screen_coordinates = Point(a + self._calc_ratio(dimensions) * self.tile_size,
                                                            b - self.tile_size / 2 * scale / 0.78)
            self.engine.place_building(Point(i, j), self.chosen_building.building, self.mode)
            self.chosen_building = None

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
        return self.map_gui.field_priority[x][y]

    def _place_town(self):
        self.chosen_building = self.building_manager.get_copy(len(self.building_manager.buildings) - 1)
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
