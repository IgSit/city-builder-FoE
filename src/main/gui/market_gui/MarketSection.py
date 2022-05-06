import arcade

from src.main.gui.util_classes.Button import Button
from src.main.gui.util_classes.Point import Point
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
        self.cards: [OfferCard] = []
        self.panel = MarketPanel(self.trade_manager,
                                 left=(self.window.width - PANEL_WIDTH) / 2, bottom=(1 / 8 * self.window.height),
                                 width=PANEL_WIDTH, height=PANEL_HEIGHT,
                                 prevent_dispatch={True}, prevent_dispatch_view={True})
        self.section_manager.add_section(self.panel)

    def on_draw(self):
        if self._trade_mode:
            self.panel.on_draw()
            self._update_cards()
            for card in self.cards:
                card.on_draw()
                card.enable_button()
        else:
            for card in self.cards:
                card.disable_button()

    def change_mode(self):
        self._trade_mode = not self._trade_mode

    def _update_cards(self):
        i = len(self.cards)
        n = len(self.trade_manager.active_offers)
        if i != n:
            while i < n:
                self.cards.append(OfferCard(self.trade_manager, i))
                i += 1
            while i > n:
                self.cards.pop().disable_button()
                i -= 1
            for i, offer in enumerate(self.trade_manager.active_offers):
                self.cards[i].offer = offer
                self.cards[i].update()


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


class OfferCard:
    """Single offer 'card' containing offer signboard and its button."""

    def __init__(self, trade_manager: TradeManager, i: int):
        self.ind = i
        self.trade_manager = trade_manager
        self.offer = None
        self.lower_left = self._calc_position(i)
        self.upper_right = self.lower_left.add(Point(140, 30))
        self.button = Button("Accept", self.lower_left, self.upper_right,
                             click_function=self._remove_offer, idx=i)

    def on_draw(self):
        if self.offer is not None:
            self.button.draw_button()
            arcade.draw_text(self.offer.signboard, self.lower_left.x + 20, self.lower_left.y + 50,
                             arcade.color.GRAY, 20, 100, 'left')

    def disable_button(self):
        self.button.enabled = False

    def enable_button(self):
        self.button.enabled = True

    def update(self):
        if self.offer.type_ == "BOT_OFFER":
            self.button = Button("Accept", self.lower_left, self.upper_right,
                                 click_function=self._accept_offer, idx=self.ind)
        else:
            self.button = Button("Remove", self.lower_left, self.upper_right,
                                 click_function=self._remove_offer, idx=self.ind)

    def _accept_offer(self):
        self.trade_manager.accept_offer(self.offer)

    def _remove_offer(self):
        self.trade_manager.remove_offer(self.offer)

    @staticmethod
    def _calc_position(i: int):
        return Point(20+(SCREEN_WIDTH - PANEL_WIDTH)/2 + 200*(i % 5),
                     PANEL_HEIGHT - (i // 5)*70)
