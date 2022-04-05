import arcade

from src.main.buildings.ResidentialBuilding import ResidentialBuilding
from src.main.buildings.util_classes.Dimensions import Dimensions


class BuildingsGui:
    def __init__(self, buildings):
        self.buildings = buildings
        self.building_sprites = arcade.SpriteList()
        self.building_sprites.append(self.buildings.chosen.sprite)

    def set_chosen_coords(self, point: (float, float)):
        if self.buildings.build_mode and self.buildings.chosen is not None:
            x, y = point
            self.buildings.chosen.sprite.center_x = x
            self.buildings.chosen.sprite.center_y = y

    def set_chosen_basic_coords(self, point: (float, float)):
        if self.buildings.build_mode and self.buildings.chosen is not None:
            x, y = point
            self.buildings.chosen.x_coord = x
            self.buildings.chosen.y_coord = y

    def draw_chosen_building(self):
        if self.buildings.chosen is not None:
            self.buildings.chosen.sprite.draw()

    def draw_buildings_on_map(self):
        for building in self.buildings.on_map:
            building.sprite.draw()

    def update_coords(self, x_offset: float, y_offset: float):
        for building in self.buildings.on_map:
            building.sprite.center_x = building.x_coord + x_offset
            building.sprite.center_y = building.y_coord + y_offset
