from src.main.gui.builder_gui.BuilderGui import BuilderGui
from src.main.gui.util_classes.Button import Button
from src.main.gui.util_classes.Point import Point


class ControlsGui:

    def __init__(self, builder_gui: BuilderGui):
        self.builder_gui: BuilderGui = builder_gui
        self.buttons: [Button] = self._init_buttons()

    def on_draw(self):
        for button in self.buttons:
            button.draw_button()

    def _init_buttons(self):
        funcs = [self._toggle_build_mode, self._toggle_move_mode, self._toggle_sell_mode, self._toggle_tech_mode]
        texts = ["Build", "Move", "Sell", "Tech"]
        buttons: [Button] = []
        for i in range(len(funcs)):
            buttons.append(Button(texts[i], Point(100 * i, 0), Point(100 * (i + 1), 30), click_function=funcs[i]))
        return buttons

    def _toggle_build_mode(self):
        self.builder_gui.builder_mode = not self.builder_gui.builder_mode

    def _toggle_move_mode(self):
        pass

    def _toggle_sell_mode(self):
        pass

    def _toggle_tech_mode(self):
        pass