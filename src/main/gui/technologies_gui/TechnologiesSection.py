import arcade
import arcade.gui

from src.main.buildings.BuildingsManager import BuildingsManager
from src.main.engine.Engine import Engine
from src.main.gui.util_classes.Button import Button
from src.main.gui.util_classes.Point import Point
from src.main.technologies.TechnologiesManager import TechnologiesManager, TechnologyBranch

PANEL_WIDTH = 1000
PANEL_HEIGHT = 666
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0


class TechnologiesSection(arcade.View):
    def __init__(self, buildings_manager, technologies_manager: TechnologiesManager, engine: Engine):
        global SCREEN_WIDTH, SCREEN_HEIGHT

        super().__init__()
        SCREEN_WIDTH = self.window.width
        SCREEN_HEIGHT = self.window.height
        self._tech_mode = False
        self.buildings_manager = buildings_manager
        self.technologies_manager = technologies_manager
        self.panel = TechnologiesPanel(self, self.technologies_manager, self.buildings_manager,
                                       left=(self.window.width - PANEL_WIDTH) / 2, bottom=(1 / 8 * self.window.height),
                                       width=PANEL_WIDTH, height=PANEL_HEIGHT,
                                       prevent_dispatch={True}, prevent_dispatch_view={True})
        self.section_manager.add_section(self.panel)

    def on_draw(self):
        if self._tech_mode:
            self.panel.on_draw()

    def on_quit(self):
        self.panel.on_quit()
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
            card.on_draw()

    def on_quit(self):
        for card in self.cards:
            card.on_quit()

    def _create_cards(self):
        cards = []
        for i, tech_branch in enumerate(self.technologies_manager.technologies_branches):
            cards.append(TechnologiesCard(self.buildings_manager, self.technologies_manager, tech_branch, i))
        return cards


class TechnologiesCard:
    """Single 'card' containing 3 buildings sprites and its' 'unlock' buttons."""

    def __init__(self, buildings_manager: BuildingsManager, technologies_manager: TechnologiesManager,
                 technology_branch: TechnologyBranch, i: int):
        self.technologies_manager = technologies_manager
        lower_left = self._calc_position(i)
        upper_right = lower_left.add(Point(180, 40))
        distance = 200
        self.buildings_manager = buildings_manager
        self.technology_branch = technology_branch

        state = self._postfix(self.technology_branch.basic.unlocked)
        self.building_gui_basic = self.buildings_manager.get_copy_by_name(self.technology_branch.basic.name)
        self.button_basic = Button(self.technology_branch.basic.name+state, lower_left, upper_right,
                             click_function=self.technology_branch.basic.unlock, idx=i)
        self.sprite_basic = self.building_gui_basic.normal_sprite
        self.sprite_basic.scale = 0.5
        self.sprite_basic.left = lower_left.x + 50
        self.sprite_basic.bottom = upper_right.y + 15

        upper_right.y -= distance
        lower_left.y -= distance

        state = self._postfix(self.technology_branch.intermediate.unlocked)
        self.building_gui_intermediate = self.buildings_manager.get_copy_by_name(self.technology_branch.intermediate.name)
        self.button_intermediate = Button(self.technology_branch.intermediate.name+state, lower_left, upper_right,
                             click_function=self.technology_branch.intermediate.unlock, idx=i+1)
        self.sprite_intermediate = self.building_gui_intermediate.normal_sprite
        self.sprite_intermediate.scale = 0.5
        self.sprite_intermediate.left = lower_left.x + 50
        self.sprite_intermediate.bottom = upper_right.y + 15

        upper_right.y -= distance
        lower_left.y -= distance

        state = self._postfix(self.technology_branch.advanced.unlocked)
        self.building_gui_advanced = self.buildings_manager.get_copy_by_name(self.technology_branch.advanced.name)
        self.button_advanced = Button(self.technology_branch.advanced.name+state, lower_left, upper_right,
                             click_function=self.technology_branch.advanced.unlock, idx=i+2)
        self.sprite_advanced = self.building_gui_advanced.normal_sprite
        self.sprite_advanced.scale = 0.5
        self.sprite_advanced.left = lower_left.x + 50
        self.sprite_advanced.bottom = upper_right.y + 15
        self.button_names = [(self.button_basic, self.technology_branch.basic),
                             (self.button_intermediate, self.technology_branch.intermediate),
                             (self.button_advanced, self.technology_branch.advanced)]

    def on_draw(self):
        for button, tech in self.button_names:
            button.rename(tech.name + self._postfix(tech.unlocked))
            button.enabled = True
            button.draw_button()
        # self.button_basic.enabled = True
        # self.button_intermediate.enabled = True
        # self.button_advanced.enabled = True
        self.sprite_basic.draw()
        # self.button_basic.draw_button()
        self.sprite_intermediate.draw()
        # self.button_intermediate.draw_button()
        self.sprite_advanced.draw()
        # self.button_advanced.draw_button()

    def on_quit(self):
        self.button_basic.enabled = False
        self.button_intermediate.enabled = False
        self.button_advanced.enabled = False

    @staticmethod
    def _postfix(state: bool):
        if state:
            return " UNLOCKED"
        return " UNLOCK"

    @staticmethod
    def _calc_position(i: int):
        return Point((SCREEN_WIDTH - PANEL_WIDTH)//2 + i * 200,
                     PANEL_HEIGHT - (SCREEN_HEIGHT - PANEL_HEIGHT)//2)
