import arcade.window_commands

from ...map.map import Map


class MapGui:

    def __init__(self, game_map: Map):
        self.map = game_map
        self.tile_size = 64
        self.screen_width, self.screen_height = arcade.window_commands.get_display_size()
        self.isometric_map = self._create_map()

    def draw_map(self):
        for x in range(self.map.length):
            for y in range(self.map.width):
                polygon = self.isometric_map[x][y]
                polygon = [(x + self.screen_width // 2, y + self.screen_height // 16) for x, y in polygon]
                arcade.draw_polygon_outline(polygon, arcade.csscolor.GOLD)
        # arcade.finish_render()

    def _create_map(self):
        return [[self._create_grid(x, y) for x in range(self.map.length)] for y in range(self.map.width)]

    def _create_grid(self, grid_x: int, grid_y: int):
        length = grid_x * self.tile_size
        height = grid_y * self.tile_size
        rectangle = (
            (length, height),
            (length + self.tile_size, height),
            (length + self.tile_size, height + self.tile_size),
            (length, height + self.tile_size)
        )

        return [self._cartesian_to_isometric(x, y) for x, y in rectangle]

    def draw_free_fields(self):
        for i, row in enumerate(self.map.free):
            for j, field_free in enumerate(row):
                if field_free:
                    self.mark_field(i, j)

    def place_on_map(self, x: int, y: int):
        polygon = self.isometric_map[x][y]
        polygon = [(x + self.screen_width // 2, y + self.screen_height // 16) for x, y in polygon]
        arcade.draw_polygon_filled(polygon, arcade.csscolor.GREEN)

    def mark_field(self, x: int, y: int):
        polygon = self.isometric_map[x][y]
        polygon = [(x + self.screen_width // 2, y + self.screen_height // 16) for x, y in polygon]
        arcade.draw_polygon_filled(polygon, arcade.csscolor.GREEN)

    @staticmethod
    def _cartesian_to_isometric(x: int, y: int):
        return [x - y, (x + y) / 3]
