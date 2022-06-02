from gui.gui import Gui
from engine.Engine import Engine


if __name__ == '__main__':
    engine = Engine(10)
    app = Gui(engine)
    app.run()

