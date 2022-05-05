class Offer:
    def __init__(self, wanted_amount: int, wanted_resource: str, offered_amount: int, offered_resource: str, type_: str):
        self.offered_resource = offered_resource
        self.offered_amount = offered_amount
        self.wanted_resource = wanted_resource
        self.wanted_amount = wanted_amount
        self.type_ = type_
        self.signboard = self._create_signboard()

    def _create_signboard(self):
        return str(self.wanted_amount)+" "+self.wanted_resource+" -> "+str(self.offered_amount)+" "+\
               self.offered_resource


class TradeManager:
    """
    Class to manage trade operations
    """
    def __init__(self):
        self.active_offers: {Offer} = set()
        # some test offers
        self.active_offers.add(Offer(0, "x", 0, "y", "USER_OFFER"))
        self.active_offers.add(Offer(0, "x", 0, "y", "BOT_OFFER"))
        self.active_offers.add(Offer(0, "x", 0, "y", "USER_OFFER"))
        self.active_offers.add(Offer(0, "x", 0, "y", "BOT_OFFER"))
        self.active_offers.add(Offer(0, "x", 0, "y", "BOT_OFFER"))
        self.active_offers.add(Offer(0, "x", 0, "y", "BOT_OFFER"))
        self.active_offers.add(Offer(0, "x", 0, "y", "USER_OFFER"))
        self.active_offers.add(Offer(0, "x", 0, "y", "BOT_OFFER"))
        self.active_offers.add(Offer(0, "x", 0, "y", "BOT_OFFER"))

    def place_offer(self, offer: Offer):
        if offer.type_ == "USER_OFFER":
            # TODO: check if offer is valid
            # TODO: engine -> remove x units of resource X
            pass
        self.active_offers.add(offer)

    def remove_offer(self, offer: Offer):
        if offer.type_ == "USER_OFFER":
            # TODO: engine -> add x units of resource X
            pass
        self.active_offers.remove(offer)

    def accept_offer(self, offer: Offer):
        if offer.type_ == "BOT_OFFER":
            # TODO: check if user has enough resources to accept the offer
            # TODO: engine -> remove x units of resource X, engine -> add y units of resource Y
            self.active_offers.remove(offer)
