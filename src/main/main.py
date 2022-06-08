from src.main.engine.Engine import Engine
from src.main.gui.gui import Gui

if __name__ == '__main__':
    engine = Engine(10)
    app = Gui(engine)
    app.run()

