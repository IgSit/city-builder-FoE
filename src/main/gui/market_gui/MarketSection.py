import arcade
from src.main.trade_offers.TradeManager import TradeManager

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
PANEL_WIDTH = 1000
PANEL_HEIGHT = 666


class MarketSection(arcade.View):
    def __init__(self):
        global SCREEN_WIDTH, SCREEN_HEIGHT
        super().__init__()
        SCREEN_WIDTH = self.window.width
        SCREEN_HEIGHT = self.window.height
        self._trade_mode = False
        self.trade_manager = TradeManager()
        self.panel = MarketPanel(self.trade_manager,
                                 left=(self.window.width - PANEL_WIDTH)/2, bottom=(1 / 8 * self.window.height),
                                 width=PANEL_WIDTH, height=PANEL_HEIGHT,
                                 prevent_dispatch={True}, prevent_dispatch_view={True})
        self.section_manager.add_section(self.panel)

    def on_draw(self):
        if self._trade_mode:
            self.panel.on_draw()

    def change_mode(self):
        self._trade_mode = not self._trade_mode


class MarketPanel(arcade.Section):
    """Section where is placed interface to manage trade offers"""

    def __init__(self, trade_manager: TradeManager, left: int, bottom: int, width: int, height: int, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)
        self.trade_manager = trade_manager

    def on_draw(self):
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top,
                                          self.bottom, arcade.color_from_hex_string('#0D0D0D'))
        arcade.draw_lrtb_rectangle_outline(self.left, self.right, self.top,
                                           self.bottom, arcade.color_from_hex_string('#D9BBA0'))
