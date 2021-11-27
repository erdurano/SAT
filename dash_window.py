
from PySide6.QtQuickWidgets import QQuickWidget


class DashWindow(QQuickWidget):

    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.setResizeMode(QQuickWidget.SizeRootObjectToView)

        self.setWindowTitle('Dash')
