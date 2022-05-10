import arcade

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
PANEL_WIDTH = 1000
PANEL_HEIGHT = 666


class WorkModeSection(arcade.View):
    def __init__(self):
        global SCREEN_WIDTH, SCREEN_HEIGHT
        super().__init__()
        SCREEN_WIDTH = self.window.width
        SCREEN_HEIGHT = self.window.height
