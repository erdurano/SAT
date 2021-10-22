from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow
import os

def main():
    app = QApplication()
    window = MainWindow()
    window.openImage(os.path.join(os.path.dirname(__file__), "images\qt.png"))
    window.show()
    

    return app.exec_()

if __name__ == '__main__':
    main()