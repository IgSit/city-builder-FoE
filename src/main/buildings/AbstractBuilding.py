from abc import ABC, abstractmethod, abstractproperty
from util_classes import Dimensions, Cost


class AbstractBuilding(ABC):

    def __init__(self, name: str, asset_path: str, dimensions: Dimensions, cost: Cost):
        self.name = name
        self.asset_path = asset_path
        self.dimensions = dimensions
        self.cost = cost

