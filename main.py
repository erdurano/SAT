from PySide2.QtWidgets import QApplication

from main_win import MainWindow

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()

    window.show()

    app.exec_()
