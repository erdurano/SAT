import sys

from PySide2.QtGui import QPainter, QBrush, QColor
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import qmlRegisterType
from PySide2.QtCore import QUrl, Property, Signal, Qt, QPointF
from PySide2.QtQuick import QQuickPaintedItem, QQuickView


class TextBalloon(QQuickPaintedItem):

    rightAlignedChanged = Signal()

    def __init__(self, parent=None):
        self._rightAligned = False
        super().__init__(parent)

    @Property(bool, notify=rightAlignedChanged)
    def rightAligned(self):
        return self._rightAligned

    @rightAligned.setter
    def rightAlignedSet(self, value):
        self._rightAligned = value
        self.rightAlignedChanged.emit()

    def paint(self, painter: QPainter):

        brush = QBrush(QColor("#007430"))

        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)

        itemSize = self.size()

        painter.drawRoundedRect(0, 0, itemSize.width(), itemSize.height() - 10, 10, 10)

        if self.rightAligned:
            points = [
                QPointF(itemSize.width() - 10.0, itemSize.height() - 10.0),
                QPointF(itemSize.width() - 20.0, itemSize.height()),
                QPointF(itemSize.width() - 30.0, itemSize.height() - 10.0),
            ]
        else:
            points = [
                QPointF(10.0, itemSize.height() - 10.0),
                QPointF(20.0, itemSize.height()),
                QPointF(30.0, itemSize.height() - 10.0),
            ]
        painter.drawConvexPolygon(points)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    view = QQuickView()
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    qmlRegisterType(TextBalloon, "TextBalloonPlugin", 1, 0, "TextBalloon")
    view.setSource(QUrl.fromLocalFile("qml/mock2.qml"))

    if view.status() == QQuickView.Error:
        sys.exit(-1)
    view.show()

    sys.exit(app.exec_())