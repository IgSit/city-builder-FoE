from enum import Enum, auto


class ResourceType(Enum):
    """Goods the player has. Class extends Resources class (more goods)
    but is used for setting work modes for each building."""

    MONEY, SUPPLY, PEOPLE = auto, auto, auto
    WHEAT, IRON, WOOD = auto, auto, auto
    NULL = auto


class ResourceQuantity:
    """Nice container to send required/produce goods"""

    def __init__(self, resource: ResourceType, quantity: int):
        self.resource = resource
        self.quantity = quantity
