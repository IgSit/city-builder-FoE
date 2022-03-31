from src.main.engine.engine import Engine
from src.main.gui.map_gui.map_gui import MapGui
import arcade


class Gui(arcade.Window):
    def __init__(self, run_engine: Engine):
        self.engine = run_engine
        self.map_gui = MapGui(run_engine.map)
        self.screen_width, self.screen_height = arcade.window_commands.get_display_size()
        super().__init__(1000, 800, fullscreen=True)

    def run(self):
        arcade.run()
        self.on_draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 65307:  # ESC
            arcade.exit()

    def on_draw(self):
        self.map_gui.draw_map()
