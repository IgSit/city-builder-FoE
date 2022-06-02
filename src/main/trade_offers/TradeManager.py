from src.main.engine import Engine
from src.main.resources.Goods import ResourceQuantity, ResourceType


class Offer:
    def __init__(self, wanted: ResourceQuantity, offered: ResourceQuantity, type_: str):
        self.offered = offered
        self.wanted = wanted
        self.type_ = type_
        self.signboard = self._create_signboard()

    def _create_signboard(self):
        return str(self.wanted.quantity) + " " + self.wanted.resource.name() + " -> " + \
               str(self.offered.quantity) + " " + self.offered.resource.name()


class TradeManager:
    """
    Class to manage trade operations
    """

    def __init__(self, engine: Engine):
        self.engine = engine
        self.active_offers: {Offer} = set()
        # some test offers
        self.active_offers.add(Offer(ResourceQuantity(ResourceType.WOOD, 10),
                                     ResourceQuantity(ResourceType.IRON, 10), "USER_OFFER"))
        self.active_offers.add(Offer(ResourceQuantity(ResourceType.WOOD, 5),
                                     ResourceQuantity(ResourceType.IRON, 10), "BOT_OFFER"))
        self.active_offers.add(Offer(ResourceQuantity(ResourceType.WOOD, 5),
                                     ResourceQuantity(ResourceType.IRON, 15), "BOT_OFFER"))

    def place_offer(self, offer: Offer):
        if offer.type_ == "USER_OFFER" and self.engine.is_valid_offer(offer.offered):
            self.engine.remove_resource(offer.offered)
            self.active_offers.add(offer)

    def remove_offer(self, offer: Offer):
        if offer.type_ == "USER_OFFER" and offer in self.active_offers:
            self.engine.add_resource(offer.offered)
            self.active_offers.remove(offer)

    def accept_offer(self, offer: Offer):
        if offer.type_ == "BOT_OFFER" and self.engine.is_valid_offer(offer.wanted):
            self.engine.add_resource(offer.offered)
            self.engine.remove_resource(offer.wanted)
            self.active_offers.remove(offer)
