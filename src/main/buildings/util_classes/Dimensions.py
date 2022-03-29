# W rzucie izometrycznym lewa krawędź to szerokość, a prawa krawędź to głębokość
# Wizualnie:
# - \ - szerokość
# - / głębokość

class Dimensions:
    def __init__(self, width: int, depth: int):
        self.width = width
        self.depth = depth
