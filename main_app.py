from PySide2.QtWidgets import QApplication
from main_win import MainWindow


class App(QApplication):
    """A class to organize main functions of the application and create
    a bridge between qml and qt components"""

    def __init__(self):
        super().__init__()

        self.main_window = MainWindow()
        self.main_window.show()

        self.main_window.import_button.clicked.connect(mine_turtle)


def mine_turtle():
    print('Hello!')

if __name__ == "__main__":
    app = App()

    app.exec_()