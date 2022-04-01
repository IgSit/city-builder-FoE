import time

from src.main.buildings.ResidentialBuilding import ResidentialBuilding
from src.main.buildings.util_classes.Cost import Cost
from src.main.buildings.util_classes.Dimensions import Dimensions
from src.main.engine.engine import Engine
from src.main.gui.Button import Button
from src.main.gui.map_gui.map_gui import MapGui
import arcade


class Gui(arcade.Window):
    def __init__(self, run_engine: Engine):
        self.engine = run_engine
        self.map_gui = MapGui(run_engine.map)
        self.screen_width, self.screen_height = arcade.window_commands.get_display_size()
        self.button_list = []

        self.test_building = ResidentialBuilding("test building","../assets/test.png",Dimensions(1,1), 0, 0)
        self.sprites_on_map = arcade.SpriteList()
        self.sprites_on_map.append(self.test_building.building_sprite)

        self.create_button("Build", (10, 160), (10, 50), self.change_mode)
        self.build_mode = False
        super().__init__(1000, 800, fullscreen=True)

    def run(self):
        arcade.run()
        self.on_draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 65307:  # ESC
            arcade.exit()

    def on_draw(self):
        self.clear()
        if self.build_mode:
            self.draw_free_fields()
        self.map_gui.draw_map()
        if self.build_mode:
            self.sprites_on_map.draw()
        for button in self.button_list:
            self.draw_button(button.x_es, button.y_es)

    def draw_free_fields(self):
        for i, row in enumerate(self.engine.map.free):
            for j, field_free in enumerate(row):
                if field_free:
                    self.map_gui.mark_field(i, j)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        for button in self.button_list:
            x1, x2 = button.x_es
            y1, y2 = button.y_es
            if x1 <= x <= x2 and y1 <= y <= y2 and button.action is not None:
                button.action()
                break

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if self.build_mode:
            self.test_building.building_sprite.center_x = x
            self.test_building.building_sprite.center_y = y

    def create_button(self, title: str, x_es: (int, int), y_es: (int, int), action=None):
        button = Button(title, x_es, y_es, action)
        self.button_list.append(button)

    def draw_button(self, x_es: (int, int), y_es: (int, int)):
        x1, x2 = x_es
        y1, y2 = y_es
        arcade.draw_polygon_filled([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], arcade.csscolor.GOLD)

    def change_mode(self):
        self.build_mode = not self.build_mode
