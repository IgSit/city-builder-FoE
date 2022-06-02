import arcade

from src.main.engine.Engine import Engine
from src.main.gui.builder_gui.BuilderGui import BuilderGui
from src.main.gui.map_gui.MapGui import MapGui
from src.main.gui.market_gui.MarketSection import MarketSection
from src.main.gui.technologies_gui.TechnologiesSection import TechnologiesSection
from src.main.gui.util_classes.Button import Button
from src.main.gui.util_classes.Point import Point


class ControlsGui(arcade.View):

    def __init__(self, builder_gui: BuilderGui, map_gui: MapGui, market_section: MarketSection,
                 tech_section: TechnologiesSection, engine: Engine):
        super().__init__()
        self.builder_gui: BuilderGui = builder_gui
        self.map_gui: MapGui = map_gui
        self.market_section: MarketSection = market_section
        self.tech_section = tech_section
        self.buttons: [Button] = self._init_buttons()
        self.engine = engine
        self.resources = self.engine.get_resources()

    def on_draw(self):
        self._draw_resources()
        for button in self.buttons:
            button.draw_button()

    def _init_buttons(self):
        funcs = [self._toggle_build_mode, self._toggle_move_mode, self._toggle_sell_mode, self._toggle_tech_mode,
                 self._toggle_market_mode]
        texts = ["Build", "Move", "Sell", "Tech", "Market"]
        buttons: [Button] = []
        for i in range(len(funcs)):
            buttons.append(Button(texts[i], Point(100 * i, 0), Point(100 * (i + 1), 30), click_function=funcs[i]))
        return buttons

    def _draw_resources(self):
        self.resources = self.engine.get_resources()
        width, height, separator = 70, 25, 20
        texts = ["M: " + str(self.resources.money_cost), "S: " + str(self.resources.supply_cost),
                 "P: " + str(self.resources.people_cost), "WH: " + str(self.resources.wheat_cost),
                 "I: " + str(self.resources.iron_cost), "W: " + str(self.resources.wood_cost),
                 ]
        for i in range(len(texts)):
            arcade.draw_lrtb_rectangle_outline(left=width*i + (i + 1)*separator, right=(i + 1)*(width + separator),
                                               top=self.window.height - separator,
                                               bottom=self.window.height - height - separator,
                                               color=arcade.csscolor.ALICE_BLUE, border_width=3)
            arcade.draw_text(text=texts[i], start_x=25 + (width + separator) * i, start_y=self.window.height-40)

    def _toggle_build_mode(self):
        self.builder_gui.mode = "BUILD"

    def _toggle_move_mode(self):
        self.builder_gui.mode = "MOVE"

    def _toggle_sell_mode(self):
        self.builder_gui.mode = "SELL"

    def _toggle_tech_mode(self):
        self.tech_section.change_mode()

    def _toggle_market_mode(self):
        self.market_section.change_mode()
