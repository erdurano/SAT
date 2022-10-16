from PySide6.QtQuick import QQuickWindow, QSGRendererInterface
from PySide6.QtWidgets import QApplication

from .main_win import MainWindow


def main():
    QQuickWindow.setGraphicsApi(QSGRendererInterface.GraphicsApi.OpenGLRhi)
    app = QApplication()
    window = MainWindow()

    window.show()

    app.exec()
