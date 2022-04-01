class Map:

    def __init__(self, n: int):
        self.free = [[True for _ in range(n)] for _ in range(n)]
        self.buildings = []
        self.length = n
        self.width = n

    def place_building(self):
        pass