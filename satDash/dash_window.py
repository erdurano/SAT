import os
from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtQuickWidgets import QQuickWidget


class DashWindow(QQuickWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowIcon(QIcon(QPixmap('./rsrc/img/cemre_logo.ico')))

        self.setResizeMode(QQuickWidget.SizeRootObjectToView)

        self.setWindowTitle('Dash')
        self.hide()

    def setDashRoot(self):
        self.setSource(
            QUrl.fromLocalFile(
                os.path.join(os.path.dirname(__file__), "qml/Dash.qml")
            )
        )
