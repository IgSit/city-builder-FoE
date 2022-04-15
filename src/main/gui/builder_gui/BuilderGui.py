from src.main.engine.engine import Engine
from src.main.gui.map_gui.MapGui import MapGui
from src.main.buildings.BuildingsManager import BuildingsManager
from src.main.gui.util_classes.Button import Button
from src.main.gui.util_classes.Point import Point


class BuilderGui:
    def __init__(self, map_gui: MapGui, engine: Engine, tile_size: int = 64):
        self.map_gui = map_gui
        self.engine = engine
        self.tile_size = tile_size
        self.building_manager = BuildingsManager()
        self.buttons = [Button("Build", Point(0, 0), Point(100, 100), click_function=self.choose_building)]
        self.chosen_building = None

    def on_draw(self):
        for button in self.buttons:
            button.draw_button()
        if self.chosen_building is not None:
            self.chosen_building.sprite.draw()

    def on_mouse_motion(self, x: float, y: float):
        if self.chosen_building is not None:
            scale = self.chosen_building.sprite.scale
            self.chosen_building.sprite.center_x = x
            self.chosen_building.sprite.bottom = y - self.tile_size / 2 * (1 - (0.78 - scale))

    def on_mouse_drag(self, x: float, y: float):
        if self.chosen_building is not None:
            scale = self.chosen_building.sprite.scale
            self.chosen_building.sprite.center_x = x
            self.chosen_building.sprite.bottom = y - self.tile_size / 2 * (1 - (0.78 - scale))

    def on_mouse_press(self, x: float, y: float):
        for button in self.buttons:
            if button.is_clicked(Point(x, y)):
                button.click_function()

        if self.chosen_building is not None:
            coords = self.map_gui.find_field_under_cursor()
            if coords is None:
                return
            i, j = coords
            self._place_building(i, j)

    def choose_building(self):
        if self.chosen_building is not None:
            self.chosen_building = None
        else:
            self.chosen_building = self.building_manager.get_copy()

    def _place_building(self, i: int, j: int):
        if self.engine.place_building_on_map(Point(i, j), self.chosen_building.building):
            self.chosen_building.building.map_position = (i, j)
            self._append_building_to_lists()
            a, b = self.map_gui.get_middle_point(i, j)
            scale = self.chosen_building.sprite.scale
            self.chosen_building.screen_coordinates = Point(a, b - self.tile_size / 2 * (1 - (0.78 - scale)))
            self.chosen_building = None

    def _append_building_to_lists(self):
        """
        Inserts a building in sorted array of buildings **(inserts both to map_gui.map_buildings and
        map_gui.map_buildings_sprite_list)**.

        :return: void
        """

        self.map_gui.map_buildings.append(self.chosen_building)
        self.map_gui.map_building_sprite_list.append(self.chosen_building.sprite)
        i = len(self.map_gui.map_buildings) - 1
        while i > 0:
            while self.chosen_building.is_after(self.map_gui.map_buildings[i - 1]):
                prev = self.map_gui.map_buildings[i - 1]
                curr = self.map_gui.map_buildings[i]
                self.map_gui.map_buildings[i - 1], self.map_gui.map_buildings[i] = curr, prev
                i -= 1
                if i == 0:
                    break
            else:
                break
