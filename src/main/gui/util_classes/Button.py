import arcade

from src.main.gui.util_classes.Point import Point


class Button:
    """
    Class representing a click button having some function triggered on click.
    """

    def __init__(self, title: str, lower_left: Point, upper_right: Point, click_function=None):
        self.title = title
        self.lower_left = lower_left
        self.upper_right = upper_right
        self.click_function = click_function

    def draw_button(self):
        x1, y1 = self.lower_left.x, self.lower_left.y
        x2, y2 = self.upper_right.x, self.upper_right.y
        arcade.draw_polygon_filled([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], arcade.csscolor.GOLD)
        arcade.draw_text(self.title, x1 + abs(x1 - x2) / 4, y1 + abs(y1 - y2) / 4,
                         arcade.color.FRENCH_WINE, font_size=10, bold=True)

    def is_clicked(self, point: Point):
        return self.lower_left.precedes(point) and self.upper_right.follows(point)
