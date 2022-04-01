from abc import ABC, abstractmethod, abstractproperty

import arcade

from src.main.buildings.util_classes import Dimensions, Cost


class AbstractBuilding(ABC):

    def __init__(self, name: str, asset_path: str, dimensions: Dimensions, cost: Cost):
        self.name = name
        self.asset_path = asset_path
        self.dimensions = dimensions
        self.cost = cost
        self.building_sprite = arcade.Sprite(asset_path, 1.5)

