import arcade
import arcade.gui

from src.main.buildings.BuildingsManager import BuildingsManager
from src.main.gui.util_classes.Button import Button
from src.main.gui.util_classes.Point import Point
from src.main.technologies.TechnologiesManager import TechnologiesManager

PANEL_WIDTH = 320
PANEL_HEIGHT = 600
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0


class BuildingListSection(arcade.View):

    def __init__(self, builder_gui, buildings_manager: BuildingsManager, technologies_manager: TechnologiesManager):
        global SCREEN_WIDTH, SCREEN_HEIGHT

        super().__init__()
        SCREEN_WIDTH = self.window.width
        SCREEN_HEIGHT = self.window.height
        self.builder_gui = builder_gui
        self.buildings_manager = buildings_manager
        self.panel = Panel(builder_gui, buildings_manager, technologies_manager,
                           left=(self.window.width - PANEL_WIDTH), bottom=100,
                           width=(PANEL_WIDTH - 10), height=PANEL_HEIGHT,
                           prevent_dispatch={True}, prevent_dispatch_view={True})

        self.section_manager.add_section(self.panel)

    def on_draw(self):
        self.panel.on_draw()


class Panel(arcade.Section):
    """Panel to the right where buildings with build buttons are shown (so-called cards)."""

    def __init__(self, builder_gui, buildings_manager, technologies_manager,
                 left: int, bottom: int, width: int, height: int, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)
        self.builder_gui = builder_gui
        self.buildings_manager = buildings_manager
        self.technologies_manager = technologies_manager
        self.cards = self._create_cards()
        self.start_Ind = 0
        self.end_Ind = 6
        self.right_button = Button(">", lower_left=Point(left + 55, bottom - 30), upper_right=Point(left + 105, bottom),
                                   click_function=self.right_shift)
        self.left_button = Button("<", lower_left=Point(left, bottom - 30), upper_right=Point(left + 50, bottom),
                                  click_function=self.left_shift)

    def on_draw(self):
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top,
                                          self.bottom, arcade.color_from_hex_string('#0D0D0D'))
        arcade.draw_lrtb_rectangle_outline(self.left, self.right, self.top,
                                           self.bottom, arcade.color_from_hex_string('#D9BBA0'))
        self.right_button.draw_button()
        self.left_button.draw_button()
        for card in self.cards[self.start_Ind:self.end_Ind]:
            card.button.draw_button()
            card.sprite.draw()

    def right_shift(self):
        if self.end_Ind < len(self.cards):
            self._hide_buttons()
            self.start_Ind = self.end_Ind
            self.end_Ind = min(self.end_Ind + 6, len(self.cards))
            self._show_buttons()

    def left_shift(self):
        if self.start_Ind > 0:
            self._hide_buttons()
            self.end_Ind = self.start_Ind
            self.start_Ind -= 6
            self._show_buttons()

    def _hide_buttons(self):
        for i in range(self.start_Ind, self.end_Ind):
            self.cards[i].button.hide_button()

    def _show_buttons(self):
        for i in range(self.start_Ind, self.end_Ind):
            self.cards[i].button.show_button()

    def _create_cards(self):
        cards = []
        for i in range(len(self.buildings_manager.buildings) - 1):
            cards.append(Card(self.builder_gui, self.buildings_manager, self.technologies_manager, i))
        return cards


class Card:
    """Single 'card' containing building sprite and its 'build' button."""

    def __init__(self, builder_gui, buildings_manager, technologies_manager: TechnologiesManager, i: int):
        self.builder_gui = builder_gui
        self.buildings_manager = buildings_manager
        self.technologies_manager = technologies_manager

        lower_left = self._calc_position(i)
        upper_right = lower_left.add(Point(140, 30))

        self.building_gui = self.buildings_manager.get_copy(i)
        self.button = Button(self.building_gui.building.name, lower_left, upper_right,
                             click_function=self.choose_building, idx=i)
        self.sprite = self.building_gui.sprite
        self.sprite.scale = 0.5
        self.sprite.left = lower_left.x + 35
        self.sprite.bottom = upper_right.y + 15

    def choose_building(self, i: int):
        building = self.buildings_manager.buildings[i].building
        if self.builder_gui.chosen_building is not None:
            self.builder_gui.chosen_building = None
        elif building.is_road() or \
                self.technologies_manager.technologies_dict[building.name].unlocked:
            self.builder_gui.chosen_building = self.buildings_manager.get_copy(i)
            self.builder_gui.chosen_building.sprite.bottom = 800

    @staticmethod
    def _calc_position(i: int):
        return Point(SCREEN_WIDTH - PANEL_WIDTH + (i % 2) * 150,
                     860 - ((i % 6) // 2) / 3 * PANEL_HEIGHT - 860 / 2.5)
