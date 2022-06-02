import arcade
import arcade.gui

from src.main.buildings.BuildingsManager import BuildingsManager
from src.main.engine.Engine import Engine
from src.main.gui.util_classes.Button import Button
from src.main.gui.util_classes.Point import Point
from src.main.technologies.TechnologiesManager import TechnologiesManager

PANEL_WIDTH = 1000
PANEL_HEIGHT = 666
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0


class TechnologiesSection(arcade.View):
    def __init__(self, buildings_manager, engine: Engine):
        global SCREEN_WIDTH, SCREEN_HEIGHT

        super().__init__()
        SCREEN_WIDTH = self.window.width
        SCREEN_HEIGHT = self.window.height
        self._tech_mode = False
        self.technologies_manager = TechnologiesManager(engine)
        self.buildings_manager = buildings_manager
        self.panel = TechnologiesPanel(self, self.technologies_manager, self.buildings_manager,
                                       left=(self.window.width - PANEL_WIDTH) / 2, bottom=(1 / 8 * self.window.height),
                                       width=PANEL_WIDTH, height=PANEL_HEIGHT,
                                       prevent_dispatch={True}, prevent_dispatch_view={True})
        self.section_manager.add_section(self.panel)

    def on_draw(self):
        if self._tech_mode:
            self.panel.on_draw()

    def on_quit(self):
        if self._tech_mode:
            self._tech_mode = False
            return True
        return False

    def change_mode(self):
        self._tech_mode = not self._tech_mode


class TechnologiesPanel(arcade.Section):

    def __init__(self, technologies_section: TechnologiesSection, technologies_manager: TechnologiesManager,
                 buildings_manager: BuildingsManager, left: int, bottom: int, width: int, height: int, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)
        self.technologies_section = technologies_section
        self.technologies_manager = technologies_manager
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
        # for i in range(len(self.buildings_manager.buildings) - 1):
        #     cards.append(TechnologiesCard(self.buildings_manager, self.technologies_manager, i))
        return cards


class TechnologiesCard:
    """Single 'card' containing building sprite and its 'unlock' button."""

    # TODO change list in buildings_manager to dictionary indexed by names
    # def __init__(self, buildings_manager: BuildingsManager, technologies_manager: TechnologiesManager, names: [str]):
    #     self.technologies_manager = technologies_manager
    #     lower_left = self._calc_position(i)
    #     upper_right = lower_left.add(Point(140, 30))
    #     self.buildings_manager = buildings_manager
    #     self.building_gui = self.buildings_manager.get_copy(i)
    #     self.button = Button(self.building_gui.building.name, lower_left, upper_right,
    #                          click_function=self.choose_building, idx=i)
    #     self.sprite = self.building_gui.sprite
    #     self.sprite.scale = 0.5
    #     self.sprite.left = lower_left.x + 35
    #     self.sprite.bottom = upper_right.y + 15
    #
    # def choose_building(self, i: int):
    #     if self.builder_gui.chosen_building is not None:
    #         self.builder_gui.chosen_building = None
    #     else:
    #         self.builder_gui.chosen_building = self.buildings_manager.get_copy(i)
    #         self.builder_gui.chosen_building.sprite.bottom = 800

    @staticmethod
    def _calc_position(i: int):
        return Point(SCREEN_WIDTH - PANEL_WIDTH + (i % 2) * 150,
                     860 - ((i % 6) // 2) / 3 * PANEL_HEIGHT - 860 / 2.5)
