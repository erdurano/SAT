from PySide2.QtCore import QModelIndex, QObject, QRectF, QSize, Qt, Slot, qFuzzyIsNull
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QAbstractItemDelegate, QStyle, QStyleOptionViewItem, QStyledItemDelegate


ItemSize = 256

class PixelDelegate(QAbstractItemDelegate):
    

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent=parent)
        self.pixelSize: int = 12
    
    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex) -> None:
        
        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, option.palette.highlight())
        
        size = min(option.rect.width(), option.rect.height())

        brightness = index.model().data(index, Qt.DisplayRole)
        radius = (size/2) - (brightness/255 * size/2)

        if qFuzzyIsNull(radius):
            return
        
        painter.save()

        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(Qt.NoPen)

        if option.state & QStyle.State_Selected:
            painter.setBrush(option.palette.highlightedText())
        else:
            painter.setBrush(option.palette.text())

        painter.drawEllipse(
            QRectF(
                option.rect.x() + option.rect.width()/2 - radius,
                option.rect.y() + option.rect.height()/2 - radius,
                2*radius, 2*radius
            )
        )

        painter.restore()

    def sizeHint(self, option: QStyleOptionViewItem, index: QModelIndex) -> QSize:
        return QSize(self.pixelSize, self.pixelSize)

    @Slot(int)
    def setPixelSize(self, size: int):
        self.pixelSize = size