from gui.gui import Gui
from engine.engine import Engine


if __name__ == '__main__':
    engine = Engine(15)
    app = Gui(engine)
    app.run()

