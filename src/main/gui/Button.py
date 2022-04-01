class Button:
    def __init__(self, title: str, x_es: (int, int), y_es: (int, int), action=None):
        self.title = title
        self.x_es = x_es
        self.y_es = y_es
        self.action = action
        self.pressed = False