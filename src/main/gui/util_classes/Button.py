import arcade
import arcade.gui

from src.main.gui.util_classes.Point import Point


class Button:
    """
    Class representing a click button having some function triggered on click.
    """

    def __init__(self, title: str, lower_left: Point, upper_right: Point, click_function=None, idx=-1):
        self.click_function = click_function
        self.manager = arcade.gui.UIManager()
        self.v_box = arcade.gui.UIBoxLayout()
        self.idx = idx
        self.hidden = False
        self.manager.enable()
        self.enabled = True
        self.title = title

        self.ui_flat_button = arcade.gui.UIFlatButton(text=self.title, width=(upper_right.x - lower_left.x),
                                                      height=(upper_right.y - lower_left.y))
        self.v_box.add(self.ui_flat_button.with_space_around(bottom=10, left=10))
        self.widget = arcade.gui.UIAnchorWidget(
            anchor_x="left", anchor_y="bottom",
            align_x=lower_left.x, align_y=lower_left.y,
            child=self.v_box)
        self.manager.add(self.widget)

        @self.ui_flat_button.event("on_click")
        def on_click_flat_button(event):
            try:
                if self.enabled:
                    click_function()
            except TypeError:
                click_function(self.idx)

    def draw_button(self):
        self.manager.draw()

    def show_button(self):
        if self.hidden:
            self.manager.add(self.widget)
            self.hidden = False

    def hide_button(self):
        if not self.hidden:
            self.manager.remove(self.widget)
            self.hidden = True

    def rename(self, new_title: str):
        self.title = new_title
        self.ui_flat_button.text = self.title
