from PySide6.QtQuick import QQuickWindow, QSGRendererInterface
from PySide6.QtWidgets import QApplication

from .main_win import MainWindow

if __name__ == "__main__":
    QQuickWindow.setGraphicsApi(QSGRendererInterface.OpenGLRhi)
    app = QApplication()
    window = MainWindow()

    window.show()

    app.exec()
