import arcade

from src.main.engine.Engine import Engine
from src.main.gui.builder_gui.BuilderGui import BuilderGui
from src.main.gui.controls_gui.ControlsGui import ControlsGui
from src.main.gui.map_gui.MapGui import MapGui
from src.main.gui.market_gui.MarketSection import MarketSection
from src.main.gui.technologies_gui.TechnologiesSection import TechnologiesSection
from src.main.gui.work_mode_gui.WorkModeGui import WorkModeGui


class Gui(arcade.Window):

    def __init__(self, engine: Engine):
        super().__init__(100, 800, fullscreen=True)
        self.engine = engine
        self.market_section = MarketSection(engine)
        self.map_gui = MapGui(engine)
        self.builder_gui = BuilderGui(self.map_gui, engine)
        self.tech_section = TechnologiesSection(self.builder_gui.building_manager, engine)
        self.controls_gui = ControlsGui(self.builder_gui, self.map_gui, self.market_section, self.tech_section,
                                        self.engine)
        self.work_mode_gui = WorkModeGui(self.map_gui, self.builder_gui, self.engine)

    def run(self):
        arcade.run()

    def on_draw(self):
        self.clear()
        self.map_gui.on_draw()
        self.builder_gui.on_draw()
        self.controls_gui.on_draw()
        self.market_section.on_draw()
        self.tech_section.on_draw()
        self.work_mode_gui.on_draw()

    def on_update(self, dt: float):
        self.work_mode_gui.on_update(dt)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == 1:  # left
            self.builder_gui.on_mouse_press(x, y)
            self.work_mode_gui.on_mouse_press()

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, buttons: int, modifiers: int):
        if buttons == 2:  # middle mouse button
            self.map_gui.on_mouse_drag(x, y, dx, dy)
            self.builder_gui.on_mouse_drag(x, y)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.map_gui.on_mouse_motion(x, y)
        self.builder_gui.on_mouse_motion(x, y)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self._escape_click()

    def _escape_click(self):
        if self.tech_section.on_quit():
            return
        if self.market_section.on_quit():
            return
        if self.builder_gui.on_quit() or self.work_mode_gui.on_quit():
            return
        else:
            arcade.exit()
