from enum import Enum


class ResourceType(Enum):
    """Goods the player has. Class extends Resources class (more goods)
    but is used for setting work modes for each building."""

    MONEY, SUPPLY, PEOPLE = 0, 1, 2
    WHEAT, IRON, WOOD = 3, 4, 5
    NULL = 6

    def name(self):
        return str(self)[13:]


class ResourceQuantity:
    """Nice container to send required/produce goods"""

    def __init__(self, resource: ResourceType, quantity: int):
        self.resource = resource
        self.quantity = quantity
