import arcade

from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.engine.Engine import Engine
from src.main.gui.util_classes.Button import Button
from src.main.gui.util_classes.Point import Point
from src.main.work_modes.WorkModes import WorkMode

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
PANEL_WIDTH = 1000
PANEL_HEIGHT = 300
CARD_WIDTH = 150
CARD_HEIGHT = 200


class WorkModeSection(arcade.View):
    def __init__(self, building: AbstractBuilding, engine: Engine):
        global SCREEN_WIDTH, SCREEN_HEIGHT
        super().__init__()
        SCREEN_WIDTH = self.window.width
        SCREEN_HEIGHT = self.window.height
        self.building: AbstractBuilding = building
        self._work_mode: bool = True
        self.panel = WorkModePanel(building, engine,
                                   left=(self.window.width - PANEL_WIDTH) / 2, bottom=(1 / 8 * self.window.height),
                                   width=PANEL_WIDTH, height=PANEL_HEIGHT,
                                   prevent_dispatch={True}, prevent_dispatch_view={True})
        self.section_manager.add_section(self.panel)

    def on_draw(self):
        if self._work_mode:
            self.panel.on_draw()


class WorkModePanel(arcade.Section):

    def __init__(self, building: AbstractBuilding, engine: Engine,
                 left: int, bottom: int, width: int, height: int, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)
        self.building: AbstractBuilding = building
        self.engine: Engine = engine
        self.cards: [WorkModeCard] = self._create_cards()

    def on_draw(self):
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top,
                                          self.bottom, arcade.color_from_hex_string('#0D0D0D'))
        arcade.draw_lrtb_rectangle_outline(self.left, self.right, self.top,
                                           self.bottom, arcade.color_from_hex_string('#D9BBA0'))

        for card in self.cards:
            card.on_draw()

    def _create_cards(self):
        cards = []
        for work_mode in [WorkMode.EFFICIENT, WorkMode.MODERATE, WorkMode.LAZY]:
            cards.append(WorkModeCard(self.building, self.engine, work_mode))
        return cards


class WorkModeCard:

    def __init__(self, building: AbstractBuilding, engine: Engine, work_mode: WorkMode):
        self.building: AbstractBuilding = building
        self.engine: Engine = engine
        self.work_mode: WorkMode = work_mode

        self.lower_left = WorkModeCard._calc_position(work_mode)
        self.upper_right = self.lower_left.add(Point(CARD_WIDTH, CARD_HEIGHT))

        self.button = Button("Start", lower_left=self.lower_left.add(Point(5, CARD_HEIGHT * 0.75)),
                             upper_right=self.upper_right.subtract(Point(20, CARD_HEIGHT * 0.1)),
                             click_function=self._start_work)

    def on_draw(self):
        arcade.draw_lrtb_rectangle_filled(self.lower_left.x, self.upper_right.x,
                                          self.upper_right.y, self.lower_left.y,
                                          arcade.csscolor.WHEAT)
        arcade.draw_text(WorkMode.get_text(self.work_mode),
                         start_x=WorkModeCard._calc_position(self.work_mode).x + CARD_WIDTH / 9,
                         start_y=WorkModeCard._calc_position(self.work_mode).y + 10,
                         color=arcade.csscolor.NAVY,
                         font_size=20)
        self.button.draw_button()
        if self.building.work_mode == self.work_mode and self.building.time_left > 0:
            self._draw_time()

    def _draw_time(self):
        arcade.draw_text("Time left:",
                         start_x=WorkModeCard._calc_position(self.work_mode).x + CARD_WIDTH / 9 + 10,
                         start_y=WorkModeCard._calc_position(self.work_mode).y + 90,
                         color=arcade.csscolor.DARK_GREEN,
                         font_size=18)
        arcade.draw_text(self._stringify_time(),
                         start_x=WorkModeCard._calc_position(self.work_mode).x + CARD_WIDTH / 9 + 17,
                         start_y=WorkModeCard._calc_position(self.work_mode).y + 60,
                         color=arcade.csscolor.DIM_GRAY,
                         font_size=15)

    def _start_work(self):
        if self.engine.can_start_work(self.building, self.work_mode):
            self.engine.start_work(self.building, self.work_mode)

    def _stringify_time(self):
        hours = int(self.building.time_left // 3600)
        minutes = int(self.building.time_left // 60)
        seconds = int(self.building.time_left % 60)
        return f"{hours:02}:{minutes:02d}:{seconds:02d}"

    @staticmethod
    def _calc_position(work_mode):
        i = 0
        if work_mode == WorkMode.MODERATE:
            i = 1
        if work_mode == WorkMode.LAZY:
            i = 2

        return Point(120 + 300 * i + (SCREEN_WIDTH - PANEL_WIDTH) / 2,
                     PANEL_HEIGHT - 110)
