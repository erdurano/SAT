import os
from PySide2.QtCore import QUrl
from PySide2.QtQuickWidgets import QQuickWidget


class DashWindow(QQuickWidget):

    def __init__(self):
        super().__init__()
        self.setSource(QUrl.fromLocalFile(
            os.path.join(os.path.dirname(__file__), 'qml/Dash.qml')
            ))
        self.setResizeMode(QQuickWidget.SizeRootObjectToView)

        self.setWindowTitle('Dash')
