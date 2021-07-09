from PySide2.QtWidgets import QApplication, QFileDialog
from main_win import MainWindow


class App(QApplication):
    """A class to organize main functions of the application and create
    a bridge between qml and qt components"""

    def __init__(self):
        super().__init__()

        # widgets and types that's gonna be used in application
        self.main_window = MainWindow()
        self.import_diag = QFileDialog(
                parent=None,
                caption="Import SAT Excel",
                filter="Excel file (*.xlsx)")

        # Connections. Might elaborate with custom signal and slots
        self.main_window.import_button.clicked.connect(filename)

        # Compulsory show method for main window
        self.main_window.show()


def filename():
    a, b = app.import_diag.getOpenFileName()
    print(a, b)


if __name__ == "__main__":
    app = App()

    app.exec_()
