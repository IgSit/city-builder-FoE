import arcade

from src.main.buildings.ResidentialBuilding import ResidentialBuilding
from src.main.buildings.util_classes.Dimensions import Dimensions


class BuildingsGui:
    def __init__(self, gui):
        self.gui = gui
        self.building_sprites = arcade.SpriteList()
        self.chosen_building = ResidentialBuilding("test building", "../assets/test.png", Dimensions(1, 1), 0, 0)
        self.building_sprites.append(self.chosen_building.building_sprite)

    def set_chosen_building_coords(self, x: float, y: float):
        if self.gui.build_mode:
            self.chosen_building.building_sprite.center_x = x
            self.chosen_building.building_sprite.center_y = y