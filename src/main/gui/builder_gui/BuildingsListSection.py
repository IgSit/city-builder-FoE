import arcade
import arcade.gui

from src.main.buildings.BuildingsManager import BuildingsManager
from src.main.gui.util_classes.Button import Button
from src.main.gui.util_classes.Point import Point


class BuildingListSection(arcade.View):

    def __init__(self, builder_gui, buildings_manager: BuildingsManager):
        super().__init__()
        self.width = 320
        self.height = 600
        self.builder_gui = builder_gui
        self.buildings_manager = buildings_manager
        self.panel = Panel(builder_gui, buildings_manager,
                           left=(self.window.width - self.width), bottom=(1 / 8 * self.window.height),
                           width=(self.width - 10), height=self.height,
                           prevent_dispatch={True}, prevent_dispatch_view={True})

        self.section_manager.add_section(self.panel)

    def on_draw(self):
        self.panel.on_draw()


class Panel(arcade.Section):
    """Panel to the right where buildings with build buttons are shown (so-called cards)."""

    def __init__(self, builder_gui, buildings_manager,
                 left: int, bottom: int, width: int, height: int, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)
        self.builder_gui = builder_gui
        self.buildings_manager = buildings_manager
        self.cards = self._create_cards()

    def on_draw(self):
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top,
                                          self.bottom, arcade.color_from_hex_string('#0D0D0D'))
        arcade.draw_lrtb_rectangle_outline(self.left, self.right, self.top,
                                           self.bottom, arcade.color_from_hex_string('#D9BBA0'))

        for card in self.cards:
            card.button.draw_button()
            card.sprite.draw()

    def _create_cards(self):
        cards = []
        for i in range(len(self.buildings_manager.buildings)):
            cards.append(Card(self.builder_gui, self.buildings_manager, i))
        return cards


class Card:
    """Single 'card' containing building sprite and its 'build' button."""

    def __init__(self, builder_gui, buildings_manager, i: int):
        self.builder_gui = builder_gui
        self.buildings_manager = buildings_manager
        lower_left = self._calc_position(i)
        upper_right = lower_left.add(Point(140, 30))
        self.button = Button("Residence", lower_left, upper_right, click_function=self.choose_building, idx=i)
        self.sprite = self.buildings_manager.get_copy(i).sprite
        self.sprite.left = lower_left.x + 35
        self.sprite.bottom = upper_right.y + 15

    def choose_building(self, i: int):
        if self.builder_gui.chosen_building is not None:
            self.builder_gui.chosen_building = None
        else:
            self.builder_gui.chosen_building = self.buildings_manager.get_copy(i)
            self.builder_gui.chosen_building.sprite.bottom = 800

    @staticmethod
    def _calc_position(i: int):
        if i == 0:
            return Point(1045, 500)
        return Point(0, 0)
