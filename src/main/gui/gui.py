import time

from src.main.buildings.ResidentialBuilding import ResidentialBuilding
from src.main.buildings.util_classes.Cost import Cost
from src.main.buildings.util_classes.Dimensions import Dimensions
from src.main.engine.engine import Engine
from src.main.gui.Buildings_gui import BuildingsGui
from src.main.gui.Button import Button
from src.main.gui.Buttons_gui import ButtonsGui
from src.main.gui.map_gui.map_gui import MapGui
import arcade


class Gui(arcade.Window):
    def __init__(self, run_engine: Engine):
        self.engine = run_engine
        self.map_gui = MapGui(run_engine.map)
        self.buildings_gui = BuildingsGui(self)
        self.buttons_gui = ButtonsGui(self)

        self.screen_width, self.screen_height = arcade.window_commands.get_display_size()
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
            self.map_gui.draw_free_fields()
        self.map_gui.draw_map()
        if self.build_mode:
            self.buildings_gui.building_sprites.draw()
        self.buttons_gui.draw_all()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.buttons_gui.are_buttons_pressed(x, y)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.buildings_gui.set_chosen_building_coords(x, y)

    def change_mode(self):
        self.build_mode = not self.build_mode
