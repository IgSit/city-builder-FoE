from typing import Optional

from src.main.buildings.AbstractBuilding import AbstractBuilding
from src.main.engine.Engine import Engine
from src.main.gui.builder_gui.BuilderGui import BuilderGui
from src.main.gui.map_gui.MapGui import MapGui
from src.main.gui.work_mode_gui.WorkModeSection import WorkModeSection


class WorkModeGui:
    def __init__(self, map_gui: MapGui, builder_gui: BuilderGui, engine: Engine):
        self.map_gui = map_gui
        self.builder_gui = builder_gui
        self.engine = engine
        self.building: Optional[AbstractBuilding] = None
        self.work_mode_section = WorkModeSection(self.building, self.engine)
        self.set_work_mode = False

    def on_draw(self):
        if self.set_work_mode:
            self.work_mode_section.on_draw()

    def on_mouse_press(self):
        if self.builder_gui.mode is None:
            cords = self.map_gui.find_field_under_cursor()
            if cords is None:
                return
            x, y = cords
            building = self.engine.find_building_at_field(x, y)
            if building is None:
                return
            self.work_mode_section.building = building
            for card in self.work_mode_section.panel.cards:
                card.building = building
            self.set_work_mode = True

    def on_quit(self):
        if self.set_work_mode:
            self.set_work_mode = False
            return True
        return False
