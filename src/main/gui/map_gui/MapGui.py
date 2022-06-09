import arcade
from math import inf

from src.main.engine.Engine import Engine
from src.main.gui.building_gui.BuildingGui import BuildingGui
from src.main.gui.util_classes.Point import Point


class MapGui:
    """
    Part of gui containing visual representation of map and its buildings, handling dragging map.
    This class **does not** have access to map itself -
    all operations are done via engine.
    """

    def __init__(self, engine: Engine, tile_size: int = 64):
        self.engine = engine
        self.length, self.width = engine.get_map_dimensions()
        self.tile_size = tile_size
        self.map_buildings: [BuildingGui] = []
        self.offset = Point(0, 0)
        self.mouse_position = Point(0, 0)
        self.screen_width, self.screen_height = arcade.window_commands.get_display_size()
        self.isometric_map = self._create_map()
        self.middle_points = self._create_middle_points()
        self.field_priority = self._create_field_priority()
        self.background_sprite = arcade.Sprite("./gui/map_gui/assets/background.png", center_x=self.screen_width / 2,
                                               center_y=self.screen_height / 2)

    def on_mouse_motion(self, x: float, y: float):
        self.mouse_position = Point(x, y)

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float):
        self.mouse_position = Point(x, y)
        self.offset = self.offset.add(Point(dx, dy))
        self.offset.set_x(min(max(self.offset.x, -500), 500))
        self.offset.set_y(min(max(self.offset.y, -250), 350))

    def on_draw(self):
        self._update_background_coords()
        self.background_sprite.draw()
        for x in range(self.length):
            for y in range(self.width):
                polygon = self.isometric_map[x][y]
                polygon = [(x + self.offset.x + self.screen_width // 2,
                            y + self.offset.y + self.screen_height // 16) for x, y in polygon]
                arcade.draw_polygon_outline(polygon, arcade.csscolor.GOLD)

        self.find_field_under_cursor()

        for building in self.map_buildings:
            if building.building.connected_to_town or building.non_road_sprite is None:
                building.sprite.center_x = building.screen_coordinates.x + self.offset.x
                building.sprite.bottom = building.screen_coordinates.y + self.offset.y
                building.sprite.draw()
            else:
                building.non_road_sprite.center_x = building.screen_coordinates.x + self.offset.x
                building.non_road_sprite.bottom = building.screen_coordinates.y + self.offset.y
                building.non_road_sprite.draw()

    def on_update(self, dt: float):
        for building_gui in self.map_buildings:
            building_gui.building.on_update(dt)

    def find_field_under_cursor(self):
        """
        If cursor is on the map, return the (x, y) tuple containing coordinates of map tile (row/column indexes).
        Else returns None.

        :return: (x, y)
        """
        x, y = self.mouse_position.x, self.mouse_position.y
        x, y = x - self.offset.x, y - self.offset.y
        closest_mid_pnt_ind = (0, 0)
        min_dist = inf
        for i in range(self.length):
            for j in range(self.width):
                closest_mid_pnt_ind = min(closest_mid_pnt_ind, (i, j), key=lambda t: self._dist(x, y, t[0], t[1]))
                min_dist = (self._dist(x, y, closest_mid_pnt_ind[0], closest_mid_pnt_ind[1]))
        if min_dist < 50:
            x, y = closest_mid_pnt_ind
            self.color_tile(x, y)
            return closest_mid_pnt_ind
        return None

    def color_tile(self, x: int, y: int):
        """Colors given tile of a map.

        :param: x: int - row index
        :param: y: int - column index
        :return: void
        """
        if self.is_tile_free(x, y):
            self.mark_field(x, y, arcade.csscolor.SKY_BLUE)
        else:
            self.mark_field(x, y, arcade.csscolor.RED)

    def mark_field(self, x: int, y: int, color: arcade.csscolor):
        """
        Colours given matrix tile in given color
        :param x: int
        :param y: int
        :param color: arcade,csscolor
        :return:
        """
        polygon = self.isometric_map[x][y]
        polygon = [(x + self.offset.x + self.screen_width // 2, y + self.offset.y + self.screen_height // 16)
                   for x, y in polygon]
        arcade.draw_polygon_filled(polygon, color)

    def get_middle_point(self, i: int, j: int):
        return self.middle_points[i][j]

    def remove_building_sprite(self, sprite: arcade.sprite):
        for building in self.map_buildings:
            if building.sprite == sprite or building.non_road_sprite == sprite:
                self.map_buildings.remove(building)

    def _update_background_coords(self):
        self.background_sprite.center_x = self.screen_width / 2 + self.offset.x
        self.background_sprite.center_y = self.screen_height / 2 + self.offset.y

    def _create_map(self):
        """
        Creates iso map containing tiles of a map.
        """
        return [[self._create_tile(x, y) for x in range(self.length)] for y in range(self.width)]

    def _create_tile(self, grid_x: int, grid_y: int):
        """
        Creates tile for iso map at (x, y) position in map array.

        :param grid_x: int - x index of map
        :param grid_y: int - y index of map
        :return: [[x, y] * 4] - polygon coordinates
        """

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
        return [[(d[0] + abs(d[0] - b[0]) / 2 + self.screen_width // 2,
                  a[1] + abs(c[1] - a[1]) / 2 + self.screen_height // 16) for a, b, c, d in row]
                for row in self.isometric_map]

    def _create_field_priority(self):
        n = max(self.width, self.length)
        m = 2 * n - 1 - abs(self.width - self.length)
        priority_map = list(reversed(
            [list(reversed([[i + j, 0] for j in range(self.length)])) for i in range(self.width)])
        )
        x = 0
        y = min(self.width, self.length) - 1
        fields = {(x + i + j, y - i + j): (i, j) for i in range(self.width) for j in range(self.length)}
        k = self.width * self.length - 1
        for i in range(m):
            for j in range(m):
                if (i, j) in fields.keys():
                    a, b = fields[(i, j)]
                    priority_map[a][b][1] = k
                    k -= 1
        return priority_map

    def _dist(self, x: float, y: float, i: int, j: int):
        a, b = self.middle_points[i][j]
        return abs(x - a) + abs(y - b)

    def is_tile_free(self, x: int, y: int):
        return self.engine.is_tile_free(x, y)

    @staticmethod
    def _cartesian_to_isometric(x: int, y: int):
        """
        Changes cartesian coords to isometric.
        :param x:
        :param y:
        :return:
        """
        return [x - y, (x + y) / 2]
