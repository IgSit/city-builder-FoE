import arcade

from src.main.gui.Button import Button


class ButtonsGui:
    def __init__(self, gui):
        self.gui = gui
        self.button_list = []
        self._create_button("Build", (10, 160), (10, 50), self.gui.engine.buildings.change_mode)

    def _create_button(self, title: str, x_es: (int, int), y_es: (int, int), action=None):
        button = Button(title, x_es, y_es, action)
        self.button_list.append(button)

    def _draw_button(self, x_es: (int, int), y_es: (int, int), pressed: bool, text: str = ""):
        x1, x2 = x_es
        y1, y2 = y_es
        color = arcade.csscolor.GOLD
        if pressed:
            color = arcade.csscolor.KHAKI
        arcade.draw_polygon_filled([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], color)
        arcade.draw_text(text, x1+abs(x1-x2)/4, y1+abs(y1-y2)/4, arcade.color.FRENCH_WINE, 20, bold=True)

    def are_buttons_pressed(self, x: float, y: float):
        for button in self.button_list:
            x1, x2 = button.x_es
            y1, y2 = button.y_es
            if x1 <= x <= x2 and y1 <= y <= y2 and button.action is not None:
                button.pressed = not button.pressed
                button.action()
                break

    def draw_all(self):
        for button in self.button_list:
            self._draw_button(button.x_es, button.y_es, button.pressed, button.title)

