import os
from PySide2.QtCore import QUrl
from PySide2.QtGui import QWindow
from PySide2.QtQuick import QQuickView
from PySide2.QtWidgets import QVBoxLayout, QWidget


class DashWindow(QWindow):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        view = QQuickView()
        container = QWidget().createWindowContainer(self)

        view.setSource(QUrl.fromLocalFile(
            os.path.join(os.path.dirname(__file__), "qml/Dash.qml")))
        layout.addWidget(container)
