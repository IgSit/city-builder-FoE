import arcade.window_commands
from ...map.map import Map


class MapGui:

    def __init__(self, game_map: Map):
        self.map_ = game_map
        self.tile_size = 64
        self.mouse_at_field = (0, 0)
        self.x_offset = 0
        self.y_offset = 0
        self.screen_width, self.screen_height = arcade.window_commands.get_display_size()
        self.isometric_map = self._create_map()
        self.middle_points = self._create_middle_points()

    def draw_map(self):
        for x in range(self.map_.length):
            for y in range(self.map_.width):
                polygon = self.isometric_map[x][y]
                polygon = [(x + self.x_offset + self.screen_width // 2,
                            y + self.y_offset + self.screen_height // 16) for x, y in polygon]
                arcade.draw_polygon_outline(polygon, arcade.csscolor.GOLD)

    def _create_map(self):
        return [[self._create_grid(x, y) for x in range(self.map_.length)] for y in range(self.map_.width)]

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

    def _create_middle_points(self):
        return [[(d[0]+abs(d[0]-b[0])/2+self.screen_width//2,
                  a[1]+abs(c[1]-a[1])/2+self.screen_height//16) for a, b, c, d in row] for row in self.isometric_map]

    def draw_free_fields(self):
        for i, row in enumerate(self.map_.free):
            for j, field_free in enumerate(row):
                if field_free:
                    self.mark_field((i, j), arcade.csscolor.GREEN)

    def mark_field(self, point: (int, int), color: arcade.csscolor):
        x, y = point
        polygon = self.isometric_map[x][y]
        polygon = [(x + self.x_offset + self.screen_width // 2, y + self.y_offset + self.screen_height // 16) for x, y in polygon]
        arcade.draw_polygon_filled(polygon, color)

    def find_field_under_mouse(self):
        x, y = self.mouse_at_field
        x -= self.x_offset
        y -= self.y_offset
        closest_mid_pnt_ind = (0, 0)
        for i in range(self.map_.length):
            for j in range(self.map_.width):
                closest_mid_pnt_ind = min(closest_mid_pnt_ind, (i, j), key=lambda t: self._dist(x, y, t[0], t[1]))
        if self.map_.is_free(closest_mid_pnt_ind):
            self.mark_field(closest_mid_pnt_ind, arcade.csscolor.SKY_BLUE)
        else:
            self.mark_field(closest_mid_pnt_ind, arcade.csscolor.RED)
        self.map_.set_chosen_field(closest_mid_pnt_ind)

    def set_mouse_at_field(self, x: float, y: float):
        self.mouse_at_field = (x, y)

    def _dist(self, x: float, y: float, i: int, j: int):
        a, b = self.middle_points[i][j]
        return abs(x-a)+abs(y-b)

    def get_chosen_field_middle_point(self):
        if self.map_.chosen_field is not None:
            a, b = self.map_.chosen_field
            return self.middle_points[a][b]
        return None

    @staticmethod
    def _cartesian_to_isometric(x: int, y: int):
        return [x - y, (x + y) / 2]
