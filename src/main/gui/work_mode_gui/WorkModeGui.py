import arcade

from src.main.buildings.AbstractBuilding import AbstractBuilding

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
PANEL_WIDTH = 1000
PANEL_HEIGHT = 666


class WorkModeSection(arcade.View):
    def __init__(self, building: AbstractBuilding):
        global SCREEN_WIDTH, SCREEN_HEIGHT
        super().__init__()
        SCREEN_WIDTH = self.window.width
        SCREEN_HEIGHT = self.window.height
        self.building = building
        self.panel = WorkModePanel(building,
                                   left=(self.window.width - PANEL_WIDTH) / 2, bottom=(1 / 8 * self.window.height),
                                   width=PANEL_WIDTH, height=PANEL_HEIGHT,
                                   prevent_dispatch={True}, prevent_dispatch_view={True})
        self.section_manager.add_section(self.panel)


class WorkModePanel(arcade.Section):

    def __init__(self, building: AbstractBuilding, left: int, bottom: int, width: int, height: int, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)
        self.building = building


class WorkModeCard:

    def __init__(self, building: AbstractBuilding):
        self.building = building
