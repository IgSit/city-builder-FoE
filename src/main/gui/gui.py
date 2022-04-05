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
        self.map_gui = MapGui(run_engine.map_)
        self.buildings_gui = BuildingsGui(run_engine.buildings)
        self.buttons_gui = ButtonsGui(self)
        self.screen_width, self.screen_height = arcade.window_commands.get_display_size()
        super().__init__(1000, 800, fullscreen=True)

    def run(self):
        arcade.run()
        self.on_draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 65307:  # ESC
            arcade.exit()

    def on_draw(self):
        self.clear()
        if self.engine.buildings.build_mode:
            self.map_gui.draw_free_fields()
        self.map_gui.draw_map()
        if self.engine.buildings.build_mode:
            self.map_gui.find_field_under_mouse()
            self.buildings_gui.draw_chosen_building()
        self.buildings_gui.draw_buildings_on_map()
        self.buttons_gui.draw_all()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == 1:
            self.buttons_gui.are_buttons_pressed(x, y)
        if button == 4:
            self.buildings_gui.set_chosen_coords(self.map_gui.get_chosen_field_middle_point())
            self.engine.place_chosen_on_map()

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, buttons: int, modifiers: int):
        if buttons == 2:  # middle mouse button
            self.map_gui.x_offset += dx
            self.map_gui.y_offset += dy
            self.map_gui.x_offset = min(max(self.map_gui.x_offset, -500), 500)
            self.map_gui.y_offset = min(max(self.map_gui.y_offset, -250), 350)
            self.map_gui.draw_map()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.buildings_gui.set_chosen_coords((x, y))
        self.map_gui.set_mouse_at_field(x, y)
